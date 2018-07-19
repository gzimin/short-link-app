from django.shortcuts import render
from .forms import ShortLinkForm, SourceLinkForm
from . import shortener
from  shortlink.models import Link

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
                        source_url = Link.objects.get(source_url=form_short['source_url'].value())
                        print(source_url)
                        short_url = source_url.get_short_url()
                        print(short_url)
                        return render(request, 'shortlink/index.html',
                        {'short_url': short_url,
                         'form_short': form_short,
                         'form_source': form_source,})
                    # If there is no short url, create it
                    except:
                        # Check if source url format is OK
                        source_url = form_short['source_url'].value()
                        if shortener.check_url(source_url):
                            short_url = shortener.generate_random_link()
                            post = form_short.save(commit=False)
                            post.short_url = short_url
                            post.save()
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
