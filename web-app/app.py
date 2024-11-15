from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import sqlite3
import requests
import base64
import sqlite3
import os

app = Flask(__name__)

def get_db_connect():
    conn = sqlite3.connect('flight_database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        return redirect(url_for('result', user_input=user_input))
    return render_template('index.html')

@app.route('/result')
def result():
    user_input = request.args.get('user_input', '')
    return f'<h1>Content saved: {user_input}</h1>'

@app.route('/api-request', methods=['GET', 'POST'])
def api_request():
    if request.method == 'POST':
        API_KEY = os.getenv('API_KEY')

        headers = {
            "Content-Type": "application/json",
            "api-key": API_KEY,
        }
        payload = {
          "messages": [
                {
                "role": "system",
                "content": [
                    {
                    "type": "text",
                    "text": "You are an AI model trained to generate SQL queries based on a given database schema."
                    }
                ]
                },
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": "find travel arrangements for a round trip flight from dallas to pittsburgh"
                    }
                ]
                },
                {
                "role": "assistant",
                "content": [
                    {
                    "type": "text",
                    "text": "SELECT DISTINCT flight_1.flight_id FROM flight flight_1 , airport_service airport_service_1 , city city_1 , airport_service airport_service_2 , city city_2 , flight_fare flight_fare_1 , fare fare_1 WHERE flight_1.from_airport = airport_service_1.airport_code AND airport_service_1.city_code = city_1.city_code AND city_1.city_name = 'DALLAS' AND( flight_1.to_airport = airport_service_2.airport_code AND airport_service_2.city_code = city_2.city_code AND city_2.city_name = 'PITTSBURGH' AND flight_1.flight_id = flight_fare_1.flight_id AND flight_fare_1.fare_id = fare_1.fare_id AND fare_1.round_trip_cost IS NOT NULL AND 1 = 1 )"
                    }
                ]
                }
            ],
          "temperature": 0.7,
          "top_p": 0.95,
          "max_tokens": 800
        }
        ENDPOINT = "https://sqlifibot.openai.azure.com/openai/deployments/gpt-4o-2024-08-06-ft-ba883aa5709f4c709cad7309c9f296d5/chat/completions?api-version=2024-02-15-preview"

        try:
            response = requests.post(ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()  # Checks for HTTP errors
            response_data = response.json()
            sql_query = response_data['choices'][0]['message']['content']
            return render_template('response.html', result=sql_query)
        except requests.RequestException as e:
            return f"Failed to make the request. Error: {e}", 500
    return render_template('index.html')

@app.route('/run-query', methods=['POST'])
def run_query():
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    try:
        conn = get_db_connect()
        cursor = conn.cursor()

        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]

        result = [dict(zip(columns, row)) for row in rows]

        conn.close()
        return jsonify(result)
    
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(use_reloader=False, debug=True)
    for rule in app.url_map.iter_rules():
        print(rule)

