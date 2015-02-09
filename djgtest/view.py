from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now=datetime.datetime.now()
    # t=get_template("time.html")
    ar=[0,1,2,3,4]
    # html=t.render(Context({'current_date':now,'ar':ar}))
    # return HttpResponse(html)
    return render_to_response('test/time.html',{'current_date':now,'ar':ar})