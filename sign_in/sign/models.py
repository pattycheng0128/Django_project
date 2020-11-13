from django.db import models

# Create your models here.
class Event(models.Model):
    #發佈會的標題
    name = models.CharField(max_length=100)
    #參加的人數
    limit = models.IntegerField()
    #狀態
    status = models.BooleanField()
    #地址
    address = models.CharField(max_length=200)
    #發佈會時間
    start_time = models.DateTimeField('event time')
    #建立時間
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Guest(models.Model):
    # 關聯發佈會id
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    #realname
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("event", "phone")

    def __str__(self):
        return self.realname
