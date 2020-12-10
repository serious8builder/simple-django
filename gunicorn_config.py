import os

bind = '0.0.0.0:' + os.environ.get('SIMPLE_DJ_PORT', '5000') # --bind 0.0.0.0:8000
max_requests = 10
num_cpu = os.cpu_count()
workers = int(os.getenv('SIMPLE_DJ_WORKERS') or 2 * num_cpu + 1)

worker_connections = 10
timeout = 60
keepalive = 2

os.makedirs('/tmp/simple-dj', exist_ok=True)
pidfile = "/tmp/simple-dj/simple-dj.pid"    # --pid /home/ubuntu/project/simple-api/gunicorn.pid
logfile = "/tmp/simple-dj/simple-dj.log"    # --log-file /home/ubuntu/project/simple-api/gunicorn.log
loglevel = "debug"
errorlog = '-'
accesslog = '-'

proc_name = "simple-dj"
preload_app = True
