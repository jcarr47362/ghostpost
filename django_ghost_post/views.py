from django.shortcuts import render, HttpResponseRedirect, reverse
from django_ghost_post import models
from django_ghost_post.forms import PostForm

# Create your views here.

def index(request):
    ghostposts = models.BoastRoast.objects.all().order_by('-timeposted')
    return render(request, 'index.html', {'Welcome': "Ghostpost: Roast and Boast", "ghostpost": ghostposts})


def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            models.BoastRoast.objects.create(
                choices=data.get('choices'),
                user_post=data.get('user_post')
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = PostForm()
    return render(request, "generic_form.html", {'form':form})

def boast_view(request):
    boast = models.BoastRoast.objects.all().order_by('-timeposted')
    return render(request, 'boast.html', {"boast": boast})

def roast_view(request):
    roast = models.BoastRoast.objects.all().order_by('-timeposted')
    return render(request, 'roast.html', {"roast": roast})

def upvote_view(request, upvote_id):
    post = models.BoastRoast.objects.filter(id=upvote_id).first()
    post.upvote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def downvote_view(request, downvote_id):
    post = models.BoastRoast.objects.filter(id=downvote_id).first()
    post.downvote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def sort_by_votes(request):
    sorted_votes = sorted(models.BoastRoast.objects.all(), key=lambda x: x.votes, reverse=True)
    return render(request, "sortbyvote.html", {"sorted_votes": sorted_votes})


