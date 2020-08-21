from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class BlogView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "pages/blog_1.html")
