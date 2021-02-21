from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)

quotes = [
    {
        "id": 0,
        "author": "Marilyn Monroe ",
        "quote": "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best." 
    },
    {
        "id": 1,
        "author": "Oscar Wilde ",
        "quote": "Be yourself; everyone else is already taken."
    },
    {
        "id": 2,
        "author": "Albert Einstein ",
        "quote": "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
    },
    {
        "id": 3,
        "author": "Bernard M. Baruch",
        "quote": "Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind."

    },
    {
        "id": 4,
        "author": "Mahatma Gandhi",
        "quote": "Be the change that you wish to see in the world."
    },
    {
        "id": 5,
        "author": "Marilyn Monroe",
        "quote": "Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring."
    },
    {
        "id": 6,
        "author": "Oscar Wilde",
        "quote": "We are all in the gutter, but some of us are looking at the stars."
    },
    {
        "id": 7,
        "author": "Robert Louis Stevenson",
        "quote": "Don't judge each day by the harvest you reap but by the seeds that you plant."
    },
    {
        "id": 8,
        "author": "Will Smith",
        "quote": "Money and success don’t change people; they merely amplify what is already there."
    },
    {
        "id": 9,
        "author": "Mark Twain",
        "quote": "Good friends, good books, and a sleepy conscience: this is the ideal life."
    }
]

class Quote(Resource):

    def get(self, id=0):
        if id == 0:
            return random.choice(quotes), 200

        for quote in quotes:
            if(quote["id"] == id):
                return quote, 200
        return "Quote not found", 404

    def post(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("author")
      parser.add_argument("quote")
      params = parser.parse_args()

      for quote in quotes:
          if(id == quote["id"]):
              return f"Quote with id {id} already exists", 400

      quote = {
          "id": int(id),
          "author": params["author"],
          "quote": params["quote"]
      }

      quotes.append(quote)
      return quote, 201

api.add_resource(Quote, "/quotes", "/quotes/", "/quotes/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)