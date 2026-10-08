from django.shortcuts import render
from .models import Job, JobApplication


def job_list(request):

    search = request.GET.get("search")

    if search:
        jobs = Job.objects.filter(
            title__icontains=search
        )
    else:
        jobs = Job.objects.all()

    return render(
        request,
        "job_list.html",
        {
            "jobs": jobs,
            "search": search
        }
    )


def job_detail(request, id):
    job = Job.objects.get(id=id)
    return render(request, "job_detail.html", {"job": job})


def apply_job(request, id):
    job = Job.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        resume = request.FILES.get("resume")
        cover_letter = request.POST.get("cover_letter")

        JobApplication.objects.create(
            job=job,
            name=name,
            email=email,
            phone=phone,
            resume=resume,
            cover_letter=cover_letter
        )

        return render(
            request,
            "application_success.html",
            {"job": job}
        )

    return render(
        request,
        "apply_job.html",
        {"job": job}
    )