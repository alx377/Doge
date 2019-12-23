# Doge

docker build -t doge .
docker tag doge aleksinyyss/doge:latest
docker push aleksinyyss/doge:latest

docker run -p localhost:80:5000 aleksinyyss/doge:latest
