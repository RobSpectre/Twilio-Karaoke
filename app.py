import flask
from twilio import twiml
import os

app = flask.Flask(__name__)

@app.route('/karaoke')
def karaoke():
    response = twiml.Response()
    with response.dial() as dial:
        dial.conference("Penn Apps Karaoke Party")
    return str(response)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
