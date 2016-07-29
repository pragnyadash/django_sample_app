from django.shortcuts import *
import logging

def signup(request):
    if request.method == 'POST' and 'login' in request.POST:
        logger = logging.getLogger('upyantra')
        logger.info('login')
        return render(request, 'signup.html', {'show': 1, 'login': 1})

    if request.method == 'POST' and 'buy' in request.POST:
        bought = 0
        for k, v in request.POST.items():
            if 'item_' in k:
                bought+=1
        logger = logging.getLogger('upyantra')
        logger.info('buy, '+ str(bought))
        return render(request, 'signup.html', {'show': 0, 'login': 0})
    return render(request, 'signup.html', {'show': 0})

def welcome(request):
    if request.method == 'POST':
        logger = logging.getLogger('upyantra')
        print(request.POST)
        logger.info('1')
        return render(request, 'welcome.html')
    return render(request, 'welcome.html')