from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm


def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})


def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'members/member_detail.html', {'member': member})


def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()

    return render(request, 'members/member_form.html', {'form': form})


def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_detail', pk=member.pk)
    else:
        form = MemberForm(instance=member)

    return render(request, 'members/member_form.html', {'form': form})


def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        member.delete()
        return redirect('member_list')

    return render(request, 'members/member_confirm_delete.html', {'member': member})
