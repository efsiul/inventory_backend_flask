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
You need to look at the container number and run the following command

     ```bash
     docker start [flask_container]
     ```

## Endpoints

- GET_ALL: <http://172.23.0.3:5000/>

This endpoint will take you to the home page, where the list of items saved in the database and options to add, delete, edit, or view details will be displayed.

- POST: <http://172.23.0.3:5000/add>

This page will allow you to add items with their respective characteristics.

- GET_BY_ID: <http://172.23.0.3:5000/1>

In this endpoint you can see details of a specific item

- PUT: <http://172.23.0.3:5000/edit/1>
Entpoint that allows updating the attributes of an already created item

- DELETE: <http://172.23.0.3:5000/delete/1>
Endpoint that allows you to delete an item.

---