# Twilio Karaoke

A ten-minute demo where you build a karaoke machine in front of an audience
using [Twilio](http://www.twilio.com) and [Heroku](http://www.heroku.com).

Originally given at [PennApps 2012 Spring Hackathon](http://www.pennapps.com).

## Summary

This live-coding demonstration uses [Twilio 
Client](http://www.twilio.com/api/client) , [Twilio
Voice](http://www.twilio.com/api/voice) and [Twilio
SMS](http://www.twilio.com/api/sms) to piece together a karaoke machine on 
the fly starting from nothing but a blank file.  The four components created 
are:

* Microphone (Twilio Client to a Twilio Conference)
* Speaker (Twilio Client to a Twilio Conference, muted)
* Music (Twilio Voice to a Twilio Conference)
* Lyrics (Twilio SMS iterating through text file)

## Demo Outline

- Intro
    - Who wants to sing karaoke (yay!)
    - Karaoke machine has four components
        - Microphone
        - Speaker
        - Music
        - Lyrics
    - We're going to create all of those things using Twilio
    - And we're going to do it right now.
- Microphone
    - Create TwiML application for Conference Room
        - Write route for conference room
        - Create TwiML app in Twilio Dashboard
        - Assign to phone number
    - Create microphone
        - Call number from singer's cell phone
        - Alternatively, create a Twilio Client for the Conference Room
- Speaker
    - Create another TwiML application to connect muted
        - Write route for conference room muted
        - Create TwiML app
    - Create Twilio Client for the Conference room
- Music
    - Create yet another TwiML application to play music
    - Connect TwiML application to conference by using REST API
    - Create call with REST API to karaoke conference phone number
- Lyrics
    - Search for song lyrics
    - Drop into text file
    - Create function to send text message to singer with a string
    - Iterate through file and send lyrics to singer

## Hacking

### Installation

Requires Python 2.5 or greater.

1) Clone repo:

<pre>
git clone git@github.com:RobSpectre/Twilio-Karoke.git
</pre>

2) Install dependencies:

<pre>
cd Twilio-Karoke
pip install -r requirements.txt
</pre>

3) Login to [Twilio](https://www.twilio.com/login) (or [signup for
account](https://www.twilio.com/try-twilio?g=)).

4) [Create new TwiML App](https://www.twilio.com/user/account/apps/add) for Somebody Put Something In My Ring.

5) Configure local_settings.py with your Twilio account details or use
environment variables.

<pre>
export ACCOUNT_SID='ACxxxxxxxxxxxxxxxxx'
export AUTH_TOKEN='yyyyyyyyyyyyyyyyyyyy'
export SPEAKER_APP_SID='APzzzzzzzzzzzzz'
export SPEAKER_CALLER_ID='+17778889999'
</pre>

6) Launch dev server.

<pre>
python web.py
</pre>

Note - a Procfile is included if you would prefer to use Foreman.

### Structure

* app.py - Core Flask app.
* templates/index.html - Main webpage with [Twilio Client](http://www.twilio.com/api/client) integration.
* music - Music file and lyrics for song ("Blitzkrieg Bop" lyrics included.

### Deployment

This app is currently running on [Heroku](http://www.heroku.com), but can be
deployed to any WSGI compliant hosting provider.  If it runs Python, it should
be able to run this project.


## Technologies

* [Flask](http://flask.pocoo.org/) - Python microframework.  Makes all this go.
* [Heroku](http://www.heroku.com) - Uber easy cloud hosting for Python (and lesser) apps.
* [Twilio](http://www.twilio.com), snacky. 


## Credits

* License: [Mozilla Public License](http://www.mozilla.org/MPL/)
* Author: [Rob Spectre](http://www.brooklynhacker.com)
* Powered by [Twilio](http://www.twilio.com).

## Plug

Yes, this is what I do for a living.

Want to do it too?  [We're hiring.](http://www.twilio.com/jobs)
