from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import User
from pprint import pprint
from baseapps.forms import UserForm
# Create your views here.

class IndexPage(ListView):
    template_name = './index.html'
    model = User
    queryset= User.objects.all()
    paginate_by = 10
    context_object_name = 'users'
    
    def get_queryset(self):
        ret = self.queryset
        sex = self.request.GET.get('sex',None)
        if sex:
            ret = ret.filter(sex=sex)
        age = self.request.GET.get('age',None)
        if age:
            ret = ret.filter(age=age)
        sort = self.request.GET.get('sort', None)
        if sort:
            sort = sort.split(",")
            sort = list(sort)
            for s in sort:
                ret = ret.order_by(s)
        return ret

    def get_context_data(self,**kwargs):
        context = super(IndexPage,self).get_context_data(**kwargs)
        context['const_sex'] = User.CONST_SEX
        context['const_age'] = User.objects.all().values_list('age',flat=True).distinct()
        context['sort']= self.request.GET.get('sort',None)
        context['sex']= self.request.GET.get('sex',None)
        context['age']= self.request.GET.get('age',None)
        print (self.request.get_full_path())
        return context


class CreateUser(CreateView):
    template_name = './create.html'
    form_class = UserForm


class EditUser(UpdateView):
    template_name = './edit.html'
    model = User
    form_class = UserForm

    def get_context_data(self,**kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['user'] = get_object_or_404(User, pk=pk)
        context['form'] = self.form_class(instance=context['user'])
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        form = self.form_class(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            url = reverse('home-page')
            return HttpResponseRedirect(url)