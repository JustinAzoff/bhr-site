from django.views.generic import View, FormView, TemplateView
from django.http import HttpResponse

from bhr.models import WhitelistEntry, Block, BlockEntry, BHRDB
from bhr.forms import AddBlockForm

from django.db import transaction
from django.db.models import Q
from django.utils import timezone
import datetime

from django.db import transaction



class IndexView(TemplateView):
    template_name = "bhr/index.html"

class AddView(FormView):
    template_name = "bhr/add.html"
    form_class = AddBlockForm
    success_url = '/bhr'

    def form_valid(self, form):
        block_request = form.cleaned_data
        block_request['cidr'] = str(block_request['cidr'])
        BHRDB().add_block(who=self.request.user, source='web', **block_request)
        return super(AddView, self).form_valid(form)
