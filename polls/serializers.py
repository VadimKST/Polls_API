from django.db.models import Q
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *


class QuestionPollCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'text', 'type_question']
        model = Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Question


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Poll


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name']
        model = Choice


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Answer


class AnswerTextSerializer(serializers.ModelSerializer):
    one_choice = PrimaryKeyRelatedField(many=False, queryset=Choice.objects.all())

    class Meta:
        fields = ['text_answer']
        model = Answer


class AnswerOneChoiceSerializer(serializers.ModelSerializer):
    one_choice = PrimaryKeyRelatedField(many=False, queryset=Choice.objects.all())

    class Meta:
        fields = ['one_choice']
        model = Answer


class AnswerFewChoiceSerializer(serializers.ModelSerializer):
    many_choice = PrimaryKeyRelatedField(many=True, queryset=Choice.objects.all())

    class Meta:
        fields = ['few_choice']
        model = Answer
