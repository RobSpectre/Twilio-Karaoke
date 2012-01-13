import flask
from twilio import twiml
from twilio.util import TwilioCapability
import os

app = flask.Flask(__name__)

@app.route('/karaoke')
def karaoke():
    response = twiml.Response()
    with response.dial() as dial:
        dial.conference('PennApps Karaoke Party')
    return str(response)

@app.route('/mic')
def mic():
    capability = TwilioCapability(os.environ.get('ACCOUNT_SID'),
            os.environ.get('AUTH_TOKEN'))
    capability.allow_client_outgoing(os.environ.get('SPEAKER_CALLER_ID'))
    token = capability.generate()
    return flask.render_template('client.html', token=token, name='Microphone')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    if port == 5000:
        app.debug = True
    app.run(host='0.0.0.0', port=port)
