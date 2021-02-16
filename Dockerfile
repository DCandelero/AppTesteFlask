from python:3.7
env home=/home/app
workdir $home
run pip install --upgrade pip
copy requirements.txt $home/requirements.txt
run pip install -r requirements.txt
copy . $home
entrypoint gunicorn --bind 0.0.0.0:8080 wsgi:app
