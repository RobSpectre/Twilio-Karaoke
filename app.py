import flask
from twilio import twiml
import os

app = flask.Flask(__name__)

@app.route('/karaoke')
def karaoke():
    response = twiml.Response()
    with response.dial() as dial:
        dial.conference('PennApps Karaoke Party')
    return str(response)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
