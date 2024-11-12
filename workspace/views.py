from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from sneakers.models import Sneakers
from workspace.forms import SneakersForm, LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


def main(request):
    sneakers = Sneakers.objects.filter().order_by('code')

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

def login_profile(request):
         
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user')
            password = form.cleaned_data.get('password')
            user1 = authenticate(username=username,password=password)
            print(username)
            print(password)
            
            if user1:
                login(request, user1)
                messages.success(request, 'Successful entrance')
                return redirect('/workspace/')
            
        messages.error(request, 'Account not found')
   
    return render(request, 'auth/login.html', {'form':form})


def logout_profile(request):

    if request.user.is_authenticated:
        logout(request)

    return redirect('/profile/')


def regist_profile(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались )')
            return redirect('/sneakers/')
        
    return render(request, 'auth/register.html', {'form': form})
