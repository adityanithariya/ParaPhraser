from django.urls import path
from .views import pyCompiler, cCompiler, cppCompiler, javaCompiler, jsCompiler, rCompiler, goCompiler, rubyCompiler

urlpatterns = [
	path("py/", pyCompiler, name="pyCompile"),
	path("c/", cCompiler, name="cCompile"),
	path("cpp/", cppCompiler, name="cppCompile"),
	path("java/", javaCompiler, name="javaCompile"),
	path("js/", jsCompiler, name="jsCompile"),
	path("r/", rCompiler, name="rCompile"),
	path("go/", goCompiler, name="goCompiler"),
	path("ruby/", rubyCompiler, name="rubyCompiler"),
]
