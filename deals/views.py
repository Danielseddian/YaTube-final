from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DealForm, SubDealForm
from .models import Deal, Group, SubDeal
from .settings import DEALS_COUNT, DONE, NOT_DONE


def server_error(request):
    return render(request, 'misc/500.html', status=500)


def page_not_found(request, exception):
    return render(request,
                  'misc/404.html',
                  {"path": request.path},
                  status=404)


@login_required
def index(request):
    deals = Deal.objects.filter(author=request.user, status=NOT_DONE)
    paginator = Paginator(deals, DEALS_COUNT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {
        'page': page,
        'deals': deals,
        'NOT_DONE': NOT_DONE,
        'DONE': DONE,
    })


@login_required
def index_done(request):
    deals = Deal.objects.filter(author=request.user, status=DONE)
    paginator = Paginator(deals, DEALS_COUNT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'done.html', {
        'page': page,
        'NOT_DONE': NOT_DONE,
        'DONE': DONE,
    })


@login_required
def group_deals(request, slug):
    group = get_object_or_404(Group, slug=slug)
    deals = Deal.objects.filter(author=request.user, group=group)
    paginator = Paginator(deals, DEALS_COUNT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'group.html', {
        'group': group,
        'page': page,
        'NOT_DONE': NOT_DONE,
        'DONE': DONE,
    })


@login_required
def new_deal(request):
    form = DealForm(request.POST or None, files=request.FILES or None)
    if not form.is_valid():
        return render(request, 'new.html', {'form': form})
    new_deal = form.save(commit=False)
    new_deal.author = request.user
    new_deal.save()
    return redirect('deals:index')


@login_required
def view_deal(request, deal_id):
    deal = get_object_or_404(Deal, author=request.user, id=deal_id)
    sub_deals = SubDeal.objects.filter(author=request.user,
                                       deal__id=deal_id)
    paginator = Paginator(sub_deals, DEALS_COUNT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    form = SubDealForm(request.POST or None)
    return render(request, 'deal.html', {'deal': deal,
                                         'page': page,
                                         'form': form,
                                         'NOT_DONE': NOT_DONE,
                                         'DONE': DONE, })


@login_required
def edit_deal(request, deal_id):
    deal = get_object_or_404(Deal, author=request.user,
                             id=deal_id)
    form = DealForm(request.POST or None, files=request.FILES or None,
                    instance=deal)
    if not form.is_valid():
        return render(request, 'new.html', {'form': form, 'deal': deal})
    form.save()
    return redirect('deals:index')


@login_required
def add_sub_deal(request, deal_id):
    deal = get_object_or_404(Deal, author=request.user, id=deal_id)
    form = SubDealForm(request.POST or None)
    paginator = Paginator(deal.sub_deals.all(), DEALS_COUNT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    if not form.is_valid():
        return render(request, 'deal.html', {'form': form,
                                             'deal': deal,
                                             'page': page,
                                             'NOT_DONE': NOT_DONE,
                                             'DONE': DONE, })
    new_deal = form.save(commit=False)
    new_deal.author = request.user
    new_deal.deal = deal
    new_deal.save()
    return redirect('deals:view_deal', deal_id=deal_id)


@login_required
def edit_sub_deal(request, deal_id):
    deal = get_object_or_404(SubDeal, author=request.user,
                             id=deal_id)
    form = DealForm(request.POST or None, files=request.FILES or None,
                    instance=deal)
    if not form.is_valid():
        return render(request, 'new.html', {'form': form, 'deal': deal})
    form.save()
    return redirect('deals:view_deal', deal_id=deal_id)


@login_required
def done_sub_deal(request, deal_id, sub_deal_id):
    sub_deal = get_object_or_404(SubDeal, author=request.user, deal__id=deal_id,
                                 id=sub_deal_id)
    form = SubDealForm(request.POST or None, instance=sub_deal)
    done_sub_deal = form.save(commit=False)
    done_sub_deal.status = DONE
    done_sub_deal.save()
    return redirect('deals:view_deal', deal_id=deal_id)


@login_required
def done_deal(request, deal_id):
    deal = get_object_or_404(Deal, author=request.user, id=deal_id)
    form = DealForm(request.POST or None, instance=deal)
    done_deal = form.save(commit=False)
    done_deal.status = DONE
    done_deal.save()
    return redirect('deals:index')


@login_required
def undone_deal(request, deal_id):
    deal = get_object_or_404(Deal, author=request.user, id=deal_id)
    form = DealForm(request.POST or None, instance=deal)
    done_deal = form.save(commit=False)
    done_deal.status = NOT_DONE
    done_deal.save()
    return redirect('deals:index')


'''def profile(request, username):
    author = get_object_or_404(User, username=username)
    paginator = Paginator(author.deals.all(), DEALS_COUNT)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    following = Follow.objects.filter(user__username=request.user.username,
                                      author=author).exists()
    return render(request, 'profile.html', {'page': page,
                                            'author': author,
                                            'following': following})'''
