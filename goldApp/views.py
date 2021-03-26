from django.shortcuts import render, redirect
import random
from datetime import datetime

# helper dictionary, for easy access to min/max gold values
GOLD_MAP = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (0,50)
}

# Create your views here.
def index(request):
    # check if either 'gold' or 'activities' keys are not in session (yet)
    if not "gold" in request.session or "activities" not in request.session:
        # set these to initial values if that is the case!
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def reset(request):
    request.session.clear()
    return redirect('/')

def process_gold(request):
    if request.method == 'GET':
        return redirect('/')

    building_name = request.POST['building']
    #building name = "Farm" for ex.

    min = 0
    max = 50
    if building_name == "Farm":
        min = 10
        max = 20
    elif building_name == "Cave":
        min = 5
        max = 10
    elif building_name == "House":
        min = 2
        max = 5
    elif building_name == "Casino":
        min = 0
        max = 50

    # access the correct mix/max values from the user's form submission
    building = GOLD_MAP[building_name]
    # upper case string (for message)
    building_name_upper = building_name[0].upper() + building_name[1:] 

    # calculate the correct random number for this building
    curr_gold = random.randint(min, max)

    # generate a datetime string, with the proper format, for RIGHT NOW
    time_stamp = datetime.now().strftime("%m/%d/%Y %I:%M%p")

    # for formatting message color! (this will correspond to a css class)
    result = 'earn'


    message = f"Earned {curr_gold} from the {building_name_upper}! ({time_stamp})"

    # check if we need to do casino stuff
    if building_name == 'Casino':
        # if so, see if we lost money
        if random.randint(0,1) > 0: # 50% chance of being True/False
            # if we lost money, we need a different message!
            message = f"Entered a {building_name_upper} and lost {curr_gold} golds... Ouch... ({time_stamp})"
            # we also need to convert our turn's gold amount to a negative number
            curr_gold = curr_gold * -1
            result = 'lose'

    # update session gold value
    request.session['gold'] += curr_gold
    # update session activities with new message
    # NOTE: each 'activity' is a dictionary, with the message as well as the 'result' for css purposes
    request.session['activities'].append({"message": message, "result": result})
    return redirect('/')
    
# def index(request):
#     if 'total_gold' not in request.session or 'activities' not in request.session:
#         request.session['total_gold'] = 0
#     request.session['activities'] = []
#     return render(request, "index.html")

# def process(request):
#     if request.method == 'POST':
#         if request.POST['location'] =='farm':
#             gold = random.randint(10,21)
#             request.session['activites'].append('You earned' + str(gold) + 'gold from' + request.POST['location'] + '' + '(' + str(datetime.now().localtime('%Y-%m-%d H:%M'))+')')
#         elif request.POST['location'] == 'cave':
#             gold = random.randint(5,11)
#             request.session['activites'].append('You earned' + str(gold) + 'gold from' + request.POST['location'] + '' + '(' + str(datetime.now().localtime('%Y-%m-%d H:%M'))+')')
#         elif request.POST['location'] == 'house':
#             gold = random.randint(5,11)
#             request.session['activites'].append('You earned' + str(gold) + 'gold from' + request.POST['location'] + '' + '(' + str(datetime.now().localtime('%Y-%m-%d H:%M'))+')')
#         elif request.POST['location'] == 'casino':
#             gold = random.randint(-50,51)
#             if gold > 0:
#                 request.session['activites'].append('You earned' + str(gold) + 'gold from' + request.POST['location'] + '' + '(' + str(datetime.now().localtime('%Y-%m-%d H:%M'))+')')
#             else:
#                 request.session['activites'].append('Entered casino and lost' + str(gold) + 'gold...Ouch' + '' + '(' + str(datetime.now().localtime('%Y-%m-%d H:%M'))+')')
#         request.session['total_gold'] += gold

#     return redirect('/')

# def reset(request):
#     request.session.flush()
#     return redirect('/')


# def index(request):
#     context = {
#         "time": strftime("%Y-%m-%d %H:%M %p", localtime())
#     }
#     return render(request,'index.html', context)


    # get this to push all form submissions to actitivies
# Create your views here.
