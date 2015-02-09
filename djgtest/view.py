from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Book
import datetime

def current_datetime(request):
    now=datetime.datetime.now()
    # t=get_template("time.html")
    ar=[0,1,2,3,4]
    # html=t.render(Context({'current_date':now,'ar':ar}))
    # return HttpResponse(html)
    return render_to_response('test/time.html',{'current_date':now,'ar':ar})

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('test/search_results.html',
                {'books': books, 'query': q})
    return render_to_response('test/search_form.html',
        {'errors': errors })