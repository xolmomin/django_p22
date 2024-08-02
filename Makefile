mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

celery:
	celery -A root worker -l INFO

beat:
	celery -A root beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler


# Docker

image:
	docker build -t django_image .

container:
	docker run -p 8000:8000 -d django_image
	#docker run --name django_container -p 8000:8000 -d django_image