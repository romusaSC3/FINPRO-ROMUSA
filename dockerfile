# create your dockerfile here, for more information, read readme.md
FROM python:3.9-slim-buster

WORKDIR /app

COPY . .
RUN python -m pip install python-dotenv
RUN python -m pip install -r requirements.txt

# COPY app .env ./

EXPOSE 5000

CMD ["python3", "-m", "flask", "--app", "app/app", "run", "--host=0.0.0.0"]
