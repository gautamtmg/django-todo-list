
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('auth/', include('authentication.urls')),
]

handler404 = "helpers.views.handle_not_found"
handler500 = "helpers.views.handle_server_error"