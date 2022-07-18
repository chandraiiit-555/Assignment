# Purnachandra Assignment

Question 1: Write a code to add the mailing feature in the Flask Application?

* pip install Flask
* pip install Flask-Mail

* Google disabled the less secure app access (https://myaccount.google.com/lesssecureapps) to we can't test the mail feature with smtp.gmail.com

  Please setup another smtp server like https://mailtrap.io/ for testing purpose and update MAIL_USERNAME & MAIL_PASSWORD in task1.py
  
* open command prompt and run task1.py using python task1.py

* Please check logs in command prompt & open http://127.0.0.1:5000 in browser to check the message.

* Please check task1.png & task11.png for more information.


  
Question 2: What is OpenCV? Give some examples of OpenCV usage.
  * pip install pip install opencv-python

  * Download task2.py & no_such_column_issue.png in same folder.
  * Run python task2.py to see the results.
  * Added openCV description in task2.py, please check it.

Question 3: What is pandas? Write down a code to join two dataframes.

* pip install pandas

* Download task3.py and run the file using python task3.py command to see the results.
* Please check task3.py docstring for pandas description.

Question 4: Write python code to establish connection with any database (SQL/MongoDB).

* pip install mysql-connector-python
* Update database host name, username, password in task4.py
* run the task4.py using python task4.py to see the results.


Question 5: Create a simple POST API in python using any python framework of your choice (Django/Flask), which can do following:

* pip install django
* pip install djangorestframework
* django-admin startproject task5
* cd task5
* django-admin startapp task
* cd ..
* python manage.py migrate
* python manage.py createsuperuser --email someone@shorewise.com --username admin
* Download task5 folder from the repo.
* copy & paste task5/urls.py
* Copy & past task/views.py
* Run python manage.py runserver command in command prompt.
* Check command prompt logs and paste http://127.0.0.1:8000/task5 in the browser.
* paste the below json object in the content of post request 
* {
"name":"testing",
"date_of_birth":"05/02/1990",
"country":"India"
}

* Hit POST button to see the API response.
* Please check task5.xlsx for tested results ( shared the file for referrance )
