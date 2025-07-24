from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(f"New Contact from {name}",
                  sender=email,
                  recipients=['your_email@gmail.com'])
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    try:
        mail.send(msg)
        flash("Message sent successfully!", "success")
    except Exception as e:
        flash("Failed to send message. Try again later.", "danger")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
