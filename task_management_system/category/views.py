from django.shortcuts import render
from .forms import addCategoryForm

# Create your views here.
def addCategory(req):
    if req.method == "POST":
        form = addCategoryForm(req.POST)
        if form.is_valid():
            form.save()
            form = addCategoryForm()
            return render (req, 'category/add_category.html', {'form': form})

    else:
        form = addCategoryForm()
    return render (req, 'category/add_category.html', {'form': form})