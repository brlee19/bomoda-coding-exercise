from flask import Flask
import json, time

app = Flask(__name__)

# read persisent_time_run and _first_ever_start from file
# if file is empty, init the file

times_run = 0
start_time = time.time()
app_data = {
    'server_first_start': None,
    'server_times_run': 0,
    'process_times_run': 0,
    'process_elapsed_time': 0,
}


@app.route('/status')
def index():
    global app_data, start_time
    # update process_times_run
    # update persistent_times_run and in the filesystem
    app_data['process_times_run'] += 1
    app_data['process_elapsed_time'] = time.time() - start_time
    return json.dumps(app_data)


if __name__ == '__main__':
    app.run(debug=True)