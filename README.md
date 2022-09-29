# aweber
An django rest api for interview with Aweber.

Build Docker Image:

docker build -t aweber_widget_api .

Run Docker Container:

docker run -d -p 8080:8000 --name aweber_widget_api aweber_widget_api

# openapi/swagger specification

Downloadable OpenAPI schema: 127.0.0.1:8080/schema/
Swagger UI: 127.0.0.1:8080/schema/swagger-ui