# Flask ke functions import kar rahe hain
from flask import Flask, render_template, request, redirect

# Backend ko request bhejne ke liye
import requests

app = Flask(__name__)

# Backend ka address
BACKEND_URL = 'http://127.0.0.1:9000'


# Home page
@app.route('/')
def home():

    # index.html open hoga
    return render_template('index.html')


# Form submit hone par ye route chalega
@app.route('/submit', methods=['POST'])
def submit():

    # Form ka data dictionary me convert kar rahe hain
    form_data = dict(request.form)

    try:

        # Backend ko POST request bhej rahe hain
        response = requests.post(
            BACKEND_URL + '/submit',
            data=form_data
        )

        # Backend se aaya response json me convert kar rahe hain
        data = response.json()

        # Agar success mila
        if data['status'] == 'success':

            # Dusre page par redirect kar denge
            return redirect('/success')

        else:

            # Error ko same page par dikhayenge
            return render_template(
                'index.html',
                error=data['message']
            )

    except Exception as e:

        # Agar backend band ho ya koi aur error ho
        return render_template(
            'index.html',
            error=str(e)
        )


# Success page
@app.route('/success')
def success():

    # success.html page open hoga
    return render_template('success.html')


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8000,debug=True)