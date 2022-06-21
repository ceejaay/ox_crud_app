from django.shortcuts import render, redirect

from todo_items.models import Item

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/main')
    else:
        items = Item.objects.all()
        return render(request, 'home.html', {"items": items})


def view_list(request):
    items = Item.objects.all()
    return render(request, 'home.html', {"items": items})

# Create your views here.
