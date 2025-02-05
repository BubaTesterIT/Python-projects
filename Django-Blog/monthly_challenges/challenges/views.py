from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges ={
    "january": "Learn Django at least 2 hours a day!!!",
    "february": "Hello, world. It's February!!!",
    "march": "Hello, world. It's March!!!",
    "april": "Hello, world. It's April!!!",
    "may": "Hello, world. It's May!!!",
    "june": "Hello, world. It's June!!!",
    "july": "Hello, world. It's my birthday!!!",
    "august": "Hello, world. It's August!!!",
    "september": None,
    "october": "Hello, world. It's October!!!",
    "november": "Hello, world. It's November!!!",
    "december": "Hello, world. It's Christmas!!!",

}
# Create your views here.

def index(request):

    months = list(monthly_challenges.keys())

    return render(request,
    "challenges/index.html",
    {"months": months,
     }
    )

def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
        return HttpResponseRedirect(redirect_path)  #("/challenges/" + redirect_month)
    except:
        return HttpResponseNotFound("The month is not available")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,
        "challenges/challenge.html",
        {"text": challenge_text,
                "month_name": month,
         },

        )
    except :
        raise Http404()


