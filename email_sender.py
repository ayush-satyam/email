import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'Ayush Kumar'
email['to'] = 'seattledon22@gmail.com'
email['subject'] = 'Cogratulation! You won 1,000,000dollars'
email.set_content('I am a Python Rookie! ')
with smtplib.SMTP(host='smtp.google.com',port=465) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('ksidhant028@gamail.com', 'KSIDHANT028@GMAIL')
	smtp.send_message(email)
	print('all good boss!')