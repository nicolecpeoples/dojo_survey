from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "thisismysecretkey"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods =['POST'])
def get_info():
	#to access the data the user inputs into the fields we use request.form['name of input']
	
	if len(request.form['full_name']) < 1:
		flash("Please fill in your full name")
		return redirect('/')
	if len(request.form['comments']) < 1:
		flash("We would like to know more about what you think")
		return redirect('/')
	if len(request.form['comments'])  > 120:
		flash("Your comment cannot be longer than 120 characters")
		return redirect('/')

	else: 
		flash('')

	#redirects bck to the '/' route
	return render_template('result.html',
	name = request.form['full_name'],
	location = request.form['location'],
	language= request.form['language_preference'],
	comments = request.form['comments'])

@app.route('/set_cookie')
def cookie_insertion():
    redirect_to_index = redirect('/index')
    response = current_app.make_response(redirect_to_index )  
    response.set_cookie('cookie_name',value='values')
    return response


app.run(debug=True) #run our server
