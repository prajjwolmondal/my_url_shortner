release: flask db upgrade
web: gunicorn my_url_shortner.app:create_app\(\) -b 0.0.0.0:$PORT -w 3
