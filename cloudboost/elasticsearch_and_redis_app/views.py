from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from cloudboost.settings import es,rds
from django.views.decorators.csrf import csrf_exempt
# import json



def cloudboost(request):
    template = loader.get_template('elasticsearch_and_redis_app/index.html')
    context = {}        
    
    return HttpResponse("Hello, world. This is home page"+template.render(context, request))

@csrf_exempt
def index(request):
    # book = get_object_or_404(Books)
    if request.method == 'GET':
    	key=request.GET['key']
    	result=rds.get(key) 
    	return HttpResponse(result)
    elif request.method == 'POST':
    	message = request.POST['message']
    	res1 = es.index(index="test-index", doc_type='cloudboost', body={"message": message, "timestamp": datetime.now()})
    	res2=rds.set("message",message)#since I had to index only one item, i.e. message, I only create a key message,
    								# otherwise I would have used list in Redis    	
    	# res1=json.dumps(res1, sort_keys=False, indent=4, separators=(',', ': '))
    	response="\n\n".join([str(res1),str(res2)])
    	
    	# template = loader.get_template('elasticsearch_and_redis_app/insert.html')
    	# context={}
    	return HttpResponse(response)
    	
    else:
    	return HttpResponse("GET/POST required")

def search(request):
	res = es.search(index="test-index", body={"query": {"match": {"message": request.GET['message']} }})
	ret = []
	for hit in res['hits']["hits"]:
		ret.append(hit['_source'])
	return HttpResponse(str(ret)) 

