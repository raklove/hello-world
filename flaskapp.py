from flask import Flask
app = Flask(__name__)


from pymongo import MongoClient

connection = MongoClient()


@app.route("/")
def hello():
	
        return connection.essa.users.find({}).next()['name']


@app.route('/halla/<username>')
def hi(username):
	return "Halla " + username

@app.route('/add/<x>/<y>')
def sum(x,y):
	return str( x+y)

app.debug = True

if __name__ == "__main__":
        app.run("0.0.0.0")



