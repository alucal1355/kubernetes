from flask import Flask
app = Flask(__name__)
default_name = 'Víctor Ponz'
@app.route('/')
def get_identicon():
	name = default_name
	header = '<html><head><title>Identidock</title></head><body>'
	body = '''<form method="POST">
			Hola <input type="text" name="name" value="{}">
			<input type="submit" value="submit">
			</form>
			<p>Te pareces a:
			<img src="/monster/monster.png"/>
			'''.format(name)
	footer = '</body></html>'
	return header + body + footer
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')