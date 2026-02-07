from django.db import models
from books.models import Book
from members.models import Member


class Quiz(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='quizzes'
    )
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class QuizResult(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='quiz_results'
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='results'
    )
    score = models.PositiveIntegerField()

    class Meta:
        unique_together = ('member', 'quiz')

    def __str__(self):
        return f"{self.member} - {self.quiz} ({self.score})"
