import mail
print("connected")
m = mail.login()
details = {}
details["client"] = m
details["to"] = input("mail")
details["message"] = "hello"
details["subject"] = "hello"
times = input("amoun tof times")
for i in range(int(times)):
    mail.send(details)