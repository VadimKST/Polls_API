from datetime import datetime

from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404

from .models import Poll, Question, Choice, Answer
from .serializers import PollSerializer, QuestionPollCreateSerializer, \
    QuestionSerializer, ChoiceSerializer, AnswerSerializer, AnswerOneChoiceSerializer, AnswerFewChoiceSerializer, \
    AnswerTextSerializer


class PollCreateView(generics.CreateAPIView):
    queryset = Poll.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PollSerializer


class PollListView(generics.ListAPIView):
    queryset = Poll.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PollSerializer


class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionSerializer
    filter_backends = [SearchFilter]
    search_fields = ['poll__id']


class QuestionDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionSerializer


class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionSerializer


class PollQuestionsView(generics.ListCreateAPIView):
    serializer_class = QuestionPollCreateSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        poll = get_object_or_404(Poll, pk=self.kwargs['pk'])
        return poll.questions.all()

    def perform_create(self, serializer):
        poll = get_object_or_404(Poll, pk=self.kwargs['pk'])
        serializer.save(poll=poll)


class PollDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PollSerializer


class ChoiceView(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        question = get_object_or_404(Question, id=self.kwargs['pk'])
        return question.choices.all()

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        serializer.save(question=question)


class ActivePollListView(generics.ListAPIView):
    queryset = Poll.objects.filter(end_date__gte=datetime.today())
    serializer_class = PollSerializer
    permission_classes = (permissions.AllowAny,)


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            poll__id=self.kwargs['id'],
        )
        if question.type_question == 'text_answer':
            return AnswerTextSerializer
        elif question.type_question == 'one_choice':
            return AnswerOneChoiceSerializer
        else:
            return AnswerFewChoiceSerializer

    def perform_create(self, serializer):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            poll__id=self.kwargs['id'],
        )
        serializer.save(author=self.request.user, question=question)
