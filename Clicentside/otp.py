# Import the necessary modules
from flask import Flask, render_template, request, session
from twilio.rest import Client
import random
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Configure the secret key for the Flask app
app.secret_key = 'your_secret_key'  # replace with your own secret key

# Configure the Twilio account SID and auth token
account_sid = 'ACe31aa8022e67a9986a9334ce929602f1'
auth_token = '7b45f7e8cf7034f16f7777df4346be0a'
twilio_phone_number = '+16073501494'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Render the index page


@app.route('/')
def index():
    return render_template('index.html')


# Send OTP


@app.route('/send-otp', methods=['POST'])
def send_otp():
    # Get the phone number from the POST request
    phone_number = request.form['phone_number']

    # Generate a random 6-digit OTP
    otp = random.randint(100000, 999999)

    # Store the OTP in the session
    session['otp'] = str(otp)

    # Send the OTP via SMS using Twilio
    message = client.messages.create(
        to=phone_number,
        from_=twilio_phone_number,
        body=f'Your OTP is {otp}.'
    )

    return 'OK'

# Verify OTP


@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    # Get the OTP from the POST request
    otp = request.form['otp']

    # Check if the OTP is valid
    if otp == session['otp']:
        # Clear the OTP from the session
        session.pop('otp', None)
        return 'OK'
    else:
        return 'Invalid OTP'


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)


# INBD01716472
