from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from .forms import SignUpForm, ProductForm, CategoryForm
from . models import *
# Create your views here.

def Homeview(request):
    return render(request, 'crudapp/base.html')

def Register_view(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'User created successfully.!!!!')
    else:
        fm = SignUpForm()
    return render(request, 'crudapp/register.html', {'form': fm})

# login fuctionality
def Login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pword = fm.cleaned_data['password']
                user = authenticate(username=uname, password=pword)
                if user is not None:
                    login(request, user)
                    if request.user.is_superuser:
                        return redirect('admin_view')
                    else:
                        return redirect('view_product')
            else:
                messages.success(request, 'User Does\'t Exist first Complete your Registration Please!!!!')
                return redirect('register')
        else:
            fm = AuthenticationForm()
            return render(request, 'crudapp/login.html', {'form': fm})
    else:
        return redirect('product_view')

# Admin view product by filter
def Admin_view(request):
    if request.user.is_authenticated:
        products = None
        categories = Category.get_all_categories()
        categoryId = request.GET.get('category')
        if categoryId:
            products = Product.get_all_products_by_category_id(categoryId)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request, 'crudapp/admin_view.html', data)
    else:
        return redirect('login')

# admin view product by search
def Admin_search(request):
    search = request.POST.get('search')
    products = Product.objects.filter(product_name=search)
    return render(request, 'crudapp/admin_view.html', {'prod':products})


# user will create Product
def Add_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ProductForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                return redirect('view_product')
        else:
            fm = ProductForm()
        return render(request, 'crudapp/add_product.html', {'form': fm})
    else:
        return redirect('login')

# user view all his own product
def View_product(request):
    user = request.user
    products = Product.objects.filter(user__id=user.id)
    return render(request, 'crudapp/display_product.html', {'products': products})

# user will update question
def Update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'crudapp/update_product.html', {'form': form})
    else:
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_product')

# user can delete product
def Delete_Product(request, id):
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect('view_product')

# user will create category
def Add_category(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = CategoryForm(request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('view_category')
        else:
            fm = CategoryForm()
            return render(request, 'crudapp/add_category.html', {'form': fm})
    else:
        return redirect('login')

# user display category
def View_category(request):
    categories = Category.objects.all()
    return render(request, 'crudapp/view_category.html', {'categories': categories})

# user can update category
def Update_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'GET':
        form = CategoryForm(instance=category)
        return render(request, 'crudapp/update_category.html', {'form': form})
    else:
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('view_category')

# user can delete product
def Delete_category(request, id):
    obj = Category.objects.get(id=id)
    obj.delete()
    return redirect('view_category')

#logout
def Logout_view(request):
    logout(request)
    return redirect('login')
