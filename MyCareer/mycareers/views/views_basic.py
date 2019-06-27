from django.shortcuts import render, redirect
from mycareers.models import TB_BASIC
from mycareers.forms import BasicForm
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    if request.method == 'POST':
        instance = TB_BASIC(user = request.user)

        form = BasicForm(instance=instance, data=request.POST)

        if form.is_valid():
            form.save()
        else:
            print('invlid')
        
        return redirect('mycareers:index')

@login_required
def update(request, pk):
    
    if request.method =='POST':
        instance = TB_BASIC.objects.get(pk=pk)
        form = BasicForm(instance=instance, data=request.POST)

        if form.is_valid() and instance.user == request.user :
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        else : 
            print('invalid')

        return redirect('mycareers:index')

@login_required
def delete(request, pk):

    if request.method == 'POST':
        
        instance = TB_BASIC.objects.get(pk=pk)
        
        if request.user == instance.user :
            print('delete')
            instance.delete()
        
        return redirect('mycareers:index')
    