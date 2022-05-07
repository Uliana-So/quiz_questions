# quiz_questions

## About project
A little web-app which returns one question per request for a quiz.

## Requirements for Linux
- make
- docker version 20.10.14
- docker-compose version 1.25.0

## Run project
Need to call `make` (or `sudo make`). It depends on your access level for docker daemon.

## Example

##### Request
```
curl -i -X POST -H "Content-Type: application/json" 127.0.0.1:8080/quiz -d '{"questions_num":1}'
```

##### Response
```
HTTP/1.1 200 OK
Server: nginx/1.21.6
Date: Fri, 06 May 2022 22:05:36 GMT
Content-Type: application/json
Content-Length: 90
Connection: keep-alive

{"question":"A formal public statement, like the one Abraham Lincoln made in early 1863"}
```
