from django.shortcuts import render, redirect
from .forms import ShortLinkForm, SourceLinkForm
from . import shortener
from  shortlink.models import Link
from django.http import Http404, HttpRequest, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def main(request):
    form_short = ShortLinkForm()
    form_source = SourceLinkForm()
    if request.method == "POST":
            form_short = ShortLinkForm(request.POST)
            form_source = SourceLinkForm(request.POST)
            if 'form_short' in request.POST:
                if form_short.is_valid():
                    try:
                        print("Try option")
                        source_url = Link.objects.get(source_url=form_short['source_url'].value())
                        short_url = source_url.get_short_url()
                        print("Try option_21")
                        return render(request, 'shortlink/index.html',
                        {'short_url': short_url,
                         'form_short': form_short,
                         'form_source': form_source,})
                    # If there is no short url, create it
                    except Link.DoesNotExist:
                        print("Except option")
                        # Check if source url format is OK
                        source_url = form_short['source_url'].value()
                        print("Line_30")
                        if shortener.check_url(source_url):
                            print("Before we get here_line31")
                            short_url = shortener.generate_random_link()
                            # Check that random generated value doesn't exists already
                            print("Before we get here_line34")
                            print("Before we get here_line38")
                            short_url = shortener.generate_random_link()
                            url = form_short.save(commit=False)
                            url.short_url = short_url
                            url.save()
                            print("URL was saved!")
                            return render(request, 'shortlink/index.html',
                            {'short_url': short_url,
                             'form_short': form_short,
                             'form_source': form_source,})
                        else:
                            err_msg = True
                            return render(request, 'shortlink/index.html',
                            {'form_short': form_short,
                             'form_source': form_source,
                             'err_msg': err_msg})

            elif 'form_source' in request.POST:
                if form_source.is_valid():
                    try:
                        Link.objects.get(short_url=form_source['short_url'].value())
                        source_url = Link.objects.get(short_url=form_source['short_url'].value())
                        return render(request, 'shortlink/index.html',
                        {'form_short': form_short,
                        'form_source': form_source,
                        'source_url': source_url})
                    except:
                        no_url = True
                        return render(request, 'shortlink/index.html',
                        {'form_short': form_short,
                        'form_source': form_source,
                        'no_url': no_url})

    else:
        return render(request, 'shortlink/index.html',
            {'form_short': form_short,
            'form_source': form_source})

def link(request):
    try:
        data = request.get_full_path()[1:]
        curr_object = Link.objects.get(short_url=data)
        source_link = str(curr_object)
        return redirect(source_link)
    except:
        raise Http404("Page doesn't exists")
