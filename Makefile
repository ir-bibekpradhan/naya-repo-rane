.PHONY: build run test logs clean

## Build the Docker image
build:
	docker compose build

## Run the container
run:
	docker compose up

## Build and run in one shot
up:
	docker compose up --build

## Run tests locally (no Docker)
test:
	pytest tests/ -v

## Follow container logs
logs:
	docker compose logs -f

## Stop and remove containers
down:
	docker compose down

## Remove image and containers
clean:
	docker compose down --rmi local --volumes --remove-orphans
