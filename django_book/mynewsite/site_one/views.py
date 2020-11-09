from django.shortcuts import render
from datetime import datetime



# Create your views here.
def index(request, tvno=0):
    # return render(request, 'index.html',locals())
    # 查 youtube - tvcode
    tv_list = [{},
        {},
        {},
        {}]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())