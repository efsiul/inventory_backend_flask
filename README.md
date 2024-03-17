# **NVENTORY CRUD IN FLASK**

This repository contains the configuration for a backend service, in which the methods can be accessed through 5 Endpoints:

- POST
- GET_BY_ID
- GET_ALL
- PUT
- DELETE

Contains the configurations to run inside a docker container next to a MySQL database.

The following tools are required to test the project:
    - Have Docker installed
    - Have Docker-compose installed
    - Have Postman or another tool installed to verify enpoints

## Architecture: The application has a layered architecture. They are

    - Entity
    - Model
    - Repository
    - Service
    - Controller
    - Routes

## Start the application

After you have everything you need to start the application, make sure you are in the root folder of the project and run the following command:

    ```bash
    docker-compose --build -d
    ```

Wait for about a minute, then you can see two containers running with the command

    ```bash
    docker ps -a
    ```

## Endpoints

- POST: <http://127.0.0.1:5000/api/products>

To add data with this crud make sure it has the following structure:

    ```json
    {
        "name": "Scalpel",
        "price": 2.34,
        "description": "cutting cutter",
        "quantity":32
    }
    ```

- GET_BY_ID: <http://127.0.0.1:5000/api/products/1>

Make sure you enter the ID number that corresponds to the product, and that it exists within the database

- GET_ALL: <http://127.0.0.1:5000/api/products>

This endpoint will bring a list with all the objects that are saved in the database

- PUT: <http://127.0.0.1:5000/api/products/1>
Make sure you enter the ID number that corresponds to the product, and that it exists within the database. Additionally, the data you want to change must follow the following structure:

    ```json
    {
        "name": "Scissors",
        "price": 3.55,
        "description": "Office scissors",
        "quantity": 25,
    }
    ```

     - DELETE: <http://127.0.0.1:5000/api/products/1>

Make sure you enter the ID number that corresponds to the product, and that it exists within the database