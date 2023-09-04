import sys, csv, smtplib, ssl
from validator_collection import checkers
from email.message import EmailMessage

def main():
    filename = get_file_name()
    recipient_emails = get_recipient_emails(filename)
    send_mail(recipient_emails)

def get_file_name():
    '''
    Check if user added the text file to the CLI command
    If not, ask user for name of file
    Confirm file is a text file
    :return: A text file containing the recipients' emails
    '''
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
    '''
    Read user email from text file
    Add emails to a list
    :param s: text file
    :return: list of recipient emails
    :rtype: list
    '''
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


def send_mail(s):
    '''
    Send email to all the recipients
    :param s: list of recipient emails
    '''
    sender_email = input("Enter the email address of the sender (use gmail account)")
    password = input("Enter your password: ")
    port = 587 #using tls
    context = ssl.create_default_context() #create default context

    for recipient_email in s:
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = 'Test email'

        #plain text
        plain_text = 'This is the plain text for a test email. Just checking how it works.'
        msg.set_content = plain_text

        #html version
        html_content = f'''
            <html> 
                <body> 
                    <p> This is a html version for this test email. Just checking how it works </p>
                </body>
            </html>
        '''

        msg.add_alternative(html_content, subtype = "html")

        with smtplib.SMTP("smtp.gmail.com", port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(msg)





if __name__ == "__main__":
    main()   
