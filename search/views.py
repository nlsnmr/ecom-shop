from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Create your views here.
class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        # print(request.GET)
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return not Product.objects.featured()