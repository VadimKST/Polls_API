from django.urls import path

from .views import PollCreateView, PollListView, PollQuestionsView, QuestionListView, \
    QuestionUpdateView, QuestionDeleteView, PollDeleteView, ChoiceView, AnswerCreateView, ActivePollListView

urlpatterns = [
    path('poll/create/', PollCreateView.as_view()),
    path('poll/list/', PollListView.as_view()),
    path('poll/<int:pk>/questions/', PollQuestionsView.as_view()),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view()),

    path('question/<int:pk>/', QuestionUpdateView.as_view()),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view()),
    path('question/list/', QuestionListView.as_view()),
    path('question/<int:pk>/choices', ChoiceView.as_view()),
    path('question/<int:pk>/answer', AnswerCreateView.as_view()),

    path('active_polls/', ActivePollListView.as_view()),
]
