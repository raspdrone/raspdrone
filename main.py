import sqlite3
import sensors
import dataxml
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="web", static_folder="web")
sensors = sensors.Sensors()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_data')
def get_data():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mesures")
    lines = cursor.fetchall()

    data = []
    for line in lines:
        new_data = {"id": line[0], "pression": round(line[3], 2), "temperature": round(line[2], 2), "timestamp": line[1], "altitude": round(line[4], 2)}
        data.append(new_data)

    return jsonify(data)

@app.route('/refresh')
def refresh():
    dataxml.to_db()
    return "OK"

@app.route('/new_mesure')
def new_mesure():
    sensors.new_mesure()
    return "OK"

app.run(host="0.0.0.0", port=6963)
