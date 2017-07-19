from django.shortcuts import render, redirect
import datetime
import random
import string 
# Create your views here.

def index(request):

    if "gold" in request.session:
        request.session["gold"] += 0
    else:
        request.session["gold"] = 0

    if 'messages' in request.session:
        pass
    else:
        request.session["messages"] = []
    return render(request, 'ninja/index.html')

def process(request):

    now = datetime.datetime.now()
    date_object = now.strftime('%Y/%m/%d %I:%M%p')
    random.randrange(0,2)

    if request.POST['place'] == 'farm':
        goldcoin = random.randrange(10,21)
        stringval = ''.join(["You have earned", str(goldcoin) , "gold." , str(date_object)])
        request.session['messages'].append(stringval)
        request.session['gold'] += goldcoin
        

    if request.POST['place'] == 'cave':
        goldcoin = random.randrange(5,11)
        stringval = ''.join(["You have earned", str(goldcoin) , "gold.", str(date_object)])
        request.session['messages'].append(stringval)
        request.session['gold'] += goldcoin
        

    if request.POST['place'] == 'house': 
        goldcoin = random.randrange(2,6)
        stringval = ''.join(["You have earned", str(goldcoin) , "gold.", str(date_object)])
        request.session['messages'].append(stringval)
        request.session['gold'] += goldcoin
        

    if request.POST['place'] == 'casino':
        goldcoin = random.randrange(-50,51)
        request.session['gold'] += goldcoin
        if goldcoin < 0:
            stringval = ''.join(["You have loses", str(goldcoin) , "gold." , str(date_object)])
            request.session['messages'].append(stringval)
        else:
            stringval = ''.join(["You have earned" , str(goldcoin) , "gold." , str(date_object)])
            request.session['messages'].append(stringval)

    return redirect('/')

def reset(request):
    
    if 'reset' not in request.session:
        request.session['gold'] = 0
        request.session.pop['messages'] 

    return redirect('/')

