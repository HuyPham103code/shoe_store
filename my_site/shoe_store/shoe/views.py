from django.shortcuts import render
from django.http import request, HttpResponse
from .models import Shoe
import random
from django.db.models import Q





def wife(request):
    return HttpResponse('Hello')


#trả về random 20 items, khi tải trang user
def home(request):
    # Get the total number of Shoe objects in the database
    total_shoes = Shoe.objects.count()

    #random 20 id 
    list_id = random.sample(range(2, total_shoes + 1), 20)

    #get shoe from list id
    list_shoe = Shoe.objects.filter(pk__in=list_id)
    return render(request, 'shoe/home.html', {'list_shoe': list_shoe})

#render by search
def search_category(request):
    search = request.POST.get('search')
    print(search)
    list_shoe = Shoe.objects.filter(Q(category__icontains=search) | Q(title__icontains=search))
    return render(request, 'shoe/home.html', {'list_shoe': list_shoe})

#show category
def show_category(request, category):
    list_shoe = Shoe.objects.filter(category__icontains=category)
    print(category)
    return render(request, 'shoe/home.html', {'list_shoe': list_shoe})


#search each shoe
def show_shoe(request, id):
    print(id)

    #get shoe with id
    shoe = Shoe.objects.get(pk=id)
    print(shoe)
    #get another shoe with the same category
    list_shoe = Shoe.objects.filter(category=shoe.category)
    print(list_shoe.__len__())

    response = {
        'shoe': shoe,
        'list_shoe': list_shoe
    }
    return render(request, 'shoe/details.html', response)
