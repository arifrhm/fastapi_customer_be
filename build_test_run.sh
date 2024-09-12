#!/bin/bash

# Start the db container
docker-compose up -d db

# Wait for the db container to be ready
echo "Waiting for PostgreSQL to become available..."
until docker-compose exec -T db pg_isready -U $POSTGRES_USER -d $POSTGRES_DB; do
  sleep 1
done

# Build and start the web container
docker-compose up --build -d web

# Run mypy type checks
echo "Running mypy type checks..."
mypy app/
if [ $? -ne 0 ]; then
    echo "mypy type checks failed. Exiting."
    exit 1
fi

# Run the tests
echo "Running pytest..."
docker-compose run --rm web pytest

# Optionally restart the db container
docker-compose up -d
