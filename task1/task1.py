
# importing libraries
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class

"""

Google disabled the less secure app access (https://myaccount.google.com/lesssecureapps) 
so we can't test the mail feature with smtp.gmail.com

Please setup another smtp server like smtp.mailtrap.io and setup username a& password.

All SMTP values should be read from CFG files but directly added here for testing purpose.

"""
# configuration of mail

app.config['MAIL_SERVER']= 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'f158232b63c94d'
app.config['MAIL_PASSWORD'] = '318acd54f82957'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
    msg = Message(
                    'Hello, Shorewise',
                    sender ='chandraiiit172@gmail.com',
                    recipients = ['tatikondapurna@gmail.com']
                )
    msg.body = 'Hello Shorewise team, sending you mail from Chandra Tanikonda'
    mail.send(msg)
    return 'Mail Sent'

if __name__ == '__main__':
    app.run(debug = True)
