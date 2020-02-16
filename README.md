# PyCertificateGenerator 🏆🖨
A script that reads the data from a csv file and spits certificates while sending them via email on the go!

## Usage:

- If you have an ```.xlsx``` file, First convert it to a ```.csv``` file using my [PyCSVConverter](https://github.com/smaranjitghose/PyCSVConverter) script
- Open the ```PyCertficateGen.py``` script and do the following:
  - Specify the path of the template image to be used
  - Set the path of the csv file to be used
  - Set the ```font``` you want to the type of font you want to use
  - Set the ```org``` to the coordinates of the bottom-left corner of the text string in the image
  - Set the ```fontScale``` that is multiplied by the font-specific base size
  - Set the ```color``` of the text string to be drawn in BGR.. say (255, 0, 0) is for Blue
  - Set the ```thickness``` of the line in px
  - Set ```Email_id``` to the your email address
  - Set ```Email_password``` to the password of your aforementioned email address
  
    Its a nice practice to have them saved as Environment variables in the system but not mandatory
  
  - Set ```msg['Subject']``` to the Subject of your Email
  - Set ```msg.set_content=()``` to the body of your Email.(You even use an HTML format for this)
- Run the script.
- Now sit back and Relax.🍹 Let Python Hustle 💪

(In case you need some pointers on the part of the code to send the emails. Check out my [PyMailer](https://github.com/smaranjitghose/PyMailer) repo
  
## Suggestions: ⚠
- Make sure you use a ```.csv``` file
- Make sure the ```.csv```file does'nt have any labels for the values 
- Don't have any script saved as ```email.py```
- Make sure your Google Account has [Allow Less Secure App Access](https://myaccount.google.com/lesssecureapps) enabled
- At times setting up the SSL might fall into timeout. Don't panic. Just reconnect or connect to a new network and retry
- If SSL is still timed out and its urgent, simply use TTL for connection (Instructions given at the end of the script)
