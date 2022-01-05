import os
import random
from email.message import EmailMessage
import smtplib




def sendmail():
    user = input(f" Enter your Name: ")
    email = input(f" Enter email id: ")
    message = f" Dear {user} welcome to the website"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("invincible.amits@gmail.com", "pbslgnbrjcquawlb")
   # msg = EmailMessage()
    #msg.set_content("This is my message to you")
    #s.send_message(msg)
    s.sendmail('invincible.amits@gmail.com', email, message)

    print("Email Sent!")

sendmail()
