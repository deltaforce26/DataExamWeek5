from flask import Flask
from repository.csv_repository import init_crashes_db

app = Flask(__name__)


with app.app_context():
    init_crashes_db('data/Traffic_Crashes_-_Crashes - 20k rows.csv')



if __name__ == '__main__':
    app.run()
