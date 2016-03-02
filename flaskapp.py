from flask import Flask
app = Flask(__name__)


from pymongo import MongoClient

connection = MongoClient()


@app.route("/")
def hello():
	
        return connection.essa.users.find({}).next()['name']

#update master

@app.route('/halla/<username>')
def hi(username):
	return "Halla " + username

@app.route('/add/<int:x>/<int:y>/')
def sum(x,y):
	return str( x+y)

@app.route('/test')
def test():
	return "test"
	
	
app.debug = True

if __name__ == "__main__":
        app.run("0.0.0.0")



