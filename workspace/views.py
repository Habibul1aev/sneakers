from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from sneakers.models import Sneakers
from workspace.forms import SneakersForm
from django.contrib import messages


def main(request):
    sneakers = Sneakers.objects.all().order_by('code')

    paginator = Paginator(sneakers, 6)
    page_number = request.GET.get('page')
    sneakers = paginator.get_page(page_number)

    return render(request, 'workspace/body.html', {'sneakers': sneakers})



def creatSneakers(req):
    form = SneakersForm() 
    if req.method == 'POST':
        form = SneakersForm(data=req.POST, files=req.FILES) 
        if form.is_valid(): 
            sneakers = form.save()

            messages.success(req, f'The {sneakers.name} sucsesfuliy creat')


        return redirect('/workspace/')

    return render(req, 'workspace/creat.html', {'form': form})


def updateSneakers(req,id):
    sneakers = get_object_or_404(Sneakers, id=id) 
    
    if req.method == "POST":
        form = SneakersForm(data=req.POST, files=req.FILES, instance=sneakers)

        if form.is_valid():
            sneakers = form.save()
            messages.success(req, f'The {sneakers.name} sucsesfuliy update')
        return redirect('/workspace/')
    
    else:
        form = SneakersForm(instance=sneakers)

    return render(req, 'workspace/update.html', {'form': form, 'sneakers':sneakers})


def delete(req, id):
    sneakers = Sneakers.objects.get(id=id)
    name = sneakers.name
    sneakers.delete()
    messages.success(req, f'The {name} sucsesfuliy deleted')

    return redirect('/workspace/')