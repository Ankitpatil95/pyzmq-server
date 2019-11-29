# pyzmq-server
Steps to connect server

With Docker
1) Build docker image file

	```docker-compose up```
2) Now app is running at http://127.0.0.1:5000/ 

Without Docker Image
1) Create virtualenv
2) Install requirements.txt
	
    ```pip install -r requirements.txt```
        
3) Run Flask project: 
	
	```python server.py```

4) Now app is running at http://127.0.0.1:5000/
