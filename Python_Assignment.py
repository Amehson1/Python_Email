import datetime
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Dictionary of friends and their information
friends = {
    'Samson Daniel': {'email': 'samsonobera@gmail.com', 'birthday': '1998-06-22', 'anniversary': '1988-07-12', 'phone': '08074160084'},
    'Nelson Amehson':  {'email': 'nelsonamehson@gmail.com', 'birthday': '1986-07-29', 'anniversary': '2014-04-06', 'phone': '09056941678'},
    'Amehson Endure':{'email': 'endure@gmail.com', 'birthday': '1999-09-01', 'anniversary': '1999-03-09', 'phone': '07065789812'},
    'Fiath Gabriel':{'email': 'faithgabriel@gmail.com', 'birthday': '1997-07-05', 'anniversary': '1987-03-09', 'phone': '08056879052'}
}

# Email server and account information
smtp_server = 'sundayamehson@gmail.com'  # Replace with your email provider's SMTP server
smtp_port = 465 
sender_email = 'sundayamehson@gmail.com'  
sender_password = 'vvqmejiiybiozwji'  

# Today's date
today = datetime.date.today()

# Loop through each friend
for friend, info in friends.items():
    # Get the friend's birthday and anniversary dates
    birthday = datetime.datetime.strptime(info['birthday'], '%Y-%m-%d').date()
    anniversary = datetime.datetime.strptime(info['anniversary'], '%Y-%m-%d').date()

    # Check if today is the friend's birthday or anniversary
    if today.month == birthday.month and today.day == birthday.day:
        subject = f"Happy Birthday, {friend}!"
        message = f"Dear {friend},\n\nWishing you a happy birthday and all the best for the year ahead!\n\nBest regards,\n\nAmehson Sunday"
    elif today.month == anniversary.month and today.day == anniversary.day:
        subject = f"Happy Wedding Anniversary, {friend}!"
        message = f"Dear {friend},\n\nWishing you a happy wedding anniversary and all the best for the years ahead!\n\nBest regards,\n\nAmehson Sunday"
    else:
        continue

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = info['email']
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        # server.login(sundayamehson@gmail.com, Sunny3617)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, info['email'], msg.as_string())

    # Print a confirmation message
    print(f"Sent email to {friend} ({info['email']})") 
