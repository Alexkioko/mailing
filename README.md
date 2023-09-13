# Mailing
 Sending the same version of an email to multiple recipients with python
 '''
# # Installation

-> In your virtual environment run the following command:

    - pip install -r requirements.txt
    
-> Add the file containing the recipient email to the same directory as project.py

-> Run the following command to run the program

   - python project.py

# # Project overview

-> Create a project that mimicks an automated mailing list.

-> The project should run from the command line interface

-> The program expects two command line inouts: 

    - The first one should be the project to run eg. project.py
    
    - The second one should be the name of the text file (.txt) containing user the email addresses
    
-> If only one command line argument is provided, ask user to enter the name of the text file

-> Read the email addresses from the text file, validate each email and send an email to each of the address

-> While sending the email, we need to do the following:

    - Create the email content,  includes the:
    
        - The sender's email address
        
        - The recipient email address
        
        - Title of the email
        
        - Content of the email (both plain and html formats)
    
# #    add_attachment.py
-> Write python script to send email with attachment

-> sends both a pdf and image as attachments to your email

