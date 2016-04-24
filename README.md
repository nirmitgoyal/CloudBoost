# CloudBoost
> I had to create a sample project, which I created in Django. This project should have two API's : 
 
API 1 :
METHOD :  POST
URL : /index   (my base URL is localhost:8000/cloudboost/)
Description : This takes in a sample message and indexes into ElasticSearch and Redis.
 
API 2 :
METHOD : GET 
URL : - /index
Description : This gets the data from Redis
 
API 3 :
METHOD : GET 
URL : /search
Description : This searches data from ElasticSearch.

####First install the necessary packages using 
`sudo pip install requirments.txt`

####Now, cd to cloudboost and run Django server:
`
cd cloudboost
python manage.py runserver
`