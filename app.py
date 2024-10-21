from flask import Flask, render_template, request, jsonify
import random
import csv

app = Flask(__name__)

# Function to read quotes from CSV
def read_quotes_from_csv():
    quotes = []
    with open('quotes.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            if row:  # Only add non-empty rows
                quotes.append(row[0])
    return quotes

# Function to get a random quote
def get_random_quote():
    quotes = read_quotes_from_csv()
    return random.choice(quotes) if quotes else "No quotes available."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_quote', methods=['POST'])
def generate_quote():
    quote = get_random_quote()
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(debug=True)
