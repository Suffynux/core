from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def receipes(request):
    if request.method == 'POST':
        data = request.POST
        receipe_img = request.FILES.get('recipe_img')  # Change to 'recipe_img'
        receipe_name = data.get('recipe_name')         # Change to 'recipe_name'
        receipe_description = data.get('recipe_description')  # Change to 'recipe_description'

        Receipe.objects.create(
            receipe_description = receipe_description,
            receipe_img = receipe_img,
            receipe_name = receipe_name
        )
        return(redirect('/receipes/'))
    queryset = Receipe.objects.all()
    context  = {'receipes' : queryset}
    return render ( request, 'receipes.html' , context)

def delete(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')

# This is the update function of our website
def update(request, id):
    \
    queryset = Receipe.objects.get(id= id)
    if request.method == "POST" :

        data = request.POST
        receipe_img = request.FILES.get('recipe_img')  # Change to 'recipe_img'
        receipe_name = data.get('recipe_name')         # Change to 'recipe_name'
        receipe_description = data.get('recipe_description') 
         # Change to 'recipe_description'

        queryset.receipe_img = receipe_img
        queryset.receipe_name = receipe_name
        
        queryset.receipe_img  = receipe_img


        queryset.save()

        return redirect('/receipes/')

    context  = {'receipe' : queryset}
    return render ( request, 'update.html' , context)

    
    return redirect('/receipes/')
 


   