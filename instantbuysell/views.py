from django.shortcuts import render

# Create your views here.

def instantbuysell_buy(request):
    return render(request, 'instantbuysell/instantbuy.html')


def instantbuysell_sell(request):
    return render(request, 'instantbuysell/instantsell.html')