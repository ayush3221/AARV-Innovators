from flask import Flask, jsonify, render_template
from services.etp_calculations import calculate_treatment
from services.iot_simulator import get_live_sensor_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/live-data')
def live_api():
    # 1. Get raw sensor readings
    raw_data = get_live_sensor_data()
    # 2. Calculate treated values
    processed_results = calculate_treatment(raw_data)
    
    return jsonify({
        "input_sensor": raw_data,
        "output_treated": processed_results
    })

if __name__ == '__main__':
    app.run(debug=True)