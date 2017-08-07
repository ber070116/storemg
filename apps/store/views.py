from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *


class StoreListView(ListView):
    """View to stores list"""
    template_name = 'store/index.html'
    context_object_name = 'stores'

    def get_queryset(self):
        """Get stores from user"""
        user = self.request.user
        queryset = user.stores_set.all()

        return queryset
