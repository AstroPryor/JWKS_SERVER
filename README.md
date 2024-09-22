This is a project for my foundations of cybersecurity class. The requirements were to create a simple restful jwks server. 
I decided to do the project in python as I don't have that much experience in it. 
The server will generate RSA key pairds, manage key expiration and endure only the unpaired keys are availiable in the server.

To run this project, you need to have python 3.anything, flask, pyjwt and cryptogography installed
From there, copy the repository and create and activate a virtual mahine.
The server will then run on the local host 8080 and you can interact with it using curl.

app.py is the main entry point for the flask server
auth.py creates and issues JWT's 
jwks.py implements the jwks endpoint
jey_manage.py is responsible for key generation, storage and expiration
