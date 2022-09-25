from django.contrib.auth.views import LoginView
from .authFrom import MyauthForm


class MyloginView(LoginView):
    authentication_form = MyauthForm

    def get_success_url(self):
        if self.request.user.is_staff:
            self.next_page = 'manage_course_list'
            return self.get_redirect_url() or self.get_default_redirect_url()
        return self.get_redirect_url() or self.get_default_redirect_url()
