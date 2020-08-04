from flask import Flask
import datetime

app = Flask(__name__)  #import_name='messanger'


@app.route("/")
def hello():
    return """Building messanger 
    
    <a href='/status'>Status</a>"""


@app.route("/status")
def status():
    return {
        "status": True,
        "Name": "Mesenger",
		"Time3": datetime.datetime.utcnow()
    }


if __name__ == "__main__":
    app.run()
