import smtplib
smtpserver = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtpserver.ehlo()
smtpserver.login('<email id>', '<password>')

FROM="<pesu io email id>"
SUBJECT="<Subject here>"
TEXT="Respected sir/madam,\n<Your content here> \n\nYour group presentation video link is here:\n"
ENDER="\n\nThank you,\nTeam PESU IO"

def send_mail(send_to,video_link):
	TO=send_to
	message = """From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ""+TO, SUBJECT, TEXT+video_link+ENDER)
	smtpserver.sendmail(FROM,TO, message)

fp=open("emails.csv")  #your csv file should be here named emails.csv
count=0
lines=fp.readlines()
print(lines)
fk=open("report.txt","w+")
for line in lines:
	x=line.split(",")
	to=x[0]                    #column number of emails 0 here
	video_link=x[1].rstrip("\n")            #column number of video link 1 here
	try:
		send_mail(to,video_link)
		fk.write(to)
	except:
		print(to+" not valid") #prints all invalid email adresses

smtpserver.close()
