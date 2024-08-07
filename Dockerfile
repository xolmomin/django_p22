FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirements.txt

RUN chmod +x entrypoint

CMD ["./entrypoint"]
