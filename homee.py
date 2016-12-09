import logging
import urllib2
from random import randint

from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)
homee_id = 'XXXXXX'
webhook_key = 'XXXXXX'

@ask.launch
def launched():
    return question('Willkommen in deinem intelligenten Haus')

@ask.intent('startHaus')
def homeegramm(homeegramm):
    homeegramm_url = 'https://{}.hom.ee/api/v2/webhook_trigger?webhooks_key={}&event={}'.format(homee_id, webhook_key, homeegramm.lower())
    response = urllib2.urlopen(homeegramm_url)
    print(homeegramm_url)
    print(response.getcode())
    return statement(homeegramm + 'gestartet').simple_card(card_title, fact_text)


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Bye")

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Bye")


if __name__ == '__main__':
    app.run(debug=True)
