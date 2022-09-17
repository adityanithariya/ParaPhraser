from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

	# Apps
	path("python/", include("PyPhraser.urls")),
]

from .settings import DEBUG
if DEBUG:
	import debug_toolbar
	urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
