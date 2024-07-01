mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

celery:
    celery -A root worker -l INFO
