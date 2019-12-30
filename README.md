# Doge

## Build and publish production image

docker build -t doge .
docker tag doge aleksinyyss/doge:latest
docker push aleksinyyss/doge:latest

## How to update prod

- ssh to container
- `docker-compose down`
- `docker-compose up -d`

Make sure that DOGE_TOKEN env var is correct on the host.
