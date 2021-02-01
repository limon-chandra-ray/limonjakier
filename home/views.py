from django.shortcuts import render
from django.views.generic import View
from product.models import Product
# Create your views here.
class HomeView(View):
      def get(self,request, *args, **kwargs):
            product= Product.objects.all()
            context={
                  'product':product
            }
            return render(request,'home/home.html',context)
