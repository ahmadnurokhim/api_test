from flask import Flask, request, jsonify

app = Flask(__name__)

data = [
    {'time': '25/28/2023', 'value': 27},
    {'time': '26/28/2023', 'value': 25},
    {'time': '27/28/2023', 'value': 31},
    {'time': '28/28/2023', 'value': 26},
    {'time': '29/28/2023', 'value': 27}
]

@app.route('/get_data', methods=['GET'])
def get_data():
    time_param = request.args.get('time')

    if time_param:
        result = [entry for entry in data if entry['time'] == time_param]
        if result:
            return jsonify(result)
        else:
            return "No data found for the given time.", 404
    else:
        return jsonify(data)

@app.route('/add_data', methods=['POST'])
def add_data():
    new_entry = request.get_json()
    
    if 'time' in new_entry and 'value' in new_entry:
        data.append(new_entry)
        return "Data added successfully.", 201
    else:
        return "Invalid data format. Both 'time' and 'value' are required.", 400

if __name__ == '__main__':
    app.run(debug=True)
