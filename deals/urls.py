from django.urls import path

from . import views

app_name = 'deals'

urlpatterns = [
    path('group/<slug:slug>/',
         views.group_deals,
         name='group_deals'),
    path('',
         views.index,
         name='index'),
    path('new/',
         views.new_deal,
         name='new_deal'),
    path('deal/<int:deal_id>/',
         views.view_deal,
         name='view_deal'),
    path('deal/<int:deal_id>/edit/',
         views.edit_deal,
         name='edit_deal'),
    path('404/',
         views.page_not_found,
         name='page_not_found'),
    path('500/',
         views.server_error,
         name='server_error'),
    path('deal/<int:deal_id>/sub_deal/',
         views.add_sub_deal,
         name='add_sub_deal'),
    path('deal/<int:deal_id>/sub_deal/<int:sub_deal_id>/done/',
         views.done_sub_deal,
         name='done_sub_deal'),
    path('deal/<int:deal_id>/done/',
         views.done_deal,
         name='done_deal'),
    path('deal/<int:deal_id>/undone/',
         views.undone_deal,
         name='undone_deal'),
    path("done/",
         views.index_done,
         name="index_done"),
]
