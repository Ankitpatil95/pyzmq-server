# pyzmq-server
Steps to connect server

With Docker
1) Build docker image file

	```docker build -t python-server .```
2) Run docker image file
	
    ```docker run -a stdin -a stdout -i -t --network="host" python-server```

Without Docker Image
1) Create virtualenv
2) Install requirement.txt
	
    ```pip install -r requirement.txt```
3) Run Server File

    ```python server.py```
