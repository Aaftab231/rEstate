from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from listings.choices import bedroom_choices, price_choices, state_choices
from .models import Listing


def lists(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listings = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listings
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    query_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__iexact=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)


    context = {
        'listings': query_list,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
