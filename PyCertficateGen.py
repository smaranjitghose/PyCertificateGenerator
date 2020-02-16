import cv2  # This module is used to put the text over the image
import csv  # This module is used to open the csv file
import os  # This module is used to access the system parameters
import smtplib  # This module is defines an SMTP client session object that can be used to send mail
import imghdr  # This module determines the type of image contained in a file
# This module is used to create the Email_object
from email.message import EmailMessage

# path of the image
path = r'C:\Users\Dell\Desktop\PYCertGen\template.jpg'
# font
font = cv2.FONT_HERSHEY_SIMPLEX
# Reading an image in default mode
image = cv2.imread(path)
# org
org = (300, 50)
# fontScale
fontScale = 1
# Blue color in BGR
color = (0, 0, 0)
# Line thickness of 2 px
thickness = 2

#List of names of the images generated
image_files = []
cert_count = 0

Email_id = os.environ.get('EMAIL_ID')  # Sender's email address obtained
Email_password = os.environ.get('EMAIL_PASSWORD')  # Sender's password

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Email_id, Email_password)  # Authentication
    #Open the csv file containing the name and email address of the participants
    with open('cfp.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            generate_cert(row[0])
            send_email(row[1])

    def generate_cert(name):
        '''
        Function to take in the the name of the candidate as input and generate a certificate as output
        '''
        image_name = name + ".jpg"
        image_new = cv2.putText(image, name, org, font,
                                fontScale, color, thickness, cv2.LINE_AA)

        cv2.imwrite(image_name, image_new)
        cert_count += 1
        image_files.append(image_name)

    def send_email(reciever_email_id):
        '''
        This function is used to craft the email and send it
        '''
        #Craft the email
        msg = EmailMessage()  # Creating an email object
        msg['Subject'] = 'Global CFP Day Certificate'  # Subject of the message
        msg['From'] = Email_id  # Sender's email address
        msg['To'] = receiver_email_id  # Receiver's email address
        msg.set_content(
            'Hey! Thanks for attending Global CFP Day. Here is an attachment of your certificate.')

        file = image_files[cert_count]  # Open the current certificate
        # Make sure either the images/pdfs are in the same directory or the entire path is specified
        with open(file, 'rb') as f:
            file_data = f.read()
            #Not required if we are sending pdfs
            # used to determine the type of image
            file_type = imghdr.what(f.name)
            file_name = f.name
        #Add the attachment to the message
        msg.add_attachment(file_data, maintype='image',
                           subtype=file_type, filename=file_name)
        smtp.send_message(msg)  # Send the message
