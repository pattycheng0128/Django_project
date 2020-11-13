from django.shortcuts import render
from datetime import datetime



# Create your views here.
def index(request):
    return render(request, 'index.html', locals())

def show_tv(request, tvno=0):
    # return render(request, 'index.html',locals())
    # 查 youtube - tvcode
    tv_list = [{'name':'中視','tvcode':'ptqD4qo9D3I'},
        {'name':'民視','tvcode':'XxJKnDLYZz4'},
        {'name':'台視','tvcode':'xL0ch83RAK8'},
        {'name':'華視','tvcode':'-pvROC_MdYM'}]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    hour = now.timetuple().tm_hour
    return render(request, 'show_tv.html', locals())

def carlist(request, maker=0):
    car_maker = ['SAAB', 'Ford', 'Honda', 'Nissan']
    car_list = [[],
        ['A001', 'A002', 'A003', 'A004'],
        ['A001', 'A002', 'A003', 'A004'],
        ['A001', 'A002', 'A003', 'A004'],

    ]
    # maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carlist.html', locals())
