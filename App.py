from flask import Flask, render_template
from google import genai
from dotenv import load_dotenv
import os

app = Flask(__name__)


load_dotenv()
key = os.getenv('api_key')
client = genai.Client(api_key=key)

def askGenai(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text

@app.route("/")
def hello_world():
    return askGenai("Explain how AI works in one paragraph")
    
@app.route("/split")
def split():
    return 0

@app.route("/test")
def test():
    my_file = client.files.upload(file="C:/Users/syah/Documents/GitHub/Mentri-Berbudaya/test.jpg")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[my_file, "create a json string."],
    )
    return response.text

if __name__ == "__main__":
    app.run()