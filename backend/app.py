# Flask import kar rahe hain
from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()
import os

# MongoDB ke liye pymongo
import pymongo

# Flask app bana rahe hain
app = Flask(__name__)

# MongoDB Atlas se connect kar rahe hain
MONGO_URI =os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)

# Database select kar rahe hain or collection set krrhe hai
db = client.pythos
collection = db['pythform']



# Ye API frontend se data receive karegi
@app.route('/submit', methods=['POST'])
def submit():

    try:

        # Frontend se aaya hua form data dictionary me convert kar rahe hain
        form_data = dict(request.form)

        # MongoDB Atlas me data insert kar rahe hain
        collection.insert_one(form_data)

        # Success response bhej rahe hain
        return {
            "status": "success"
        }

    except Exception as e:

        # Agar error aaya to error message bhejenge
        return {
            "status": "error",
            "message": str(e)
        }


if __name__ == '__main__':
    app.run(port=9000, debug=True)