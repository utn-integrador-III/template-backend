# About of the repo

## main branch: 

It has an almost complete solucion about the project developed in monolithic architecture.

## template branch

It is a template project where you can take it for starting your own solution.

# Workshop in RestApi (Python): Books Information

## Problem statement

Create a restapi with microservice architecture with following apis (add them docker container using docker compose and Unit Testing and Mock testing):


- Security

This api needs to have a CRUD behavior for Users, the user information shoul be stored in MongoDB.

Required endpoints in the api:

| EndPoint | Description | Input | Output |
| ------ | ------ | ------ | ------ |  
| GeAll | Endpoint returns a user list |  | { data: [{userId, name, email, password, isActive:true}, {userId, name, email, password, isActive:false}], responseCode , message} |
| GetAllActive | Endpoint returns an active user list (where isActive=true) |  | {data:[{userId, name, email, password, isActive:true}], responseCode , message} |
| Create | Endpoint to insert a new user. Backend needs to create the userId and isActive as default value |  | {data:{userId, name, email, password, isActive:true}, responseCode , message} |
| Update | Endpoint to update an especific user. | {userId, name, email, password, isActive} | {data:{userId, name, email, password, isActive}, responseCode , message} |
| Delete | Endpoint to delete an user | userId | { data: {userId:""}, responseCode , message} |

- Book

Create an api with endpoints for searching a book (request to another api).

| EndPoint | Description | Input | Output | Request | Example
| ------ | ------ | ------ | ------ | ------ | ------ |   
| GetByTitle | Endpoint that returns the info of a book. | title | { data: {title, author:["A", "B"], key, place:["A","B"]}, responseCode , message} | http://openlibrary.org/search.json?title={title} | http://openlibrary.org/search.json?title=The_Way_of_All_Flesh |
| GetByKey | Endpoint that returns the details of a book | key | { data: {title, description, covers, subjects:["A", "B"], latestRevision}, responseCode , message} | https://openlibrary.org/works/{key}.json | https://openlibrary.org/works/OL15099863W.json |


## Important to know

```sh

You can take the main branch as an example, however, it is not in a microservice architecture.

You must follow the folders structure in the project (db, controlles, models, util).

Remember apply the best practices as: Unit testing, environment variables, applying design patterns and modularity.

Additionally, you can configure dcoker container in the project.

```

## Things to consider them:

- create virtual env: python3 python3 -m venv venv
- run pip3 install -r requirements.txt
- create .env file with environment variable with connection strings, DBNm and others.
- If you are using vs code, go to run and debug and create a launch.json file and add the following (for env file, copy your path and paste it): { "version": "0.2.0", "configurations": [ { "name": "Python: Current File", "type": "python", "request": "launch", "program": "./app.py", "console": "integratedTerminal", "envFile": "/Users//Desktop/BOOKING_APP/space-booking-api/Management_API/.env" } ] }
 - Run the project under 'Run and debug'


## Things to consider them:
2. create virtual env: `python3 -m venv venv`
3. create .env file
4. run pip3 install -r requirements.txt
5. If you are using vs code, go to `run and debug` and create a launch.json file and add the following (for env file, copy your path and paste it): { "version": "0.2.0",
   "configurations": [
        {
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "./app.py",
            "console": "integratedTerminal",
            "envFile": "<<project_path>>/.env"
        }
   ]
   

6. Run the project under 'Run and debug'
7. If you get mongo certificate issues, run the following command with the proper python version on your system: `open "/Applications/Python 3.10/Install Certificates.command" `


### If you get mongo issues:
- certificate: Run the following command with the proper python version on your system: open "/Applications/Python 3.10/Install Certificates.command"
- Enable network configuration in Mongo Atlas
- Remove any ssl flag in connectionstring.

