from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django_course_app.models import Client, Newsletter, Message, MailingAttempt
from django_course_app.forms import ClientForm, MessageCreateForm, NewsletterCreateForm


class IndexView(TemplateView):
    template_name = 'django_course_app/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Главная'
        return context_data


class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        return Client.objects.all()


class ClientCreateView(ListView):
    model = Client
    template_name = 'client/client_form.html'
    form_client = ClientForm
    success_url = reverse_lazy('django_course_app:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Добавление пользователя'
        return context_data

    # def get_success_url(self):
    #     return reverse('django_course_app:clients')

    # def form_valid(self, form):
    #     self.object = form.save()
    #     self.object.owner = self.request.user
    #     self.object = form.save()
    #
    #     return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client/update_client.html'
    form_client = ClientForm
    success_url = reverse_lazy('django_course_app:clients')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Редактирование пользователя'
        return context_data

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     return self.object


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/delete_client.html'
    success_url = reverse_lazy('django_course_app:clients')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление пользователя'
        return context_data

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     return self.object


# class ClientDetailView(DetailView):
#     model = Client
#     template_name = 'client/detail_client.html'
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['title'] = "Пользователи"
#         return context_data
#
#     def get_queryset(self):
#         return Client.objects.all()


class NewsletterListView(ListView):
    model = Newsletter
    template_name = 'newsletter/newsletter_list.html'
    context_object_name = 'newsletter_list'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Рассылка сообщений'
        return context_data

    def get_queryset(self):
        return Newsletter.objects.all()


class NewsletterCreateView(CreateView):
    model = Newsletter
    template_name = 'newsletter/newsletter_form.html'
    form_class = NewsletterCreateForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создание рассылки'
        return context_data

    def get_success_url(self):
        return reverse('django_course_app:newsletter')

    # def form_valid(self, form):
    #     new_newsletter = form.save()
    #     return super().form_valid(form)


class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = 'newsletter/detail_newsletter.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.object.description

        # newsletter_item = Newsletter.objects.get(pk=self.kwargs.get('pk'))
        # user_item = Client.objects.filter(is_active=True)
        # context_data['newsletter_pk'] = newsletter_item.pk
        # context_data['user_item'] = user_item

        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    template_name = 'newsletter/update_newsletter.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Редактирование {self.object.description}'
        return context_data

    def get_success_url(self):
        return reverse('django_course_app:newsletter')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    template_name = 'newsletter/delete_newsletter.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление рассылки'
        return context_data

    def get_success_url(self):
        return reverse('django_course_app:newsletter')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object


class MessageListView(ListView):
    model = Message
    template_name = 'message/message_list.html'
    context_object_name = 'message_list'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = "Сообщения"
        return context_data

    def get_queryset(self):
        return Newsletter.objects.all()


class MessageCreateView(CreateView):
    model = Message
    template_name = 'nmessage/message_form.html'
    form_class = MessageCreateForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создание сообщения'
        return context_data

    def get_success_url(self):
        return reverse('django_course_app:messages')

    # def form_valid(self, form):
    #     new_message = form.save()
    #     return super().form_valid(form)


class MessageDetailView(DetailView):
    model = Message
    template_name = 'message/detail_message.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.object
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object


class MessageUpdateView(UpdateView):
    model = Message
    template_name = 'massege/update_message.html'
    form_class = MessageCreateForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Редактирование "{self.object.title}"'
        return context_data

    def get_success_url(self):
        return reverse('django_course_app:messages')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message/delete_message.html'
    success_url = reverse_lazy('django_course_app:messages')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Удаление сообщения'
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object


class MailingAttemptListView(ListView):
    model = MailingAttempt
    template_name = 'mailingattempt/mailingattempt_list.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object

    def get_queryset(self, *args, **kwargs):
        return MailingAttempt.objects.all()


class MailingAttemptDetailView(DetailView):
    model = MailingAttempt
    template_name = 'mailingattempt/mailingattempt_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object
