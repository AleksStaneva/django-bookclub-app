from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, QuizResult
from .forms import QuizResultForm
from members.models import Member


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    members = Member.objects.all()

    if request.method == 'POST':
        form = QuizResultForm(request.POST)
        member_id = request.POST.get('member')

        if form.is_valid() and member_id:
            member = get_object_or_404(Member, id=member_id)
            result = form.save(commit=False)
            result.member = member
            result.quiz = quiz
            result.save()

            member.total_points += result.score
            member.save()

            return redirect('ranking')

    else:
        form = QuizResultForm()

    return render(request, 'quizzes/quiz_detail.html', {
        'quiz': quiz,
        'form': form,
        'members': members
    })
from django.shortcuts import render

# Create your views here.
