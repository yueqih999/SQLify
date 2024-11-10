from flask import Flask, render_template, request, redirect, url_for, json
import os
import requests
import base64

app = Flask(__name__)

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
        API_KEY = "85WNpJ3ghADNfVwDU3H3mC7F1Mjvrzy5rqNWw4q0gW8bAekTyB2gJQQJ99AKACHYHv6XJ3w3AAABACOGyd4m"
        #IMAGE_PATH = "path/to/your/image.png"
        #encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
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


if __name__ == '__main__':
    app.run(use_reloader=False, debug=True)
