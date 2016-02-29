from flask import Flask
app = Flask(__name__)


from pymongo import MongoClient

connection = MongoClient()


@app.route("/")
def hello():
	
        return connection.essa.users.find({}).next()['name']


@app.route('/<username>')
def hi(username):
	return "Halla " + username

app.debug = True

if __name__ == "__main__":
        app.run("0.0.0.0")



