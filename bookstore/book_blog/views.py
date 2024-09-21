from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil
# Create your views here.

def index(request):
    products=product.objects.all()
    print(products)
    n=len(products)
    nofslides=n//4 + ceil((n/4) -(n//4))
    # params={ 'no_of_slides':nofslides,'range':range(1,nofslides),'product':products}
    allprods=[[products,range(1 ,len(products)),nofslides],[products,range(1 ,len(products)),nofslides]]
    params={'allprod':allprods}
    return  render(request,'blog/index2.html', params)


def about(request):
    return render(request,'blog/about.html')