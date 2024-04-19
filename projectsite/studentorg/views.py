

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from studentorg.models import Organization
from studentorg. forms import OrganizationForm
from django.urls import reverse_lazy

template_name = "home.html"

class HomePageView(ListView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')





