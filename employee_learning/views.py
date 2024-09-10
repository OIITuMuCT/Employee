import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,  \
    DeleteView, DetailView, UpdateView, TemplateView

from .models import LearningCourse

class Index(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = datetime.date.today() 
        return context



# Create CRUD Web app.
class CourseList(LoginRequiredMixin, ListView):
    # model = LearningCourse
    queryset = LearningCourse.objects.order_by('title')
    # queryset = LearningCourse.objects.filter(level='B')
    # queryset = LearningCourse.objects.filter(title__contains='Docker')
    template_name = 'employee_learning/course_list.html'
    context_object_name = 'course_object_list'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        return context

class CourseDetail(LoginRequiredMixin, DetailView):
    model = LearningCourse
    template_name = 'employee_learning/course_detail.html'
    context_object_name = 'course_object'


class CourseCreate(LoginRequiredMixin ,CreateView):
    model = LearningCourse
    template_name = 'employee_learning/course_create.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('course_list')


class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = LearningCourse
    template_name = 'employee_learning/course_update.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('course_list')
    
class CourseDelete(LoginRequiredMixin, DeleteView):
    model = LearningCourse
    template_name = 'employee_learning/course_delete.html'
    success_url = reverse_lazy('course_list')



