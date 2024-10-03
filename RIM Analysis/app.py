from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Step 1: Load the CSV file
file_path = 'Year-to-date.csv'  # Replace with the correct path if needed
data = pd.read_csv(file_path)

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/data')
def get_data():
    # Convert DataFrame to a list of dictionaries
    data_dict = data.to_dict(orient='records')
    return jsonify(data_dict)

if __name__ == '__main__':
    app.run(debug=True)
