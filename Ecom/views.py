from django.shortcuts import render
from django.http import HttpResponse
from .models import items
# Create your views here.
def index(request):
    item1=items()
    item1.name='pant'
    item1.price='750'
    item1.img='item-01.jpg'
    item2=items()
    item2.name='pant2'
    item2.price='7502'
    item2.img='item-02.jpg'
    item3=items()
    item3.name='pant3'
    item3.price='7503'
    item3.img='item-03.jpg'
    item4=items()
    item4.name='pant4'
    item4.price='7504'
    item4.img='item-04.jpg'
    item5=items()
    item5.name='pant5'
    item5.price='7505'
    item5.img='item-05.jpg'
    item6=items()
    item6.name='pant6'
    item6.price='7506'
    item6.img='item-06.jpg'
    item7=items()
    item7.name='pant7'
    item7.price='7507'
    item7.img='big-01.jpg'
    its=[item1,item2,item3,item4,item5,item6,item7]
    return render(request,'index.html',{'its':its})