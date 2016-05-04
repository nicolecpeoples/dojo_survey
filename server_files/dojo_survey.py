from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods =['POST'])
def get_info():
	#to access the data the user inputs into the fields we use request.form['name of input']
	
	#redirects bck to the '/' route
	return render_template('result.html',
	name = request.form['full_name'],
	location = request.form['location'],
	language= request.form['language_preference'],
	comments = request.form['comments'])

app.run(debug=True) #run our server
