from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import numpy as np
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

sales_data = [
    {'product_name': 'Product A', 'price': 50},
    {'product_name': 'Product B', 'price': 80},
    {'product_name': 'Product C', 'price': 60},
    # Add more data here
]

def update_prices():
    while True:
        for sale in sales_data:
            sale['price'] *= np.random.normal(1, 0.05)
        socketio.emit('update_prices', sales_data, namespace='/')
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html', sales_data=sales_data)

@socketio.on('connect', namespace='/')
def test_connect():
    emit('update_prices', sales_data)

if __name__ == '__main__':
    t = threading.Thread(target=update_prices)
    t.start()
    socketio.run(app, debug=True)
