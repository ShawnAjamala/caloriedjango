from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import FoodItem
from .forms import FoodItemForm

def index(request):
    today = timezone.now().date()
    items = FoodItem.objects.filter(date_added=today).order_by('-id')
    total_calories = sum(item.calories for item in items)

    if request.method == 'POST':
        if 'add_item' in request.POST:
            form = FoodItemForm(request.POST)
            if form.is_valid():
                food_item = form.save(commit=False)
                food_item.date_added = today
                food_item.save()
                return redirect('calorie_tracker:index')  # <-- added namespace
        elif 'reset_day' in request.POST:
            items.delete()
            return redirect('calorie_tracker:index')      # <-- added namespace
    else:
        form = FoodItemForm()

    context = {
        'items': items,
        'total_calories': total_calories,
        'form': form,
    }
    return render(request, 'index.html', context)

def delete_item(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    item.delete()
    return redirect('calorie_tracker:index')              