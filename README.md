# CloudBoost
> I had to create a sample project, which I created in Django. This project should have two API's : 
 
> API 1 :

> METHOD :  POST

> URL : /index   (my base URL is localhost:8000/cloudboost/)

> Description : This takes in a sample message and indexes into ElasticSearch and Redis.
 
 

> METHOD : GET 

> URL : - /index

> Description : This gets the data from Redis
 
 
> API 2 :

> METHOD : GET 

> URL : /search

> Description : This searches data from ElasticSearch.

####First install the necessary packages using 
`sudo pip install requirments.txt`

####Now, cd to cloudboost and run Django server:
```
cd cloudboost
python manage.py runserver
```

####Now, run elasticsearch server:
```
cd elasticsearch-2.3.1/bin
./elasticsearch
```

####Now, run redis server:
```
cd redis-3.0.7
src/redis-server
```

###Now, go to [localhost:8000/cloudboost/](http://localhost:8000/cloudboost/)


####First, hit a POST resuest @ localhost:8000/cloudboost/index using curl or postman *(i.e. without using forms)*:

###1)Using CURL
`curl -F message=amazing http://localhost:8000/cloudboost/index/`

###2)Using [postman](https://www.getpostman.com/)
You can hit a POST, GET, PUT, DELETE,  etc request using postman.

####Now, search the value in Elasticsearch database by hitting a GET request @ localhost:8000/cloudboost/search :

`localhost:8000/cloudboost/search/?message=<value>`

####You can get the value from Redis database by hitting a GET request @ localhost:8000/cloudboost/index/
`localhost:8000/cloudboost/index/?key=message`
