from flask import Flask, request, jsonify, send_from_directory
from redis import Redis
from rq import Queue
from worker import scan_ip
import uuid

app = Flask(__name__)
redis_conn = Redis()
q = Queue(connection=redis_conn)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('.', 'index.html')

@app.route('/job', methods=['POST'])
def create_job():
    ip_address = request.json['ip']
    job = q.enqueue(scan_ip, ip_address, result_ttl=60*60*8)
    return jsonify({"job_id": job.get_id()}), 202

@app.route('/job/<job_id>', methods=['GET'])
def get_job_status(job_id):
    job = q.fetch_job(job_id)
    if job is None:
        return jsonify({"error": "Invalid job ID"}), 404

    return jsonify({
        "job_id": job.get_id(),
        "status": job.get_status(),
        "result": job.result
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)