from django.shortcuts import render, redirect
from .models import Show


def root(request):
    return redirect('/shows')


def index(request):
    context = {
        'shows': Show.objects.all(),
    }

    return render(request, "index.html", context)


def show(request, show_id):
    curr_show = Show.objects.get(id=show_id)
    print(curr_show.release_date, "desde DDBB")
    context = {
        'show': curr_show,
    }

    return render(request, "show.html", context)


def new_template(request):
    return render(request, "new.html")


def add_new(request):
    new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
    return redirect(f"/shows/{new_show.id}")


def edit(request, show_id):
    curr_show = Show.objects.get(id=show_id)
    release_date = curr_show.release_date.strftime("%Y-%m-%d")

    context = {
        'show': curr_show,
        'release_date': release_date
    }
    print(curr_show.desc)
    print(curr_show.release_date)
    return render(request, "edit.html", context)


def update_show(request, show_id):
    curr_show = Show.objects.get(id=show_id)

    curr_show.title = request.POST['title']
    curr_show.network = request.POST['network']
    curr_show.release_date = request.POST['release_date']
    curr_show.desc = request.POST['desc']
    curr_show.save()
    print(request.POST['release_date'], "desde el form")
    return redirect(f"/shows/{curr_show.id}")


def delete(request, show_id):
    curr_show = Show.objects.get(id=show_id)
    curr_show.delete()
    return redirect("/shows")