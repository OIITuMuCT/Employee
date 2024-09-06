from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,  DeleteView, DetailView, UpdateView

from .models import LearningCourse

# Create CRUD Web app.
class CourseList(ListView):
    model = LearningCourse
    template_name = 'employee_learning/course_list.html'
    context_object_name = 'course_object_list'


class CourseDetail(DetailView):
    model = LearningCourse
    template_name = 'employee_learning/course_detail.html'
    context_object_name = 'course_object'
    
    # def get_context_data(self, **kwargs) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context[""] = 
    #     return context
    
class CourseCreate(CreateView):
    model = LearningCourse
    template_name = 'employee_learning/course_create.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('course_list')


class CourseUpdate(UpdateView):
    model = LearningCourse
    template_name = 'employee_learning/course_update.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('course_list')
    
class CourseDelete(DeleteView):
    model = LearningCourse
    template_name = 'employee_learning/course_delete.html'
    success_url = reverse_lazy('course_list')