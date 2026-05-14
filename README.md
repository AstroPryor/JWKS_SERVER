# RESTful JWKS Server

## Overview

This project was developed for my Foundations of Cybersecurity course at the University of North Texas. The goal of the project was to build a simple RESTful JSON Web Key Set (JWKS) server that generates RSA key pairs, manages key expiration, and serves valid public keys through a JWKS endpoint.

I chose to complete this project in Python to strengthen my experience with backend development, Flask, JWTs, and public key cryptography.

This is the first version of the JWKS server project. Later versions expand the project by adding SQL-backed key storage, encrypted private key storage, user registration, authentication logging, and rate limiting.

## Purpose

The purpose of this project was to:

- Build a RESTful JWKS server
- Generate RSA public/private key pairs
- Create signed JSON Web Tokens
- Serve valid public keys through a JWKS endpoint
- Handle expired keys correctly
- Practice backend security concepts using Python and Flask
- Write unit tests to verify server functionality

## Technologies Used

- Python
- Flask
- PyJWT
- Cryptography
- unittest
- coverage

## Repository Structure

```text
JWKS-Server/
├── app.py
├── test_app.py
├── Test Output.png
└── README.md
```

## File Descriptions

### `app.py`

`app.py` is the main entry point for the Flask server. It contains the main application logic for generating RSA key pairs, creating JWTs, serving public keys through the JWKS endpoint, and managing key expiration.

This file is responsible for:

- Starting the Flask web server
- Generating RSA public/private key pairs
- Creating signed JSON Web Tokens
- Returning public keys in JWKS format
- Managing key expiration
- Handling the `/auth` endpoint
- Handling the `/.well-known/jwks.json` endpoint

### `test_app.py`

`test_app.py` contains the unit tests for the project. These tests verify that the server routes, JWT generation, JWKS output, and key expiration behavior work as expected.

This file is responsible for testing:

- JWKS endpoint responses
- Authentication endpoint responses
- JWT creation
- Key availability
- Expired key handling
- Basic server functionality

### `Test Output.png`

`Test Output.png` is a screenshot showing the output from running the project tests. It provides visual proof that the unit tests were executed successfully.

## Endpoints

### JWKS Endpoint

```http
GET /.well-known/jwks.json
```

This endpoint returns the currently available public keys in JWKS format. These public keys can be used by clients to verify JWTs signed by the server.

Example request:

```bash
curl http://127.0.0.1:8080/.well-known/jwks.json
```

Expected behavior:

- Returns a JSON Web Key Set
- Includes only valid, non-expired public keys
- Does not expose private keys

### Authentication Endpoint

```http
POST /auth
```

This endpoint returns a signed JWT using one of the available RSA private keys.

Example request:

```bash
curl -X POST http://127.0.0.1:8080/auth
```

Expected behavior:

- Generates a signed JWT
- Uses an available RSA private key
- Returns the token to the client
- Supports testing of JWT signing and verification behavior

## How to Run

### 1. Install Python

Make sure Python 3.x is installed.

You can check your Python version with:

```bash
python --version
```

or:

```bash
python3 --version
```

### 2. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

Replace `<repository-url>` with the actual GitHub repository URL.

Replace `<repository-name>` with the folder name created after cloning the repository.

### 3. Create a Virtual Environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install flask pyjwt cryptography requests coverage
```

If a `requirements.txt` file is added later, dependencies can be installed with:

```bash
pip install -r requirements.txt
```

### 5. Run the Server

```bash
python app.py
```

The server runs locally at:

```text
http://127.0.0.1:8080
```

## Testing the Server Manually

### Test the JWKS Endpoint

Run:

```bash
curl http://127.0.0.1:8080/.well-known/jwks.json
```

This should return the available public keys in JWKS format.

### Test the Authentication Endpoint

Run:

```bash
curl -X POST http://127.0.0.1:8080/auth
```

This should return a signed JWT.

## Running Unit Tests

Run the unit tests with:

```bash
python -m unittest test_app.py
```

This command runs the test cases in `test_app.py` and verifies that the main parts of the server are functioning correctly.

## Running Tests with Coverage

To run the tests with coverage tracking:

```bash
coverage run -m unittest test_app.py
coverage report
```

This shows how much of the project code is covered by the unit tests.

## Test Output

The repository includes a screenshot of the test output:

```text
Test Output.png
```

The image shows the results of running the unit tests for the project.

If the image does not display correctly on GitHub because of the space in the file name, rename it to:

```text
test-output.png
```

Then update the image link to:

```markdown
![Unit Test Output](test-output.png)
```

Current image link:

```markdown
![Unit Test Output](Test%20Output.png)
```

![Unit Test Output](Test%20Output.png)

## What I Learned

Through this project, I gained hands-on experience with:

- Building a RESTful API with Flask
- Generating RSA public/private key pairs
- Creating and signing JSON Web Tokens
- Understanding JSON Web Key Sets
- Formatting public keys for JWKS responses
- Managing key expiration
- Testing backend security functionality
- Writing Python unit tests
- Measuring test coverage
- Understanding how authentication systems expose public keys for token verification

This project helped me better understand how JWT-based authentication systems use asymmetric cryptography and public key discovery to support secure token validation.

## Related Versions

This repository is the base version of the JWKS server project.

Later versions of this project expand the functionality by adding more realistic security features, including:

- SQL-backed key storage
- AES-encrypted private key storage
- User registration
- Authentication logging
- Rate limiting
- Additional testing and coverage requirements

These later versions build on the same core idea of generating RSA keys, signing JWTs, and exposing valid public keys through a JWKS endpoint.

## Disclaimer

This project was created for educational purposes as part of a cybersecurity course. It is intended to demonstrate JWKS, JWT, RSA key handling, key expiration, and basic REST API security concepts in a controlled local environment.

This project is not intended for production use without additional security hardening, configuration management, access control, and secure key storage.
