from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, View, UpdateView, DeleteView, ListView
from forms import ContactGroupForm
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from models import ContactGroup
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

PAGE_SIZE = 25

# Create your views here.

def index(request):
    context = {}
    return render(request, 'web/index.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                HttpResponseRedirect(reverse("index"))

    return render(request, 'web/login.html')

def register(request):
    if (request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']
        #return HttpResponseRedirect("/")

    return render(request, 'web/register.html', None)

@login_required(login_url="/web/login/")
def groups(request):
    email = request.user.username
    return render(request, reverse('groups'), None)


class Login(TemplateView):
    template_name = 'web/login.html'

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                HttpResponseRedirect(reverse("index"))
            else:
                return render(request, self.template_name, {})
        else:
            return render(request, self.template_name, {})


class Logout(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class Index(TemplateView):
    template_name = 'web/index.html'


class Register(TemplateView):
    template_name = 'web/register.html'


class Groups(ListView):
    model = ContactGroup
    template_name = 'web/group_list.html'
    paginate_by = PAGE_SIZE
    context_object_name = 'items'

    def get_query_set(self):
        return ContactGroup.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Groups, self).get_context_data(**kwargs)
        context['text'] = "Some Text for Testing"
        return context

    #def get(self, request, *args, **kwargs):
    #    all_groups = ContactGroup.objects.all()
    #    paginator = Paginator(all_groups, PAGE_SIZE)
    #    page = request.GET('page')
    #    try:
    #        groups = paginator.page(page)
    #    except PageNotAnInteger:
    #        groups = paginator.page(1)
    #    except EmptyPage:
    #        groups = paginator.page(paginator.num_pages)
    #
    #    return render


class GroupCreate(CreateView):
    form_class = ContactGroupForm
    template_name = 'web/group_create.html'
    success_url = reverse_lazy('web:groups')

    def form_valid(self, form):
        form.instance.content_modified = datetime.datetime.utcnow()
        form.instance.thumbnail_modified = datetime.datetime.utcnow()
        return super(GroupCreate, self).form_valid(form)


class GroupUpdate(UpdateView):
    form_class = ContactGroupForm
    model = ContactGroup
    template_name = 'web/group_update.html'
    success_url = reverse_lazy('web:groups')

    def form_valid(self, form):
        if form.has_changed():
            form.instance.content_modified = datetime.datetime.utcnow()
            form.instance.thumbnail_modified = datetime.datetime.utcnow()
            return super(GroupUpdate, self).form_valid(form)
        else:
            return HttpResponseRedirect(self.get_success_url())



class GroupDelete(DeleteView):
    model = ContactGroup
    template_name = 'web/group_delete.html'
    success_url = reverse_lazy('web:groups')

    def get_object(self, queryset=None):
        obj = super(GroupDelete, self).get_object()

        # Check if the current user can delete the object. if not raise exception.

        return obj;

    def get_context_data(self, **kwargs):
        context = super(GroupDelete, self).get_context_data(**kwargs)
        return context


class Group(View):
    template_name = 'web/group.html'

    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(GroupCreate, self).dispatch(*args, **kwargs)



    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            group = get_object_or_404(ContactGroup, pk=kwargs['pk'])
            form = ContactGroupForm(instance=group)
        else:
            form = ContactGroupForm()

        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            group = get_object_or_404(ContactGroup, pk=kwargs['pk'])
            form = ContactGroupForm(request.POST, instance=group)
        else:
            form = ContactGroupForm(request.POST)

        if form.is_valid():
            form.instance.content_modified = datetime.datetime.utcnow()
            form.instance.thumbnail_modified = datetime.datetime.utcnow()
            group = form.save()

            return HttpResponseRedirect(reverse('groups'))


        return render(request, self.template_name, {'form': form})




