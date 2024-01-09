FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev libffi-dev openssl-dev
EXPOSE 80
ENV NAME World
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
