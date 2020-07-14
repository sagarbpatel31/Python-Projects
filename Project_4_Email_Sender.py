import smtplib as st

to=input("Enter the Email id of the recipient:  ")
content=input("Enter the content for mail:  ")

def SendEmail(to,content):
    server=st.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('email id','passwd')
    server.sendmail('email id',to,content)
    server.close()

SendEmail(to,content)
