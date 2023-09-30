from django.shortcuts import render

# Create your views here.
def home(request):
    peoples = [
        {
            'name': 'John',
            'age': 21,
        },
        {
            'name': 'Sufi',
            'age': 21,
        },
        {
            'name': 'Hello',
            'age': 15,
        },
        {
            'name': 'Lira',
            'age': 21,
        },
        {
            'name': 'Rizwan',
            'age': 10,
        },
        {
            'name': 'Hira',
            'age': 8,
        },
        {
            'name': 'Asad',
            'age': 18,
        },
    ]

    text = "Hello this is Hira and Asad. Good to see you."

    context = {
        'peoples': peoples,
        'text': text,
    }
    return render(request, "index.html", context=context)

def about(request):

     return render(request, "about.html")
def contact(request):

     return render(request, "contact.html")
