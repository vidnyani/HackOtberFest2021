import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

f1 = open('csv file dir', 'r')

for x in f1:
    lis = x.split(',')
    name = (lis[1] + " " + lis[2])
    email = lis[3]
    link = lis[4]
    from_addr="your email"
    to_addr=[email]
    msg=MIMEMultipart()
    msg['From']=from_addr
    msg['To']=" ,".join(to_addr)
    msg['subject']='your sub'

    body= """ 
    <section style="text-align:center;">
        ***body here***
    </section>
    """

    msg.attach(MIMEText(body,'html'))

    email='your email'
    password='your pass'

    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)
    text=msg.as_string()
    mail.sendmail(from_addr,to_addr,text)
    mail.quit()
    