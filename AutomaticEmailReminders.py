def varyTime():
    #Vary Email Send Time; Reduces Chances of Email Going to Spam
    import random
    timeVariation = random.randint(0,120)
    return timeVariation


import smtplib
import time
import random


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = "Hello everyone,\n Reminder that the ***INSERT EVENT NAME*** event is in 30 minutes at ***INSERT EVENT TIME***!\n Please try to join.\n Thank you!"

#One Day Before. Events are added by Hour-Minute-Second time (# of seconds after 00:00 on Monday).
dayBeforeTimes = {
    320400: "ExampleFileName.txt", #Reminder at Thursday 3:30 (Event: Friday 4-5)
}
#320400 represents Thursday at 3:30 PM, the time the One Day Prior Reminder will be sent.



#Used in Email Send Time Variation; Reduces Email Going to Spam Folder
onHoldTimesDayBefore = {}


namesDict = {
    "ExampleEventReminder" : "Your Example Event"
}
#ID to Name (For Example, Stored as "SubmissionDate"; Reminder Email should say "Your Submission Date")    


#Each day by Hour-Minute-Second Time (Starting at 00:00 on Monday = 0 seconds)
days = {
    "Monday": 0,
    "Tuesday": 86400,
    "Wednesday": 172800,
    "Thursday": 259200,
    "Friday": 345600,
    "Saturday": 432000,
    "Sunday": 518400
}


#Reverse of namesDict
emailDict = {

}




print("Make sure you have entered the day properly, or all timings will be wrong!")
dayInput = input("What day is it currently: ")


hoursInput = int(input("How many HOURS has it been since midnight: "))
minuteInput = int(input("How many MINUTES into the HOUR has it been: "))

curTime = days[dayInput]
curTime += 3600 *hoursInput
curTime += 60*minuteInput


while True:
    curTime += 1 
    if curTime in dayBeforeTimes:
        sendNowOrLater = random.randint(0,1)
        if sendNowOrLater == 0:
            w = open(dayBeforeTimes[curTime])
            recepients = []
            x = w.readline().strip()
            while x != "":
                recepients.append(x)
                x = w.readline().strip()

            name = dayBeforeTimes[curTime]
            pos = 0
            while name[pos] != '.':
                pos += 1
            name = name[0:pos]
            
            sender_address = "" 
            sender_pass = ""   #Create an APP PASSWORD and copy paste it here
            receiver_address = recepients
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = ", ".join(receiver_address)
            message['Subject'] = namesDict[name] + ' event Reminder!'
            
            
            #Can be changed to whatever message you plan to send!!!
            emailfile = open(emailDict[namesDict[name]])
            msg = "Hello,\n Reminder that the " + namesDict[name] + " event is tomorrow!\n"
            x = emailfile.readline().strip()
            while x != "end":
                msg += x
                msg += "\n"
                x = emailfile.readline().strip()
            message.attach(MIMEText(msg, "plain", "utf-8"))            

            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print('Mail Sent')
        else:
            variation = varyTime()
            onHoldTimesDayBefore[curTime+variation] = dayBeforeTimes[curTime]

        
    if curTime in onHoldTimesDayBefore:
        w = open(onHoldTimesDayBefore[curTime])
        recepients = []
        x = w.readline().strip()
        while x != "":
            recepients.append(x)
            x = w.readline().strip()

        name = onHoldTimesDayBefore[curTime]
        pos = 0
        while name[pos] != '.':
            pos += 1
        name = name[0:pos]
        

        sender_address = "" 
        sender_pass = ""   #Create an APP PASSWORD and copy paste it here
        receiver_address = recepients
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = ", ".join(receiver_address)
        message['Subject'] = namesDict[name] + ' event Reminder!'
        
        
        #Can be changed to whatever message you plan to send!!!
        emailfile = open(emailDict[namesDict[name]])
        msg = "Hello,\n Reminder that the " + namesDict[name] + " event is tomorrow!\n"
        x = emailfile.readline().strip()
        while x != "end":
            msg += x
            msg += "\n"
            x = emailfile.readline().strip()
        message.attach(MIMEText(msg, "plain", "utf-8"))        

        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')

           
    if curTime == 604799:
        curTime = 0
    time.sleep(1)