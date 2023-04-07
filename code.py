import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import os
import re

answer = input('Do you want to bulk input through a txt list? (y/n): ') 
notiftoggle = input('Do you want to receive a discord notification? (y/n): ')

if answer == 'y':
    file_directory = fd.askopenfilename
    print(file_directory)
    # Open the file in read mode
    with open(str(file_directory), "r") as file:
        # Iterate through each line in the file
        for line in file:
            # Validate the URL format using a regular expression
            if not re.match(r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', line.strip()):
                print('Invalid YouTube URL: ' + line.strip())
                continue

            # Print the line
            print(line)
        
            #Open ytdl and download the video from the url
            os.chdir('{}'.format('C:\ytdl'))
            os.system('yt-dlp "' + str(line) + '"')
elif answer == 'n':
    url = input('Please input the video URL: ')

    # Validate the URL format using a regular expression
    if not re.match(r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', url.strip()):
        print('Invalid YouTube URL: ' + url.strip())
        exit()

    os.chdir('{}'.format('C:\ytdl'))
    os.system('yt-dlp "' + str(url) + '"')
else:
    print('Invalid input, please try again')
    exit()

#Disclaimer: If you only want to convert files and do not want for the program to notify you via Discord, then delete any subsequent code!

#Send a webhook reminder request
if notiftoggle == 'y':
    from discord_webhook import DiscordWebhook
    webhook = DiscordWebhook(url='[INSERT THE WEBHOOK URL HERE]', content='Your download has finished!') #Write the webhook url here
    response = webhook.execute()
elif notiftoggle == 'n':
    print('Download successful!')
else:
    print('Invalid notification toggle, defaulting to no notification')

