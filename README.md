# apiservice
public facing API service


# Steps to run locally:
## 1 Build the images
### 1.1 Redis image: The default image can be used. Hence, building redis image is not required

### 1.2 Api image: Go to the app root path where there is the Dockerfile. Run: 
    docker build -t apiservice .

## 2 Run the images
### 2.1 start redis container 
    docker run -d --name redis -p6379:6379 redis
### 2.2 start api container
    docker run -d --name apiservice -p5000:5000 apiservice
