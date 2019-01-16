from django.contrib.auth import login, logout
from django.shortcuts import render
from django import http
from django.views import generic
from . import forms, models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
class Home(generic.TemplateView):
    template_name = 'home.html'

    def get(self, request):
        if request.user.is_authenticated:
            all_posts = models.Post.objects.all()

            data = {
                'all_posts': all_posts
            }

            return render(request, self.template_name, data)
        else:
            return render(request, self.template_name, {})

    def post(self, request):
        query = request.POST['search']
        result_list = models.Post.objects.filter(title=query)
        if result_list.count() != 0:
            data = {
                'result_list': result_list,
                'query': query
            }
        else:
            data = {
                'empty': "Ничего ненайдено",
                'query': query
            }
        return render(request, 'result.html', data)


class RegisterFormView(generic.FormView):
    form_class = UserCreationForm
    success_url = "/login/"

    template_name = "register.html"

    def form_valid(self , form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):

        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(generic.FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        print("hi")
        return http.HttpResponseRedirect("/")






















































def post_form(request):
    form_post = forms.PostForm
    data = {
        "form_post": form_post
    }
    return render(request, 'post_form.html', data)


def add_post(request):
    form = forms.PostForm(request.POST)
    form.save()
    print(form)
    return http.HttpResponse('Cool!')


class ContactFormView(generic.TemplateView):
    form_contact = forms.ContactForm

    def get(self, request):
        context = {
            'form_contact': self.form_contact
        }
        return render(request, 'contact_form.html', context)

    def post(self, request):
        form = forms.ContactForm(request.POST)
        context = {
            'form_contact': form,
        }
        if form.is_valid():
            data = form.cleaned_data
            return http.HttpResponse(data.items())
        else:
            return render(request, 'contact_form.html', context)
