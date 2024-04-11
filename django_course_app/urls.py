from django.urls import path

from django_course_app.apps import DjangoCourseAppConfig
from django_course_app.views import IndexView, ClientCreateView, ClientDeleteView, ClientUpdateView, \
    ClientListView, MessageCreateView, MessageListView, MessageUpdateView, MessageDeleteView, MessageDetailView, \
    MailingAttemptDetailView, NewsletterDetailView, NewsletterCreateView, NewsletterListView, \
    NewsletterUpdateView, NewsletterDeleteView, MailingAttemptListView

app_name = DjangoCourseAppConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clients/', ClientListView.as_view(), name='clients_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),


    path('messages/', MessageListView.as_view(), name='messages'),
    path('messages/create', MessageCreateView.as_view(), name='message_create'),
    path('messages/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('messages/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('messages/detail/<int:pk>', MessageDetailView.as_view(), name='message_detail'),

    path('newsletters/', NewsletterListView.as_view(), name='newsletters'),
    path('newsletter/create', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/update/<int:pk>', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter/delete/<int:pk>', NewsletterDeleteView.as_view(), name='newsletter_delete'),
    path('schedules/detail/<int:pk>', NewsletterDetailView.as_view(), name='schedule_detail'),

    path('mailing_attempts/', MailingAttemptListView.as_view(), name='mailing_attempts'),
    path('mailing_logs/view/<int:pk>', MailingAttemptDetailView.as_view(), name='mailing_log_view'),

]
