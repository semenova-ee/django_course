from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from models import Client, Newsletter, Message, MailingAttempt
from forms import ClientCreateForm


class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        return Client.objects.all()


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/detail_client.html'
    context_object_name = 'detail_client'

   # def get_context_data(self, **kwargs):
   #      context_data = super().get_context_data(**kwargs)
   #      context_data['title'] = "Пользователи"
   #      return context_data

    def get_queryset(self):
        return Client.objects.all()


class ClientCreateView(ListView):
    model = Client
    template_name = 'client/client_form.html'
    form_client = ClientCreateForm
    success_url = reverse_lazy('django_course_app:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client/update_client.html'

    def get_queryset(self):
        pass


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/delete_client.html'

    def get_queryset(self):
        pass


class NewsletterListView(ListView):
    model = Newsletter
    template_name = 'newsletter/newsletter_list.html'
    context_object_name = 'newsletter_list'

    def get_queryset(self):
        return Newsletter.objects.all()


class NewsletterCreateView(CreateView):
    model = Newsletter
    template_name = 'newsletter/newsletter_form.html'
    form_class = ''


class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = 'client/detail_newsletter.html'

    def get_queryset(self):
        pass


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    template_name = 'client/update_newsletter.html'

    def get_queryset(self):
        pass


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    template_name = 'client/delete_newsletter.html'

    def get_queryset(self):
        pass


class MessageListView(ListView):
    model = Message
    template_name = 'newsletter/message_list.html'
    context_object_name = 'message_list'

    def get_queryset(self):
        return Newsletter.objects.all()


class MessageCreateView(CreateView):
    model = Message
    template_name = 'newsletter/message_form.html'
    form_class = ''


class MessageDetailView(DetailView):
    model = Message
    template_name = 'client/detail_message.html'

    def get_queryset(self):
        pass


class MessageUpdateView(UpdateView):
    model = Message
    template_name = 'client/update_message.html'

    def get_queryset(self):
        pass


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'client/delete_message.html'

    def get_queryset(self):
        pass
