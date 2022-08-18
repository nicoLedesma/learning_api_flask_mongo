## Introduction
This project contains two endpoints built in Flask (a lightweight WSGI web application framework). Its goal is to allow to add a task (Linux command) and get the result of its execution.
The POST endpoint `/new_task` must receive a json request with this syntax `{"cmd": "dir"}`, and will return a
json response with the created task with this syntax `{"id": "1"}`
The GET endpoint `/get_output/<id>` must receive a task_id in the URL and will return a
json response with the executed command and its output with this syntax: `{"cmd": "dir", "output": "..."}`.

The docker-compose file contains the API container and a Mongo database container. 
   

## Installing

* Setup docker containers

 1. Configure .env file if necessary

 2. Start up containers:  `$ docker-compose up -d`

## Usage
##### For testing endpoints in a simple way, we are going to use curl command.

Please replace "PORT" below with the binded port on the docker-compose file and "COMMAND" with a valid linux command, as an example: "ls -l".
1. Create task: `curl -X POST -H "Content-Type: application/json" -d '{"cmd": <COMMAND>}' http://localhost:<PORT>/new_task`
2. The endpoint above will return the "ID" of the created task.
3. Retrieve a command output using (for example): `curl http://localhost:<PORT>/get_output/<ID>`
4. Finally, you will get the command and the result of the execution of it. 
