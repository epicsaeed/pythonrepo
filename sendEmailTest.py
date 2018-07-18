import smtplib

myemail = "salnuaimi@newstore.com"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(myemail,"lungpbxybvpqgarm")

msg = "testing python script"
server.sendmail(myemail,"saeed@nuaimi.net",msg)
server.quit()

