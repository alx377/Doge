# Doge

## Build and publish production image

- `docker build -t aleksinyyss/doge:latest .`
- `docker push aleksinyyss/doge:latest`

## Prod

- ssh to container
- if docker-compose.yml file is not there copy it from this repo
- copy all the mp3's you want to /root/mp3 folder
- `docker-compose down`
- `docker-compose up -d`

Make sure that DOGE_TOKEN env var is correct on host machine
