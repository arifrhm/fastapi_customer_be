# FastAPI Customer API

## Requirements

- Docker
- Docker Compose

## Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd fastapi_customer_be
    ```

2. Build and run the Docker containers:

    ```bash
    docker compose up --build -d
    ```

3. The application will be available at `http://localhost:8000`.

## Endpoints

- `POST /customers/` - Create a new customer
- `GET /customers/{customer_id}` - Retrieve a customer by ID
- `GET /customers/` - Retrieve all customers
- `PUT /customers/{customer_id}` - Update a customer by ID
- `DELETE /customers/{customer_id}` - Delete a customer by ID

## Running Tests

1. Ensure Docker containers are running.
2. Build, test, and run the application:

    ```bash
    ./build_test_run.sh
    ```

   Alternatively, you can run each command separately:

    ```bash
    docker compose build
    docker compose run --rm web pytest
    docker compose up
    ```

## Notes

- The database is set up with PostgreSQL.
- Default database credentials are based on your `.env` file. An example configuration can be found in `.env.example`. Make sure to create and adapt your own `.env` file accordingly.
