from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/terms-of-use')
def terms_of_use():
    return 'Terms of Use'

@app.route('/privacy-policy')
def privacy_policy():
    return 'Privacy Policy'

# The below lines are not used for production in App Engine
if __name__ == '__main__':
     app.run(host='127.0.0.1', port=8080, debug=True)
