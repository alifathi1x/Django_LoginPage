from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import LoginForm


class LoginPage(FormView):
    template_name = 'auth/login_page.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')  # یا آدرس مورد نظر پس از لاگین

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)