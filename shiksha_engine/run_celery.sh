#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

cd /home/ubuntu/code

# run Celery worker for our project myproject with Celery configuration stored in Celeryconf
celery -A tasks worker --loglevel=info -B
