from flask import Flask, request
from auth import issue_jwt
from jwks import get_jwks

app = Flask(__name__)

@app.route('/jwks', methods=['GET'])
def jwks():
    return get_jwks()

@app.route('/auth', methods=['POST'])
def auth():
    expired = request.args.get('expired', 'false').lower() == 'true'
    return issue_jwt(expired=expired)

if __name__ == '__main__':
    app.run(port=8080)