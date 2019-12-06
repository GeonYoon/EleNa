# EleNa Project

Explain about the project

## How the application works

This is for you guys to understand the backend flow

1. Frontend send the request 
2. The request will heat `backend/algorithm/views.py`
3. Create the model object from `backend/algorithm/model.py`
4. Create the navigator object from `backend/algorithm/algorithm.py`
5. Run the algorithm ad get the result from `my_navigator.get_the_path()`
6. Send the result to the frontend

## How to run the application locally

First, you need to have Docker installed in your desktop.
Run the following command in the project directory (where you have docker-compose.yml file).

```
docker-compose up
```
Once it finishes the building and runs the services, visit `localhost:3050`

## How to Update the Docker Images 

If you want to test the application after you make somes changes into the application, you need to force Docker to rebuild the images.
In this case, Run the following command.

```
docker-compose up --build
```

## Built With

* [React](https://www.djangoproject.com) - Javascript Frontend framework
* [Django](https://www.djangoproject.com) - Python Web framework


## Authors

* **Geon Yoon ** - *Backend and DevOps* - [GeonYoon](https://github.com/GeonYoon)
* **Jackson Weber ** - *Frontend* - [JacksonWeber](https://github.com)
* **Adam Tiago ** - *API research and testing* - [Adam Tiago](https://github.com)
* **Kevin Tu ** - *API research and testing* - [Kevin Tu](https://github.com)