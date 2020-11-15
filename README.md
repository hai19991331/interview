# Interview
# Install requirements 
  ```
  sudo apt-get -y install mysql-server
  apt-get install python-dev libmysqlclient-dev
  pip install MySQL-python
  pip install -r requirements.txt
  ```
# Changing database.cnf

  ```
  {
    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "Hoanhai123",
        "database": "interview"
    },
    "database_type": "mysql"
}
  
  ```
# Run 
```
python server.py

```
