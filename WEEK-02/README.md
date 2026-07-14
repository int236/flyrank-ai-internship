# Week 02 - Docker & PostgreSQL
This project is a FastAPI application connected to a PostgreSQL database running inside Docker.

## Requirements
- Docker Desktop
- Docker Compose

## Running the Project
Build and start the application and database:
```bash
docker compose up --build
```

The API will be available at:
```
http://localhost:8000
```

Swagger documentation:
```
http://localhost:8000/docs
```

## Environment Variables
The PostgreSQL connection string is stored in the `.env` file.
An example configuration is provided in `.env.example`.

## Database
- PostgreSQL runs inside a Docker container.
- A Docker volume is used so that database data persists across container restarts.

## Persistence Test
1. Started the application using Docker Compose.
2. Added a message using the `/add/{text}` endpoint.
3. Verified the message using the `/messages` endpoint.
4. Stopped the containers with:
```bash
docker compose down
```
5. Started the containers again:
```bash
docker compose up
```
6. Verified that the previously added message was still present in `/messages`, confirming that the PostgreSQL volume preserved the data.

## Technologies Used
- Python
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- psycopg2