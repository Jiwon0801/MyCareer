from django.shortcuts import render, redirect
from mycareers.models import TB_EDU_HIGH, TB_EDU_UNIV, TB_GRADE
from mycareers.forms import EduHighForm, EduUnivForm, GradeForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def create_high(request):
    if request.method == 'POST':
        instance = TB_EDU_HIGH(user = request.user)

        form = EduHighForm(instance=instance, data=request.POST)
        print(form)
        if form.is_valid():
            form.save()
        else:
            print('invlid')
        
        return redirect('mycareers:index')

@login_required
def update_high(request, pk):
    
    if request.method =='POST':
        instance = TB_EDU_HIGH.objects.get(pk=pk)
        form = EduHighForm(instance=instance, data=request.POST)
        print(form)
        if form.is_valid() and instance.user == request.user :
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        else : 
            print('invalid')

        return redirect('mycareers:index')

@login_required
def delete_high(request, pk):

    if request.method == 'POST':
        
        instance = TB_EDU_HIGH.objects.get(pk=pk)
        
        if request.user == instance.user :
            print('delete')
            instance.delete()
        
        return redirect('mycareers:index')

@login_required
def create_univ(request):
    if request.method == 'POST':
        instance = TB_EDU_UNIV(user = request.user)

        form = EduUnivForm(instance=instance, data=request.POST)
        print(form)
        if form.is_valid():
            form.save()
        else:
            print('invlid')
        
        return redirect('mycareers:index')

@login_required
def update_univ(request, pk):
    
    if request.method =='POST':
        instance = TB_EDU_UNIV.objects.get(pk=pk)
        form = EduUnivForm(instance=instance, data=request.POST)
        print(form)
        if form.is_valid() and instance.user == request.user :
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        else : 
            print('invalid')

        return redirect('mycareers:index')

@login_required
def delete_univ(request, pk):

    if request.method == 'POST':
        
        instance = TB_EDU_UNIV.objects.get(pk=pk)
        
        if request.user == instance.user :
            print('delete')
            instance.delete()
        
        return redirect('mycareers:index')
    
@login_required
def create_grade(request):
    if request.method == 'POST':

        edu_univ = TB_EDU_UNIV.objects.get(user = request.user)
        instance = TB_GRADE(edu_univ = edu_univ)

        form = GradeForm(instance=instance, data=request.POST)
        print(form)
        if form.is_valid():
            data = 200
            form.save()
        else:
            data = 404
            print('invlid')
        
        return JsonResponse({"data": data})

@login_required
def update_grade(request, pk):
    
    if request.method =='POST':
        instance = TB_GRADE.objects.get(pk=pk)
        form = GradeForm(instance=instance, data=request.POST)
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.edu_univ = TB_EDU_UNIV.objects.get(user = request.user)
            instance.save()
            data = 200
        else : 
            print('invalid')
            data = 404

        return JsonResponse({"data": data})

@login_required
def delete_grade(request, pk):
    try:
        instance = TB_GRADE.objects.get(pk=pk)
        print('delete')
        instance.delete()
        data = 200

    except Exception as ex: # 에러 종류
        print(ex)
        data = 404
    return JsonResponse({"data": data})



@login_required
def delete_all_grade(request):

    if request.method == 'POST':
        try:
            edu = TB_EDU_UNIV.objects.get(user = request.user)
            instance = TB_GRADE.objects.filter(edu_univ=edu)
            print('delete')
            instance.delete()
            data = 200
        except Exception as ex:
            print(ex)
            data = 404
        
        return JsonResponse({"data": data})