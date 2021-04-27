from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Poll(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    start_date = models.DateField(auto_now_add=True, verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')
    description = models.CharField(max_length=300, verbose_name='Description')

    def __str__(self):
        return self.name


class Question(models.Model):
    QUESTION_TYPE = (
        ('text_answer', 'Ответ текстом'),
        ('one_choice', 'Выбор одного варианта'),
        ('few_choices', 'Выбор нескольких вариантов'),
    )
    text = models.TextField()
    type_question = models.CharField(
        max_length=15,
        choices=QUESTION_TYPE,
        verbose_name='Тип вопроса',
    )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, blank=True, related_name="questions")

    def __str__(self):
        return self.text


class Choice(models.Model):
    name = models.TextField(verbose_name='Name choice')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")

    def __str__(self):
        return self.name


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    text = models.TextField(null=True)
    one_choice = models.ForeignKey(Choice, null=True, on_delete=models.CASCADE, related_name="answers_one_choice")
    few_choice = models.ManyToManyField(Choice, null=True)
