import flask
from twilio import twiml
from twilio.util import TwilioCapability
import os

app = flask.Flask(__name__)

@app.route('/karaoke', methods=['GET', 'POST'])
def karaoke():
    response = twiml.Response()
    with response.dial() as dial:
        dial.conference("PennApps Karaoke Party Room")
    return str(response)

@app.route('/mic')
def mic():
    capability = TwilioCapability(os.environ.get('ACCOUNT_SID'), 
            os.environ.get('AUTH_TOKEN'))
    capability.allow_client_outgoing('AP2b4a0d70f02c4088b92f064607a95025')
    token = capability.generate()
    return flask.render_template('client.html', token=token)

@app.route('/muted', methods=['GET', 'POST'])
def muted():
    response = twiml.Response()
    with response.dial() as dial:
        dial.conference("PennApps Karaoke Party Room", muted=True)
    return str(response)

@app.route('/speaker')
    capability = TwilioCapability(os.environ.get('ACCOUNT_SID'), 
            os.environ.get('AUTH_TOKEN'))
    capability.allow_client_outgoing(os.environ.get('SPEAKER_APP_SID'))
    token = capability.generate()
    return flask.render_template('client.html', token=token)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
