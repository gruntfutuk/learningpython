from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	session['some_var'] = 'some_value'
	return redirect(url_for('output'))

@app.route('/output')
def output():
	some_var = session.get('some_var', None)
	vars_out = []
	for var in vars:
		vars_out.append(f'{var}')
	return ', '.join(vars_out)


if __name__ == "__main__":
	app.run()

