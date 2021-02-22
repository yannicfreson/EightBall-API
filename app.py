from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)

quotes = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

class Quote(Resource):

    def get(self):
        return quotes[random.randrange(len(quotes))], 200

api.add_resource(Quote, "/eightball", "/eightball/")

if __name__ == '__main__':
    app.run()
