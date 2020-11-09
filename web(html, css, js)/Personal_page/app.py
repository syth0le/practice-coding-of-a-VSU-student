from flask import Flask, render_template, url_for

application = Flask(__name__)
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@application.route('/')
@application.route('/home')
def show_hello_page():
    return render_template('index.html')


if __name__ == "__main__":
    # application.run(host='0.0.0.0', debug=False)
    application.run(debug=True)
