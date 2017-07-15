# python-micro-service-comments

A micro service to manage comments written in Python.

## Dependencies.

- flask
- sqlite3
- sqlalchemy
- python 3

## Run it.

```
FLASK_APP=src/main.py flask run
```

The application is running on `http://localhost:5000`
## Test

```
curl -X POST -H "Content-Type: application/json" -d '{"article_id": 1, "datetime": "2017-07-05 22:02:02", "text": "text", "author_id": 1}' http://localhost:5000/comment
curl -X POST -H "Content-Type: application/json" -d '{"article_id": 1, "datetime": "2017-07-06 10:30:32", "text": "text1", "author_id": 0}' http://localhost:5000/comment
curl -X POST -H "Content-Type: application/json" -d '{"article_id": 2, "datetime": "2017-07-05 15:23:17", "text": "text2", "author_id": 3}' http://localhost:5000/comment
curl http://localhost:5000/comment
```
## Use with Docker

```
docker run --name micro-service-comments -p 5000:5000 dannywillems/python-micro-service-comments
```
