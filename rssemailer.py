#!/usr/bin/env python
# -*- coding: latin-1 -*-
import feedparser
import argparse
import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def getDate():
    now = datetime.datetime.now()
    return str(now.strftime("%Y-%m-%d %H:%M"))

def arguments():
    parser = argparse.ArgumentParser(description="Options to parse rss feed")
    parser.add_argument("-p","--posts" , type=int, default=1,help="Set nr of posts from each feed (default = 1)")
    parser.add_argument("-t","--target", type=str,default="rss@example.com", help="Set target email address which will recieve updates")
    parser.add_argument("-f", "--feeds", type=str, default="./feeds.txt", help="Set path to feed file (default = ./feeds.txt)")
    parser.add_argument("--to-screen", type=str,help="print feed to screen")
    return parser.parse_args()

def sendEmail(content,target):
    fromaddr = "from@example.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = target
    msg['Subject'] = "RSS update from " + getDate() 

    msg.attach(MIMEText(''.join(content), _charset="UTF-8"))

    server = smtplib.SMTP('mail.example.com', 2525)
    server.starttls()
    server.login(fromaddr, "PASSWORD")
    text = msg.as_string()
    server.sendmail(fromaddr, target, text)
    server.quit()

def getFeeds(feedPath):
    allFeeds = []
    file = open(feedPath,'r')
    for line in file:
        allFeeds.append(feedparser.parse(line))

    file.close()
    return allFeeds

def main():
    # Get arguments,
    args = arguments() 
    postsPerFeed = args.posts
    target = args.target
    feeds = getFeeds(args.feeds)
    
    print("Started to parse feeds...\n")
    emailContent = "Email with the latest updates from: "+ str(len(feeds)) + " feeds!\nFeed will be sent to: " + str(target)
    emailContent += "\n===================================================\n"
    for feed in feeds:
        for x in range(postsPerFeed):
            emailContent += feed.entries[x].title + ":" + feed.entries[x].link + "\n\n"
            #print emailContent
    sendEmail(emailContent,target)
    print("Email sent to: " +str(target) + " with latest update from feeds\nThanks for using RssEmail sender!")
    
if __name__ == '__main__':
  main()
