# Assignment: Cloud and Big Data Rest Service with Swagger

### Service Description
 Outputs a system log entry.

Here, I have implemented a service that outputs a log entry from the system. The swagger code-gen generate the server stub code for us by taking the log.yaml as input and gives us a foundation to develop the main logic. 

### Main logic : log_stub.py 
### Location - https://github.com/cloudmesh-community/hid-sp18-421/swagger-docker /log_stub.py

You can download the code from the repository and test or enhance further.

Follow the below steps
Clone the repository
Makefile and Dockerfile are also in the above location

After you run sudo make docker-all command from your terminal
Docker will create an Ubuntu image, and after docker image is created, make file executes series of commands, creating my swagger REST service in the docker container
 
You will see something like this Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)

Running the service from browser
Open any browser and request with DB_URL Ex: Input : http://0.0.0.0:8080/api/db  
