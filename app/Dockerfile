FROM python:3.9-slim
WORKDIR /app
RUN pip install Flask
COPY . .
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]