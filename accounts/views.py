from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    return render(request, "home.html")


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        else:
            return render(
                request,
                "login.html",
                {"error": "Invalid username or password"}
            )

    return render(request, "login.html")


@login_required(login_url="login")
def dashboard(request):

    basic_score = request.session.get("basic_score", 0)
    technical_score = request.session.get("technical_score", 0)
    interview_score = request.session.get("interview_score", 0)

    return render(
        request,
        "dashboard.html",
        {
            "user": request.user,
            "basic_score": basic_score,
            "technical_score": technical_score,
            "interview_score": interview_score,
        }
    )

def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "register.html",
                {"error": "Username already exists"}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "register.html")


@login_required(login_url="login")
def basic_test(request):

    if request.method == "POST":

        score = 0

        if request.POST.get("q1") == "Python":
            score += 1

        if request.POST.get("q2") == "MySQL":
            score += 1

        if request.POST.get("q3") == "Create Read Update Delete":
            score += 1

        if request.POST.get("q4") == "a":
            score += 1

        if request.POST.get("q5") == "def":
            score += 1

        request.session["basic_score"] = score

        return render(
            request,
            "basic_test_result.html",
            {"score": score}
        )

    return render(request, "basic_test.html")



@login_required(login_url="login")
def communication_assessment(request):

    if request.method == "POST":

        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")
        q4 = request.POST.get("q4")
        q5 = request.POST.get("q5")

        return render(
            request,
            "communication_result.html",
            {
                "q1": q1,
                "q2": q2,
                "q3": q3,
                "q4": q4,
                "q5": q5
            }
        )

    return render(
        request,
        "communication_assessment.html"
    )


@login_required(login_url="login")
def team_discussion(request):

    if request.method == "POST":

        topic = request.POST.get("topic")
        response = request.POST.get("response")

        return render(
            request,
            "team_discussion_result.html",
            {
                "topic": topic,
                "response": response
            }
        )

    return render(
        request,
        "team_discussion.html"
    )



@login_required(login_url="login")
def technical_assessment(request):


    if request.method == "POST":

        score = 0

        if request.POST.get("q1") == "Python":
            score += 1

        if request.POST.get("q2") == "Django":
            score += 1

        if request.POST.get("q3") == "MySQL":
            score += 1

        if request.POST.get("q4") == "SELECT":
            score += 1

        if request.POST.get("q5") == "def":
            score += 1

        # Save Technical Assessment score
        request.session["technical_score"] = score

        return render(
            request,
            "technical_result.html",
            {"score": score}
        )

    return render(
        request,
        "technical_assessment.html"
    )


@login_required(login_url="login")
def interview_readiness(request):

    if request.method == "POST":

        score = 0

        if request.POST.get("q1") == "yes":
            score += 1

        if request.POST.get("q2") == "yes":
            score += 1

        if request.POST.get("q3") == "yes":
            score += 1

        if request.POST.get("q4") == "yes":
            score += 1

        if request.POST.get("q5") == "yes":
            score += 1

        # Save Interview Readiness score
        request.session["interview_score"] = score

        return render(
            request,
            "interview_readiness_result.html",
            {"score": score}
        )

    return render(
        request,
        "interview_readiness.html"
    )



@login_required(login_url="login")
def final_result(request):

    basic_score = request.session.get("basic_score", 0)
    technical_score = request.session.get("technical_score", 0)
    interview_score = request.session.get("interview_score", 0)

    overall_score = (
        (basic_score / 5) * 30
        + (technical_score / 5) * 40
        + (interview_score / 5) * 30
    )

    return render(
        request,
        "final_result.html",
        {
            "basic_score": basic_score,
            "technical_score": technical_score,
            "interview_score": interview_score,
            "overall_score": overall_score
        }
    )