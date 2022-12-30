from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from blog.models import BlogItem


class BlogListView(ListView):
    model = BlogItem
    paginate_by = 3
    template_name = "blog/blogitem_list.html"

    def get(self, request, *args, **kwargs):
        blogs = BlogItem.objects.all()
        paginator = Paginator(blogs, self.paginate_by)

        page_number = request.GET.get('page')
        object_list = paginator.get_page(page_number)

        current_page = object_list.number
        previous_page = object_list.number - 1 if object_list.number > 1 else None
        next_page = object_list.number + 1 if object_list.number < paginator.num_pages else None

        context = {
            "object_list": object_list,
            "paginator": paginator,
            "current_page": current_page,
            "previous_page": previous_page,
            "next_page": next_page,
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
