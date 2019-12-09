# EleNa Project

Most standard navigation applications are looking to provide you with a shortest distance path or a shortest time path. What we've done here is provide a functioning navigation application which returns a path in which we are looking to minimize elevation gain within a certain threshold. This can be useful for a variety of applications, specifically hiking and/or biking. We decided to lower our scale and focus on Amherst, Massachusetts. Our focus is on walking/hiking and we have made our application mobile-friendly. 

## How the application works

The 

This is for you guys to understand the backend flow 

1. Frontend send the request 
2. The request will heat `backend/algorithm/views.py`
3. Create the model object from `backend/algorithm/model.py`
4. Create the navigator object from `backend/algorithm/algorithm.py`
5. Run the algorithm ad get the result from `my_navigator.get_the_path()`
6. Send the result to the frontend

## Testing

### FrontEnd Testing
Our frontend testing relates primarily to user input and to ensure that the page is displaying properly. 
#### Tests
Assertions: 
* The frontend input textboxes pertaining to the "Start Location" and "Destination Location" changes are properly reflected and hold user input. 
* Visiting a page returns a 200-level response. 
* Map component is visible upon loading a page. 

### BackEnd Testing
Our backend testing is substantial as it is of utmost importance to ensuring the success of our application. 

backend/algorithm/test.py
Test_Model

Assertions:<br>
A test model was created to imitate the real model. This model is controlled and the expected values are well-known. 
- Threshhold 2.0 or 200%
    - Shortest Path: A -> B -> D
        - Distance Traveled: 5
        - Elevation Gain: 1

    - Minimized Elevation: A -> C -> D
        - Distance Traveled: 7
        - Elevation Gain: 1
- Threshold 1.0 or 100%
    - Shortest Path: A -> B -> D
    - Minimized Elevation: A -> B -> D
        - Distance Traveled: 5
        - Elevation Gain: 2

Imitation Model: 
![](image.png)

## How to run the application locally
Requirements: Docker Desktop
* [Docker Desktop](https://www.docker.com/products/docker-desktop)

Run Docker. After cloning the respository, run the following command from the project directory:

```
docker-compose up
```
Once it finishes building and runs services, visit: `localhost:3050`

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

* **Geon Yoon** - *Backend and DevOps* - [GeonYoon](https://github.com/GeonYoon)
* **Jackson Weber** - *Frontend* - [JacksonWeber](https://github.com/JacksonWeber)
* **Adam Tiago** - *API research and testing* - [Adam Tiago](https://github.com/tiagosaurus)
* **Kevin Tu** - *API research and testing* - [Kevin Tu](https://github.com)