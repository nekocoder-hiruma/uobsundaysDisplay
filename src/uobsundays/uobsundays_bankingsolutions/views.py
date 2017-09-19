from django.views.generic import ListView
from uobsundays_bankingsolutions.models import BankingSolutionsImage

class BankingSolutionsListView(ListView):
    template_name = 'uobsundays_bankingsolutions/bankingsolutions.html'
    model = BankingSolutionsImage
    context_object_name = 'images'
    paginate_by = 8
    queryset = BankingSolutionsImage.objects.order_by('-created')
