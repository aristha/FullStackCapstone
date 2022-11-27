# API Capston
## Casting Agency  App 
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.
Project use python3, postgrsql, heroku deploy
## Host Heroku: https://appdemo-tam.herokuapp.com

### Getting Started
Pre-requisites and Local Development
Developers using this project should already have Python3, pip and node installed on their local machines.

### Role

- Casting Assistant
    - Can view actors and movies
- Casting Director
    - All permissions a Casting Assistant has and…
    - delete an actor from the database
    - Modify actors or movies
- Executive Producer
    - All permissions a Casting Director has and…
    - delete a movie from the database

### BackEnd

To run the application run the following commands(window):
```console
    python -m virtualenv env
    source env/Scripts/activate
    pip3 install -r requirements.txt
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    sh setup.sh
```
The application is run on http://127.0.0.1:5000/ 


### USE postman collection 
[Collection API](Capston.postman_collection.json)
- Folder Casting Assistant with role Casting Assistant
- Folder Casting Director with role Casting Director
- Folder Executive Producer with role Executive Producer

## API Reference

### Error Handling
Errors are returned as JSON objects in the following format:
```console
{
    "success": False, 
    "error": 404,
    "message": "resource not found"
}
```
The API will return three error types when requests fail:
- 404: Resource Not Found
- 422: Not Processable

### Endpoints
#### GET /actors
- General:
  - Returns a actors success value
  - Sample: `curl http://127.0.0.1:5000/actors `
```console
{
    "actors": [
        {
            "age": 12,
            "gender": "12",
            "id": 2,
            "name": "abc"
        },
        {
            "age": 12,
            "gender": "12",
            "id": 3,
            "name": "abc"
        }

    ],
    "success": true
}
```

#### GET /movies
- General:
  - Returns a movies success value
  - Sample: `curl http://127.0.0.1:5000/movies `
```console
{
    "movies": [
        {
            "id": 1,
            "releaseDate": "2022/01/01",
            "title": "mv1"
        },
        {
            "id": 2,
            "releaseDate": "2022/02/01",
            "title": "mv1"
        }
    ],
    "success": true
}
```

#### POST /actors
- General:
  - Create new Actor a Actors success value
  - Sample: `curl  http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{"name":"An", "age":17, "category":"1",, "gender":"F"}`
```console
{
    "actors": [
        {
            "age": 12,
            "gender": "M",
            "id": 1,
            "name": "abc"
        },
        {
            "age": 14,
            "gender": "F",
            "id": 2,
            "name": "An"
        }
    ],
    "success": true
}
```

#### POST /movies
- General:
  - Create new movie a movies success value
  - Sample: `curl  http://127.0.0.1:5000/movies -X POST -H "Content-Type: application/json" -d '{"title":"mv2", "release_date":"2022-01-01 08:00:00"}`
```console
{
    "movies": [
        {
            "id": 1,
            "releaseDate": "2022/01/01",
            "title": "mv1"
        },
        {
            "id": 2,
            "releaseDate": "2022/01/01",
            "title": "mv2"
        }
    ],
    "success": true
}
```


#### PATCH /actors
- General:
  - update  Actor a Actors success value
  - Sample: `curl  http://127.0.0.1:5000/actors/1 -X PATCH -H "Content-Type: application/json" -d '{"name":"Ban", "age":17, "gender":"F"}`
```console
{
    "actors": [
        {
            "age": 18,
            "gender": "F",
            "id": 1,
            "name": "Ban"
        },
        {
            "age": 14,
            "gender": "F",
            "id": 2,
            "name": "An"
        }
    ],
    "success": true
}
```

#### POST /movies
- General:
  -  update movie a movies success value
  - Sample: `curl  http://127.0.0.1:5000/movies/1 -X POST -H "Content-Type: application/json" -d '{"title":"mv3", "release_date":"2022-01-01 08:00:00"}`
```console
{
    "movies": [
        {
            "id": 1,
            "releaseDate": "2022/01/01",
            "title": "mv3"
        },
        {
            "id": 2,
            "releaseDate": "2022/01/01",
            "title": "mv2"
        }
    ],
    "success": true
}
```

#### DELETE /actors/<int:actor_id>
- General:
  - DELETE question using a question ID.
  - Sample: `curl -X DELETE http://127.0.0.1:5000/actors/1 `
```console
{
    "success": true
}
```
#### DELETE /movies/<int:movie_id>
- General:
  - DELETE question using a question ID.
  - Sample: `curl -X DELETE http://127.0.0.1:5000/movies/1 `
```console
{
    "success": true
}
```



role
delete:actors
patch:actors
post:actors
get:actors

delete:movies
patch:movies
post:movies
get:movies