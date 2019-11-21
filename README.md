# pyzmq-server
Steps to connect server

With Docker
1) Build docker image file

	```docker build -t python-server .```
2) Run docker image file
	
    ```docker run --network="host" python-server```
3) Now app is running at http://127.0.0.1:5000/ 

Without Docker Image
1) Create virtualenv
2) Install requirements.txt
	
    ```pip install -r requirements.txt```
    
3) Run Flask project: flask run

4) Now app is running at http://127.0.0.1:5000/
