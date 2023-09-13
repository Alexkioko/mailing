import sys, smtplib, ssl
from validator_collection import checkers
from email.message import EmailMessage

def main():
    filename = get_file_name()
    recipient_emails = get_recipient_emails(filename)
    send_attached_mail(recipient_emails)

def get_file_name():
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) < 2:
        filename = input("Enter the name of the file containing user email addresses. (should be a text(.txt) file in this directory) ")
    else:
        filename = sys.argv[1]


    if filename.endswith(".txt"):
        return filename 
    else:
        sys.exit('File entered not a text(.txt) file.')

def get_recipient_emails(s):
    user_emails = []
    with open(s, 'r') as file:
        emails = file.readlines()
        cleaned_emails = [email.strip() for email in emails]
        if len(emails) != 0:
            for email in cleaned_emails:
                if checkers.is_email(email):
                    user_emails.append(email)
                else:
                    print(f"{email} is not a valid email")
 
            return user_emails
        else:
            sys.exit("No emails found in the text file")

def send_attached_mail(s):
    sender_email = input("Enter the email address of the sender (use gmail account)")
    password = input("Enter your email address ") 
    port = 587 #using tls
    context = ssl.create_default_context() #create default context

    for recipient_email in s:
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = 'Test email attached file'

        #plain text
        plain_text = 'This is the plain text for a test email containing attached file. Just checking how it works.'
        msg.set_content = plain_text

        #html version
        html_content = f'''
            <html> 
                <body> 
                    <p> This is a html version for this test email containing an attached file. Just checking how it works </p>
                </body>
            </html>
        '''

        msg.add_alternative(html_content, subtype="html")

        #file attachment
        #send pdf file as attachment
        with open("example.pdf", "rb") as content_file:   #rb denotes the file should be opened in both the read and binary modes
            content = content_file.read()   #read() function reads the content of the file and returns it as binary data
            msg.add_attachment(content, maintype="application", subtype="d", filename="example.pdf")

        #send image as attachment
        with open("example.jpg", "rb") as content_file:   
            content = content_file.read()  
            msg.add_attachment(content, maintype="image", subtype="jpg", filename="example.jpg" )
         

        #run mail server
        with smtplib.SMTP('smtp.gmail.com', port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(msg)


if __name__ == '__main__':
    main()
    
