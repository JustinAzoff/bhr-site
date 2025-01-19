from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'bhr_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('bhr/', include('bhr.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='accounts_login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', RedirectView.as_view(url='/bhr', permanent=False), name='siteroot'),
]
