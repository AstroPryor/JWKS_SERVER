This is a project for my foundations of cybersecurity class. The requirements were to create a simple restful jwks server. 
I decided to do the project in Python as I don't have that much experience in it. 
The server will generate RSA key pairs, manage key expiration and ensure only the unpaired keys are available in the server.

To run this project, you need to have Python 3.anything, flask, pyjwt and Cryptography installed along with unittest and coverage. 
From there, copy the repository and create and activate a virtual mahine.
The server will then run on the local host 8080 and you can interact with it using curl.

app.py is the main entry point for the flask server and also creates the JWT's, implements the jwks endpoints and is responsible for the key generation, storage, and expiration. 
test_app.py shows the results of unit testing to see if each part of the code is working as it should

The steps to run this project are: 
1. install python
2. clone the repository
3. set up the virtual environment using
python -m venv venv
4. activate the virtual environment
venv\Scripts\activate
5. install all dependencies: flask, PyJWT, cryptography, requests
6. Run flask
python app.py
7. Access the JWKS endpoint and authenticate them as well
curl http://127.0.0.1:8080/.well-known/jwks.json
curl -X POST http://127.0.0.1:8080/auth
8. you can also run tests
python -m unittest test_app.py
9. and also run test_app.py
