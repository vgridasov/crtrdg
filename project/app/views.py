from django.views import generic
from .models import CartridgeModel


class IndexView(generic.ListView):
    template_name = 'app/home.html'
    context_object_name = 'latest_object_list'

    def get_queryset(self):
        return CartridgeModel.objects.order_by('-reg_date')[:10]
