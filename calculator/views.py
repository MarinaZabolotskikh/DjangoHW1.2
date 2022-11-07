from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'charlotte': {
        'яблоки, шт': 4,
        'яйца, шт': 4,
        'мука, ст': 1,
        'сахар, ст': 1,
    },
}
def list_recipes(request):
    context = {
       'recipe': list(DATA.keys())
    }
    return render(request, 'home/home.html', context)

def get_dish(request, dish_name):
    if dish_name in DATA:
        list_dish = DATA[dish_name]
        servings = request.GET.get('servings', None)
        if servings:
            quantity_ingredients = {}
            for ing, quan in list_dish.items():
                quantity = quan * int(servings)
                quantity_ingredients[ing] = quantity
            context = {
                'dish_name': dish_name,
                'recipe': quantity_ingredients
                }
        else:
            context = {
                'dish_name': dish_name,
                'recipe': list_dish
                }
    else:
        context = None

    return render(request, 'calculator/index.html', context)


