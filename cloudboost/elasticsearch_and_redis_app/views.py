from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from cloudboost.settings import es,rds
from django.views.decorators.csrf import csrf_exempt



def cloudboost(request):
    template = loader.get_template('elasticsearch_and_redis_app/index.html')
    context = {}        
    
    return HttpResponse("Hello, world. This is home page"+template.render(context, request))

@csrf_exempt
def index(request):
    # book = get_object_or_404(Books)
    if request.method == 'GET':
    	result=rds.get("message") #since I had to index only one item, i.e. message, I only create a key message,
    								# otherwise I would have used list in Redis
    	return HttpResponse(result)
    elif request.method == 'POST':
    	message = request.POST['message']
    	res = es.index(index="test-index", doc_type='cloudboost', body={"message": message, "timestamp": datetime.now()})
    	res1=rds.set("message",message)
    	# template = loader.get_template('elasticsearch_and_redis_app/insert.html')
    	# context={}
    	return HttpResponse(str(res)+str(res1))
    	
    else:
    	return HttpResponse("GET/POST required")

def search(request):
	res = es.search(index="test-index", body={"query": {"match": {"message": request.GET['message']} }})
	ret = []
	for hit in res['hits']["hits"]:
		ret.append(hit['_source'])
	return HttpResponse(str(ret)) 

