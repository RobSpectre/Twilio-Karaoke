import flask
from twilio import twiml
from twilio.util import TwilioCapability
import os

app = flask.Flask(__name__)

@app.route('/karaoke', methods=['POST'])
def karaoke():
    response = twiml.Response()
    with response.dial() as dial:
        dial.conference("Penn Apps Karaoke Extravamagasma")
    return str(response)

@app.route('/mic')
def mic():
    capability = TwilioCapability(os.environ.get('ACCOUNT_SID'),
            os.environ.get('AUTH_TOKEN'))
    capability.allow_client_outgoing('APc0af6dfc68494a3b82547842c9fb2f2b')
    token = capability.generate()
    return flask.render_template('client.html', token=token)

@app.route('/muted', methods=['POST'])
def muted():
    response = twiml.Response()
    with response.dial() as dial:
        dial.conference("Penn Apps Karaoke Extravamagasma", muted=True)
    return str(response)

@app.route('/speaker')
def speaker():
    capability = TwilioCapability(os.environ.get('ACCOUNT_SID'),
            os.environ.get('AUTH_TOKEN'))
    capability.allow_client_outgoing(os.environ.get('SPEAKER_APP_SID'))
    token = capability.generate()
    return flask.render_template('client.html', token=token)

@app.route('/tunes')
def tunes()
    response = twiml.Response()
    response.play("http://demo.brooklynhacker.com/music/ramones.mp3")
    return str(response)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
