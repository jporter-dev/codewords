timeout = 60
worker_class = 'eventlet'
reload=True
workers=1 # multiprocessing.cpu_count() * 2 + 1
threads = 1 # multiprocessing.cpu_count() * 2 + 1
bind = '0.0.0.0:5000'
