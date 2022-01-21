from flask import Flask, render_template
from flask_restful import Api
from resources.Hotel import Hotels


app = Flask(__name__)
api = Api(app)

api.add_resource(Hotels, '/hotels')


@app.route('/')
def home():
    return render_template('pages/home.html')


if __name__ == '__main__':
    app.run(debug=True)
