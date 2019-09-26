import smtplib, sys

smtp_port = 465  # For SSL
smtp_server = "smtp.gmail.com"
smtp_login = "user@gmail.com"
smtp_pwd = "password"

sender_email = "NMX@harmonicinc.com"
receiver_email = "reciever@email.com"
message = """\
Subject: NMX Alarm Notifications"""

#192.168.41.11 Encoder-4 Encoder-4 192.168.1.99 NG-1 Site-1 6-Critical 09/20/2019 13:57:09:057 Service Affecting 0.000000 Timeout [ Encoder-4 ] [ Device timed out ]
message = message + "\n" + " ".join(sys.argv[8:10]) + " |" + sys.argv[7] + "|" + sys.argv[5] + "|" + sys.argv[2]  + "| " + " ".join(sys.argv[13:])

server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.ehlo()
server.login(smtp_login, smtp_pwd)
server.sendmail(sender_email, receiver_email, message)
server.close()