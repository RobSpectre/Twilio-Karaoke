import flask
from twilio import twiml
from twilio.util import TwilioCapability
import os

app = flask.Flask(__name__)

@app.route('/karaoke', methods=['POST'])
def karaoke():
    response = twiml.Response()
    with response.dial() as dial:
        dial.conference("PennApps Karaoke Party Extravamagasma")
    return str(response)

@app.route('/mic')
def mic():
    capability = TwilioCapability(os.environ.get('ACCOUNT_SID'),
            os.environ.get('AUTH_TOKEN'))
    capability.allow_client_outgoing('AP94f2131e91ec4482b835d6d81fac732f')
    token = capability.generate()
    return flask.render_template('client.html', token=token)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
