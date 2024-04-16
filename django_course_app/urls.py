from django.urls import path

from django_course_app.apps import DjangoCourseAppConfig
from django_course_app.views import IndexView, ClientCreateView, ClientDeleteView, ClientUpdateView, \
    ClientListView, MessageCreateView, MessageListView, MessageUpdateView, MessageDeleteView, MessageDetailView, \
    NewsletterDetailView, NewsletterCreateView, NewsletterListView, \
    NewsletterUpdateView, NewsletterDeleteView, MailingAttemptListView, ClientDetailView

app_name = DjangoCourseAppConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('clients/detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),

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

]
