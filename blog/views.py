from django.shortcuts import render
from django.views import View

from blog.models import BlogItem


class BlogListView(View):
    template_name = "blog/blog.html"

    def get(self, request, *args, **kwargs):
        context = {
        }

        return render(request, self.template_name, context=context)


class BlogDetail(View):
    template_name = "blog/blog-details.html"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        blog = BlogItem.objects.get(pk=pk)
        tags = [blog.main_tag]
        tags.extend(blog.tags.all())
        tags = list(set(tags))
        context = {
            "object": blog,
            "tags": tags,
        }

        return render(request, self.template_name, context=context)
