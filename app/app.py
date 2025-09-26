from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

# Connect to Redis service using environment variable
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_client = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def home():
    redis_client.incr('hits')
    count = redis_client.get('hits').decode('utf-8')
    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
