# Developed by Navin Khanthawong 

import os
import ctypes
import time
import requests
import urllib.request
from datetime import datetime as date

# schedules object
class timeSchedule(object):
    def __init__(self , title , message , icon , timeout):
        self.title = title
        self.message = message
        self.icon = icon
        self.timeout = timeout

# schedules Setting 
def setSchedules(schedules , now ,title , message , icon , setTimeout):
    schedules[now] = timeSchedule(title , message , icon , setTimeout)
        
# get Current Hour
def getHour():
    dateNow = date.now()
    hour = dateNow.hour
    return hour 

# get Quotes API
def getData():
    try:
        url = "https://zenquotes.io/api/quotes"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            quotes = data[0]
            print("\t --- Quotes : ---  \n" , quotes['q'])
            print("\t --- Author : ---  \n" , quotes['a'])
            return [quotes['q'] , quotes['a']]
    except Exception as err:
        print("Error :" , err)


# get Image API
def getImage():
    try :
        accessKey = "YOUR_API_KEY"
        url = f'https://api.unsplash.com/photos/random/?client_id={accessKey}&orientation=landscape&h=4000&w=2160&fit=max'
        response  = requests.get(url)                  # HTTP get Resquest
        if response.status_code == 200 :
            data = response.json()                     # Image Data as json
            randomPhoto = data['urls']['raw']          # get URL
            print("Random Photo : \n" , randomPhoto)
            return randomPhoto
        else : 
            print("ERROR Failed to Call API")
        print(response)
    except Exception as err:
        print('Error : ' , err)


# Download Image
def downloadImage(imageURL , filepath):
    urllib.request.urlretrieve(imageURL , filepath) # DownloadImage
    print("\t --- Image Download Sucessful ---")


# Change Background
def changeBackground(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath , 0)

# change PC background program interface
def ChangePCBackgroundProgram(filepath): 
    imageURL = getImage()                       # call API getImage
    downloadImage(imageURL , filepath)          # download Image from url to System
    changeBackground(filepath);                 # change Background


# Program life cycle
def systemLoop(seconds , filepath):
    cycleCount = 1;
    while True:
        ChangePCBackgroundProgram(filepath)         # change PC Background
        # notificationProgram()                       # push  PC notification
        print("\t Background Number : ",cycleCount)
        cycleCount = cycleCount + 1                 # cycle count
        time.sleep(seconds)                         # wait N second


# Main Program 
def main():
    filepath = "SourcePath_To_Folder_EndingWith_BackgroundImage.jpg" # "C:\\Users\\Asus\\python\\program\\backgroundProgram\\BackgroundImage.jpg"
    seconds = 72                                        # 72 * 50 = 3600 seconds = 1 hour
    systemLoop(seconds , filepath);                     # System Life Cycle

main()                                                  # Run the Program

# Install Liberys for Begin
# Request Are limited to 50 requests per hour.
# https://api.unsplash.com/photos/?client_id=YOUR_ACCESS_KEY
# https://unsplash.com/documentation




