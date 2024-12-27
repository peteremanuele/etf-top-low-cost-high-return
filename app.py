from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Read the CSV file into a DataFrame
    csv_file_path = "./../data/input.csv"
    df = pd.read_csv(csv_file_path)
    
    # Convert DataFrame to list of dictionaries for Handsontable
    data = df.to_dict(orient='records')
    columns = [{'data': col, 'title': col} for col in df.columns]
    
    return render_template('index.html', data=data, columns=columns)

if __name__ == '__main__':
    app.run(debug=True)
