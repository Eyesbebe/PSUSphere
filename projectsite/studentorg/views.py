

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from studentorg.models import Organization
from studentorg. forms import OrganizationForm
from django.urls import reverse_lazy

template_name = "home.html"

class OrganizationListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginated_by = 5





