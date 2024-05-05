Steps to Setup, Build, and Run the Application

   1 Install Python 3.x if not already installed.

   2 Install required Python packages using pip:

   3 Set up a database. In this example, we're using SQLite. You can change the database type as per your preference by modifying the create_engine function call in app.py.

   4 Run the app.py file:

   5 Your API server will start running on http://localhost:5000 by default.
   
   6 Use postman to authenticate requests. 
        In this example, I've used a simple simple token-based authentication.

        Here's how it works:

            a.  Client: Sends a request to the server with an Authorization header containing a token.
            b.  Server: Receives the request and extracts the token from the Authorization header.
            c.  Server: Validates the token against a predefined value (in this case, 'your_auth_token').
            d.  Server: If the token is valid, the request is allowed to proceed; otherwise, the server returns a 401 Unauthorized response.


API Usage
    Uploading a File:

        To upload a file, send a POST request to /upload endpoint with the file attached as form-data. Also you need to authenticate for this request 
        Example using curl:
            curl -X POST -F "file=@/path/to/your/file.pdf" -H "Authorization: Bearer dummy_token" http://localhost:5000/upload

    Retrieving Files

        To retrieve uploaded files, send a GET request to /files endpoint. Also you need to authenticate for this request.
        Example using curl:
            curl -X GET -H "Authorization: Bearer dummy_token" http://localhost:5000/files