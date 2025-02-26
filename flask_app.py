from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# Configure database connection (Azure SQL, PostgreSQL, etc.)
DATABASE_URL = "your_database_connection_string"
engine = create_engine(DATABASE_URL)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    df = pd.read_csv(file)
    df.to_sql('Transactions', con=engine, if_exists='append', index=False)
    return "File uploaded successfully"

if __name__ == '__main__':
    app.run(debug=True)
