## Flask Mini Project

### Set Up
``cd flask_mini``
### Create Virtualenv with name venv (Linux/Windows)
``python -m venv venv``
#### Activate Virtualenv
#### Linux
``source venv/bin/activate``
#### Windows
``venv\Scripts\activate``
### Install dependency
``pip install -r requirements.txt``

### Run Project
``flask run``
#### Create Migration
``flask db migrate``

#### Apply Migration
``flask db upgrade``

### Run Test Case
``python test.py``
