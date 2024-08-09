FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

# Define environment variable to specify the SQLite database
ENV DATABASE_URL=sqlite:///./test.db

# Run the application
CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 80"]
