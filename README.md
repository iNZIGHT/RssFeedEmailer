# RssEmailer
Simple RSS feed emailer made with Python.

## Install
First of all clone the repository
```
git clone https://github.com/iNZIGHT/RssEmailer.git
```
and install requirements with
```
pip install -r requirements.txt
``` 
preferably in a virtual environment.

## Prerequisites 
Ok, in order to make this work  you *need* to perform certain changes in the **sendEmail** function:
  * Change sender email address ```fromaddr = "from@example.com" ```
  * Change outgoing emailserver as well as port ```server = smtplib.SMTP('mail.example.com', 1337)```
  * Add you password to ```server.login(fromaddr, "PASSWORD")```
  
One last thing. You need to change default argument for the target email address in the **arguments** function. This allows for usage without explicit passing target email as argument.

## Usage
Simply issue 
```
python rssemailer.py
```
to execute the program in default mode. 
### Optional arguments 
```
usage: rssemailer.py [-h] [-p POSTS] [-t TARGET] [-f FEEDS]

Options to parse rss feed

optional arguments:
  -h, --help            show this help message and exit
  -p POSTS, --posts POSTS
                        Set nr of posts from each feed (default = 1)
  -t TARGET, --target TARGET
                        Set target email address which will recieve updates
  -f FEEDS, --feeds FEEDS
                        Set path to feed file (default = ./feeds.txt)
```
