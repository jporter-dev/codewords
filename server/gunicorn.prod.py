import multiprocessing

timeout = 60
worker_class = 'eventlet'
workers= multiprocessing.cpu_count() * 2 + 1
threads =  multiprocessing.cpu_count() * 2 + 1
bind = '0.0.0.0:5000'
