from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import translation
from .models import *
# Create your views here.

def index(request):
    return render(request, "index-11.html")


def blog(request):
    blogs = Blog.objects.all()

    context = {"blogs": blogs}
    return render(request, "blog.html", context)


def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    blogs = Blog.objects.filter(popular=True)

    context = {"blog": blog, "blogs": blogs}
    return render(request, "blog-details.html", context)


def change_lang(request):
    LANGUAGE_SESSION_KEY = '_language'  
    if request.method == "POST":
        sent_url = request.POST['next']
        old_lang = request.LANGUAGE_CODE
        changed_lang = request.POST['language']
        translation.activate(changed_lang)
        request.session[LANGUAGE_SESSION_KEY] = changed_lang
        # I use HTTP_REFERER to direct them back to previous path 
        print(sent_url)
        if "en" in sent_url:
            if changed_lang != 'uz':
                new_url = sent_url.replace('en', changed_lang)
                print(new_url)
                return HttpResponseRedirect(new_url)
            elif changed_lang == 'uz':
                new_url1 = sent_url.replace('en', '')
                new_url = new_url1[1:]
                print(new_url)
                return HttpResponseRedirect(new_url)
        elif "ru" in sent_url:
            if changed_lang != 'uz':
                new_url = sent_url.replace('ru', changed_lang)
                print(new_url)
                return HttpResponseRedirect(new_url)
            elif changed_lang == 'uz':
                new_url1 = sent_url.replace('ru', '')
                new_url = new_url1[1:]
                print(new_url)
                return HttpResponseRedirect(new_url)
        elif old_lang == "uz" and changed_lang != 'uz':
            new_url = f"/{changed_lang}" + sent_url
            print(new_url)

            return HttpResponseRedirect(new_url)
        
        return HttpResponseRedirect(sent_url)