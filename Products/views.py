from django.shortcuts import render
from .models import Product,Rating

def home(request):
    product = Product.objects.all()
    rating = Rating.objects.all()
    dict = {}
    for line in rating:
        if dict.get(line.product.productName):
            dict[line.product.productName] = (dict[line.product.productName] + line.rating)/2
        else:
            dict.update({line.product.productName:line.rating})
    
    averageRating = dict
   
    productNameList = []
    for i in product:
        
        productNameList.append(i.productName)
    for j in productNameList:
        # for k in dict
        k= Product.objects.get(productName=j)
        for key,val in dict.items():
            if key == k.productName:
                k.averageRating = val
                k.save()
               # print("name {} k.name {} ".format(key,k.name))
    return render(request,'home.html',{'product':product})