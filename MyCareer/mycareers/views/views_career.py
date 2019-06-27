from django.shortcuts import render, redirect
from mycareers.models import TB_CAREER
from mycareers.forms import CareerForm
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    if request.method == 'POST':
        instance = TB_CAREER(user = request.user)
        form = CareerForm(instance=instance, data=request.POST)
        # print(form)
        if form.is_valid():
            form.save()
        else:
            print('invalid')
            # Error code return
        return redirect('mycareers:index')

@login_required
def update(request, pk):
    if request.method == 'POST':
        instance = TB_CAREER.objects.get(pk=pk)
        if request.user == instance.user:
            form = CareerForm(instance=instance, data=request.POST)
            print(form)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
            else : 
                print('invalid')
                # Error code return
        return redirect('mycareers:index')

@login_required
def delete(request, pk):
    if request.method == 'POST':
        instance = TB_CAREER.objects.get(pk=pk)
        if(request.user == instance.user):
            instance.delete()
        return redirect('mycareers:index')