from django.shortcuts import render
from django.http import HttpResponse
#dummydata
pictures = [
    {
        'picture': 'Insert Image file here',
        'title':  'This is what the painting means', 
        'artist': 'Tala',
        'date_posted': 'june 12, 1999'

    }
]





# Views Rendered
def home(request):
    context = {
        'pictures': pictures
    }
    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html')