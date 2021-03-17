# BiliReminder

A toolkit will be automatically notified by email when there is a bilibilier update.

## What is BiliReminder ?

## How to use it ?

### Environment

- git
- Python3

### Step

Make sure Python3 works on your computer.

Enter the following code on the command line

```shell
git clone https://github.com/HoBeedzc/BiliReminder.git
cd BiliReminder
```

Before you use this tool for the first time, you need to configure it.

open config.py and enter some infomation about your bilibili account and email.(Click [here](#Config) to find detail infomation.)

If you are using Linux, you can enter following code on the command line to edit this file.

```shell
sudo vim ./bili_reminder/config.py
```

After configuring it, enter following code to start your BiliReminder !

```shell
python main.py
```

### Config

```Python
HEAD
SMTP_SERVER
PORT
FROM_ADDR
PASSWD
TO_ADDR

# Your bilibili uid
# Default: None
BILIBILI_UID

# Your bilibili cookies
# Default: None
# It not necessary unless the number of Uploaders you followed more than 250.
BILIBILI_COOKIES

# The format of email content you want to receive.
# Default: '''你关注的up主更新了！\nup主:{uploader},\n稿件:{manuscript},\n点此可直接观看:{link}'''
# If you want to edit it, please do not change {uploader},{manuscript} and {link}. Otherwise, the program may not work properly.
CONTENT

# The time interval between two inspections
# Default: 60 (seconds)
# Please do not set it little than 60, otherwise the program may not work properly.
SLEEP_TIME 


MAX_PAGE 
```


**[Chinese Version](./README_zh-CN.md)**
