from django.shortcuts import render
from django.core.paginator import Paginator
from sneakers.models import Sneakers, Size, Category, Color, Seazon, CategorySneakers, Brends, ImgAttribute

def main(req):
    sneakers = Sneakers.objects.all()[0:4]
    search = req.GET.get('search')
    if search:
        sneakers = sneakers.filter(name__icontains=search)

    category_list = Category.objects.all()
    return render(req, 'body.html', {'sneakers':sneakers, 'category_list': category_list})

def categor_elements(req, id):
    sneaker = Sneakers.objects.get(id=id)
    sneakers = Sneakers.objects.all()
    sneakers_size = Size.objects.all()
    sneaker_seazon = Seazon.objects.all()
    category_list = Category.objects.all()
    color_list = Color.objects.all()
    category_sneakers_list = CategorySneakers.objects.all()
    brends_list = Brends.objects.all()


    size = req.GET.get('size')
    if size:
        sneakers = sneakers.filter(size__id=int(size))
    sezon = req.GET.get('sezon')
    if sezon:
        sneakers = sneakers.filter(seazon__id=int(sezon))
    color = req.GET.get('color')
    if color:
        sneakers = sneakers.filter(color__id=int(color))
    categorySne = req.GET.get('categoryShe')
    if categorySne:
        sneakers = sneakers.filter(category_sneakers__id=int(categorySne))
    brend = req.GET.get('brend')
    if brend:
        sneakers = sneakers.filter(brends__id=int(brend))


    search = req.GET.get('search')
    if search:
        sneakers = sneakers.filter(name__icontains=search)

    paginator = Paginator(sneakers, 6)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    if id == 1:
        return render(req, 'sneakers.html', {'sneakers':sneakers,'sneakers_size':sneakers_size, 'category_list': category_list, 'sneaker':sneaker,'sneaker_seazon':sneaker_seazon, 'color_list':color_list, 'category_sneakers_list':category_sneakers_list, 'brends_list':brends_list, 'page_obj':page_obj})
    elif id == 2:
        return render(req, 'odejda.html', {'sneakers':sneakers,'sneakers_size':sneakers_size, 'category_list': category_list, 'sneaker':sneaker,'sneaker_seazon':sneaker_seazon, 'color_list':color_list, 'category_sneakers_list':category_sneakers_list, 'brends_list':brends_list, 'page_obj':page_obj})
    elif id == 3:
        return render(req, 'acsesuar.html', {'sneakers':sneakers,'sneakers_size':sneakers_size, 'category_list': category_list, 'sneaker':sneaker,'sneaker_seazon':sneaker_seazon, 'color_list':color_list, 'category_sneakers_list':category_sneakers_list, 'brends_list':brends_list, 'page_obj':page_obj})

    return render(req, 'base.html', {'sneakers':sneakers,'sneakers_size':sneakers_size, 'category_list': category_list, 'sneaker':sneaker,'sneaker_seazon':sneaker_seazon, 'color_list':color_list, 'category_sneakers_list':category_sneakers_list, 'brends_list':brends_list, 'page_obj':page_obj})


def detail_news(req, id):
    sneakers = Sneakers.objects.get(id=id)
    sneakerss = Sneakers.objects.all()[0:4]
    img = sneakers.images.all()

    return render(req, 'detail_news.html',{'sneakers':sneakers, 'sneakerss':sneakerss, 'img':img} )


def profile(request):

    return render(request, 'profile.html')