import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import os

file_directory = fd.askopenfilename()
print(file_directory)

# Open the file in read mode
with open(str(file_directory), "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Print the line
        print(line)
        
        #Open ytdl and download the video from the url
        os.chdir('{}'.format('C:\ytdl'))
        os.system('yt-dlp "' + str(line) + '"')

#Disclaimer: If you only want to convert files and do not want for the program to notify you via Discord, then delete any subsequent code!

#Send a webhook reminder request
from discord_webhook import DiscordWebhook
webhook = DiscordWebhook(url='Your webhook url here', content='Your download has finished!') #Write the webhook url here
response = webhook.execute()

