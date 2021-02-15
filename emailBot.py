import smtplib, ssl
from datetime import datetime
#CONSTANTS
context = ssl.create_default_context() #Ignore this, it is just setting up the enviroment
port = 465 #This is the port number that hosts google, may need to be changed if you are using outlook
SENDER_EMAIL = "" #This is the email addres of the account you are sending from
RECEIVER_EMAIL = "" #This is the email addres of the account you are sending to
PASSWORD = ""


EMAIL_NUM = 5 #This is the number of emails you would like it to perform
SPACE_BETWEEN = 20 #This is the amount of time you want between emails. (NOTE: set to minutes, for debugging, currently set to seconds


trueFalse = True #ignore these, simply temporary variables for functionality
counter = 0
temp = 0
with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login(SENDER_EMAIL, PASSWORD)
    
    while counter < EMAIL_NUM:
        now = datetime.now()
        seconds = int(now.strftime("%S"))
        minutes = int(now.strftime("%M"))
        hours = int(now.strftime("%H"))
        #dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if trueFalse == False:
            if seconds%SPACE_BETWEEN == 0:
                message = """\
Subject: Hi there

This message is sent from Python.
Testing
The time is {}:{}:{}""".format(hours, minutes, seconds)
                server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
                trueFalse = True
                print("sent")
                counter += 1
        elif trueFalse == True:
            if seconds%SPACE_BETWEEN == 0 and seconds != temp:
                temp = seconds
                trueFalse = False


