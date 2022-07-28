## Authentication challenge
## Steps to run the program.

### 1. Clone the repository to local machine using command
```git clone https://github.com/durgeksh/authchallenge.git```

### 2. Open terminal and enter into autochallenge directory using command cd

### 3. Create a virtual environment using command
```pipenv shell```

### 4. Install the required packages using the command
```pipenv install -r requirements.txt```

### 5. Start the local server using the command
```python3 manage.py runserver```

### 6. Open the link http://127.0.0.1:8000/
You will get authentication error as user is yet to be authenticated

### 7. Open the link http://127.0.0.1:8000/api/token/
Enter user as "demo" and password as "Demo@12345". This command will generate the api token which can be used for further requests. COpy the access token.

### 8. Install an extension ThunderClient in VS Code.
select a GET request on http://127.0.0.1:8000/ and go to Auth->Bearer and paste the access token and click send. It should display the welcome message.







## Scope
#### 1. For testing purpose sqlite db is included within the git repository
#### 2. Secret key and DB credentials can be kept separately in a file and excluded in git respository commit for security purpose
