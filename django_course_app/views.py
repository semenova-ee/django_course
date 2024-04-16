from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from django_course_app.models import Client, Newsletter, Message, MailingAttempt
from django_course_app.forms import ClientForm, MessageCreateForm, NewsletterCreateForm


class IndexView(TemplateView):
    template_name = 'django_course_app/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count_mailing'] = Newsletter.objects.all().count()
        context_data['count_activity_mailings'] = Newsletter.objects.filter(status=2).count()
        context_data['count_clients'] = Client.objects.all().count()

        return context_data


class ClientListView(ListView):
    model = Client
    template_name = 'django_course_app/client/client_list.html'

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)


class ClientCreateView(ListView):
    model = Client
    template_name = 'django_course_app/client/client_form.html'
    form_client = ClientForm
    success_url = reverse_lazy('django_course_app:clients')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Добавление пользователя'
        return context_data

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'django_course_app/client/update_client.html'
    form_client = ClientForm
    success_url = reverse_lazy('django_course_app:clients')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Редактирование пользователя'
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'django_course_app/client/delete_client.html'
    success_url = reverse_lazy('django_course_app:clients')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление пользователя'
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class ClientDetailView(DetailView):
    model = Client
    template_name = 'django_course_app/client/detail_client.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.object
        return context_data

    # def get_queryset(self):
    #     return Client.objects.all()


class NewsletterListView(ListView):
    model = Newsletter
    template_name = 'django_course_app/newsletter/newsletter_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Рассылка сообщений'
        return context_data

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.groups.filter(name='manager'):
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset


class NewsletterCreateView(CreateView):
    model = Newsletter
    template_name = 'django_course_app/newsletter/newsletter_form.html'
    form_class = NewsletterCreateForm
    success_url = reverse_lazy('django_course_app:newsletters')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создание рассылки'
        return context_data

    def form_valid(self, form):
        obj: Newsletter = form.save()
        obj.owner = self.request.user
        obj.next_try = obj.start_date
        if obj.end_date <= obj.next_try:
            obj.status = 0
        obj.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = 'django_course_app/newsletter/detail_newsletter.html'


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    template_name = 'django_course_app/newsletter/update_newsletter.html'
    newsletter_form = NewsletterCreateForm
    success_url = reverse_lazy('django_course_app:newsletters')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Редактирование {self.object.description}'
        return context_data

    def get_initial(self):
        initial = super().get_initial()
        initial['owner'] = self.request.user
        return initial


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    template_name = 'django_course_app/newsletter/delete_newsletter.html'
    success_url = reverse_lazy('django_course_app:newsletters')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление рассылки'
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class MessageListView(ListView):
    model = Message
    template_name = 'django_course_app/message/message_list.html'


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = "Сообщения"
        return context_data

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)


class MessageCreateView(CreateView):
    model = Message
    template_name = 'django_course_app/message/message_form.html'
    form_class = MessageCreateForm
    success_url = reverse_lazy('django_course_app:messages')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создание сообщения'
        return context_data

    def form_valid(self, form):
        new_message = form.save()
        new_message.owner = self.request.user
        new_message.save()
        return super().form_valid(form)


class MessageDetailView(DetailView):
    model = Message
    template_name = 'django_course_app/message/detail_message.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.object
        return context_data


class MessageUpdateView(UpdateView):
    model = Message
    template_name = 'django_course_app/message/update_message.html'
    form_class = MessageCreateForm
    success_url = reverse_lazy('django_course_app:messages')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Редактирование "{self.object.title}"'
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'django_course_app/message/delete_message.html'
    success_url = reverse_lazy('django_course_app:messages')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление сообщения'
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class MailingAttemptListView(ListView):
    model = MailingAttempt
    template_name = 'django_course_app/mailingattempt/mailingattempt_list.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.schedule.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(schedule__owner=self.request.user)
        return queryset
