## Simple mailer code I had used to automate sending bulk emails to my peers

* Open terminal and ensure it is in the directory of this folder.
* When you run this code with python you should run it in this directory
* Open the mailer.py code and change the content to your liking. 
* Keep the header of csv file or any other extra content leaving one column of emails and one column of the corresponding links. column 0 and 1 respectively. Ive put an example csv file for your reference. If you have many more columns of other data, you need to change the column numbers in the code accordingly. Ive put a comment where you can change this. Ignore the first line of the output 
* Change the login adress and password in the code to the one of PESU IO's mailing credentials. Ive put comments accordingly.
* Login to the pesu io id from which youll be sending mails and click on this link and turn on allow less secure apps
https://myaccount.google.com/lesssecureapps
* Now you can run the  code from terminal by
 
      python mailer.py

* report.txt is a text file that will have all email adresses to which the emails were sucessfully sent to
* You can use my example csv in this folder change my address to yours and run the python mailer to test it
