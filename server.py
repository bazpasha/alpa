from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html');

from flask import request, json
@app.route('/task', methods=['GET'])
def task():
	return json.dumps({'task': 'необходимость', 'formal': 'necessity', 'informal': 'need'});
	
if __name__ == "__main__":
	app.run()