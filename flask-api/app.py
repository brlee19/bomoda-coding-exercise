from flask import Flask
from datetime import datetime
from time import time
import json

app = Flask(__name__)

# get data from data.json if the server has been run before
# or initialize it if this is the first time the server is being run
try:
    persisted_data = open('data.json', 'r')
    server_data = json.load(persisted_data)
    server_first_start = server_data['server_first_start']
    server_endpoint_times_requested = server_data['server_endpoint_times_requested']
    persisted_data.close()
except FileNotFoundError:
    server_first_start = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    server_endpoint_times_requested = 0

# dictionary with all app data
times_run = 0
start_time = time()
app_data = {
    'process_elapsed_time': 0,
    'process_endpoint_times_requested': 0,
    'server_first_start': server_first_start,
    'server_endpoint_times_requested': server_endpoint_times_requested,
}


@app.route('/status')
def index():
    # update app data
    global app_data, start_time, server_first_start
    app_data['process_endpoint_times_requested'] += 1
    app_data['process_elapsed_time'] = time() - start_time
    app_data['server_endpoint_times_requested'] += 1

    # update data.json
    with open('data.json', 'w') as data_file:
        json.dump({
            'server_first_start': server_first_start,
            'server_endpoint_times_requested': app_data['server_endpoint_times_requested']
        }, data_file)

    return json.dumps(app_data)


if __name__ == '__main__':
    app.run(debug=True)