from flask import Flask, render_template

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='rahasya',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('WP_SETTINGS', silent=True)

@app.route('/')
def checkWord():
	return render_template('index.html')