from flask import Flask

app = Flask("__name__")

@app.route("/<name>")
def HelloWorldFlask(name):
	return ('Hello, {}'.format(name))

app.run(port=5555)