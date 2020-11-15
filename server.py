from flask import Flask, render_template, request
import sys 
import requests 
import json

from tools.is_even import is_even
from database_handler.database.base_database import DatabaseFactory 
app = Flask(__name__)

DATABASE_CONFIG_FILE = "./config/database.cnf"
try:
    with open(DATABASE_CONFIG_FILE) as f:
        config = json.load(f)
except IOError as err:
    print("Cannot open configuration: %s. Exiting" % (str(err)))
    sys.exit(1)
    
db_cls = DatabaseFactory.get_database(config.get('database_type'))
a={
            'database': config.get('database').get('database'),
            'host': config.get('database').get('host'),
            'user': config.get('database').get('user'),
            'password': config.get('database').get('password')
        }
db_handler = db_cls(**a)
db_handler.setup()

# View
@app.route('/', methods=['GET', 'POST'])
def index():
    payload = {}
    headers= {}
    #get url
    url = 'http://data.fixer.io/api/latest?access_key=fe3a9b3f9ac173a3e51d8ea22951cf95'
    response = requests.request("GET", url, headers=headers, data = payload)
    
    answer = json.loads(response.text.encode('utf8'))
    edited_values = [(value,answer['rates'][value]+10.0002) if is_even(answer['rates'][value]+10.0002) == False else (value,answer['rates'][value]+10.0002,'r') for value in answer['rates']]
    insert_values = [(value,answer['rates'][value]+10.0002) for value in answer['rates']]
    db_handler.insert_value(insert_values)
    return render_template("index.html",value=edited_values)

if __name__ == '__main__':
    app.run(debug=False)