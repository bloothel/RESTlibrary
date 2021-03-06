from flask import Flask
from flask_restful import Api
from routs import getBook

application = Flask(__name__)
api = Api(application)

api.add_resource(getBook, '/api/books/<int:bookID>')


if __name__ == "__main__":
    application.debug = True
    application.run()
