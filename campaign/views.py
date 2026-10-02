from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    if "player_name" not in request.session:
        return redirect("welcome")
    
    player_name = request.session.get("player_name", "Adventurer")
    xp = request.session.get("xp", 0)
    level = request.session.get("level",1)


    context = {
        "campaign_name": "Echoes of Elarion",
        "player_name": player_name,
        "xp": xp,
        "level":level
    }

    return render(request, "campaign/home.html",context)

def history(request):
    level = request.session.get("level",1)

    if level < 2:
        return redirect("home")

    player_name = request.session.get("player_name", "Adventurer")
    xp = request.session.get("xp", 0)

    context = {
        "player_name": player_name,
        "xp":xp,
        "level":level,

    }
    return render(request, "campaign/history.html", context)

def welcome(request):
    if request.method == "POST":
        name = request.POST.get("name")

        request.session["player_name"] = name
        request.session["xp"] = 0
        request.session["level"] = 1
        request.session["explored_lore"] = []
        

        return redirect("home")

    return render(request, "campaign/welcome.html")