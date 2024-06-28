from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination , Gallery


# Create your views here.

def index(request):
    data = Destination.objects.all()
    gallery_data = Gallery.objects.all()
    # obj1 = Destination()
    # obj1.title1 = "The Shooting Star "
    # obj1.desc1 = "Welcome to the award-winning sustainable travel blog. For over a decade, I’ve been telling stories at the intersection of travel, the environment and local communities. This journey has taken me as far within as with my feet."
    # obj1.img = "statics/images/gallery/banner.img"
    #
    # obj2 = Destination()
    # obj2.title2 = "Mumbai"
    # obj2.desc2 = "Mumbai, formerly known as Bombay, is a vibrant and bustling metropolis nestled on the western coast of India. As the financial capital of the country, Mumbai is renowned for its fast-paced lifestyle, towering skyscrapers, and vibrant street markets. With a population of over 20 million people, Mumbai is a melting pot of cultures, languages, and traditions. From iconic landmarks like the Gateway of India to the famous Marine Drive, this city offers a blend of history, culture, and modernity."
    # obj2.img = "statics/images/gallery/banner.img"
    #
    # obj3 = Destination()
    # obj3.title3 = 'Goa'
    # obj3.desc3 = "A small state on India's western coast, Goa has always benefitted as a trade centre because of its easily accessible ports. With a beautiful harmonization of the East and West, Goans have taken the best of both worlds. A civilization of warm, happy people, Goa sees a mix of different religions like Christians, Catholics, Muslims, and Hindus that live together in harmony. Following their age-old traditions and customs, Goan's celebrate all major festivals with fervour without bringing any religious barriers within the society."
    # obj3.img = "statics/images/gallery/banner.img"
    #
    # obj4 = Destination()
    # obj4.title4 = 'Himachal Pradesh'
    # obj4.desc4 = "The state of Himachal Pradesh, which lies in the Lower Himalayas Range, is a cultural cocktail, and a haven for nature lovers and adventure enthusiasts. There are many interesting facts about this state which most people are not aware of. Read on to find out 100 interesting facts about Himachal Pradesh."
    # obj4.img = "statics/images/gallery/banner.img"
    # data = [obj3,obj4,obj1,obj2]

    context = {
        'data': data,
        'gallery_data': gallery_data,
    }
    return render(request, 'index.html',context )

def register(request):
    return render(request, 'register.html')

# def intro(request):
#     return render(request, 'intro.html')

