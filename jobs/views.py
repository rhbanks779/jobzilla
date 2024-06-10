from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Job
from .forms import JobForm, ApplicationForm
from django.contrib import messages
from django.core.mail import EmailMessage


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'


class JobCreateView(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Job created successfully!')
        return response
    

class JobUpdateView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_url = '/jobs/'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Job updated successfully!')
        return response


class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job_list')

    def delete(self, request, *args, **kwargs):
        job = self.get_object()
        messages.success(request, f'The job "{job.title}" has been deleted.')
        job.delete()
        return redirect(self.success_url)

    
class CreateApplicationView(View):  
    def get(self, request, pk):
        job = Job.objects.get(pk=pk)
        form = ApplicationForm()
        return render(request, 'jobs/job_application_form.html', {'job': job, 'form': form})
    
    def post(self, request, pk):
        job = Job.objects.get(pk=pk)
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()

             # Access cleaned form data
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']

            # Send email confirmation- settings.py needs EMAIL_HOST_USER and EMAIL_HOST_PASSWORD values set
            message_body = f'Your application for {job.title} has been submitted to {job.company_name}. Thank you {first_name}!'
            email_message = EmailMessage("Application submission confirmation", message_body, to=[email])
            try:
                email_message.send()
            except Exception as e:
                messages.error(request, "An error occurred while sending the email.")
                return redirect('job_list')

            messages.success(request, "Application has been submitted.")
            return redirect('job_list')
        return render(request, 'jobs/job_application_form.html', {'job': job, 'form': form})
      