from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse, HttpResponse
from mycareers.models import TB_BASIC, TB_EDU_HIGH, TB_EDU_UNIV, TB_GRADE, TB_CAREER, TB_CERT, TB_EDUCATION, TB_REWARD, TB_PROJECT
from django.core.exceptions import ObjectDoesNotExist
import json
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
def landing(request):
    return render(request, 'mycareers/landing.html')

@login_required
def index(request):
    context = {}
    timeline = []
    # 기본 사항 추가
    try:
        basic = TB_BASIC.objects.get(user=request.user)
        context['basic'] = basic
        setattr(basic,'table_type', 0)
        if basic.start is not None :
            timeline.append(basic)
    except ObjectDoesNotExist:
        pass

    # 고등학교
    try:
        edu_high = TB_EDU_HIGH.objects.get(user=request.user)
        context['edu_high'] = edu_high
        setattr(edu_high, 'table_type', 1)
        if edu_high.start is not None :
            timeline.append(edu_high)        
    except ObjectDoesNotExist:
        pass

    # 대학교
    try:
        edu_univ = TB_EDU_UNIV.objects.get(user=request.user)
        context['edu_univ'] = edu_univ
        setattr(edu_univ, 'table_type', 2)
        if edu_univ.start is not None :
            timeline.append(edu_univ)
    except ObjectDoesNotExist:
        pass
    
    # 성적
    try:
        edu_univ = TB_EDU_UNIV.objects.get(user=request.user)
        grades = TB_GRADE.objects.filter(edu_univ = edu_univ)            
        context['grades'] = grades
    except ObjectDoesNotExist:
        pass
    # 경력
    try:
        career = TB_CAREER.objects.get(user=request.user)
        context['career'] = career
        setattr(career, 'table_type', 3)
        if career.start is not None :
            timeline.append(career)
    except ObjectDoesNotExist:
        pass

    # 자격증
    try:
        cert = TB_CERT.objects.get(user=request.user)
        context['cert'] = cert
        setattr(cert, 'table_type', 4)
        if cert.start is not None :
            timeline.append(cert)
    except ObjectDoesNotExist:
        pass
    # 교육
    try:
        training = TB_EDUCATION.objects.get(user=request.user)
        context['training'] = training
        setattr(training, 'table_type', 5)
        if training.start is not None :
            timeline.append(training)
    except ObjectDoesNotExist:
        pass
    # 수상이력
    try:
        reward = TB_REWARD.objects.get(user=request.user)
        context['reward'] = reward
        setattr(reward, 'table_type', 6)
        if reward.start is not None :
            timeline.append(reward)
    except ObjectDoesNotExist:
        pass

    # 프로젝트
    try:
        project = TB_PROJECT.objects.get(user=request.user)
        context['project'] = project
        setattr(project, 'table_type', 7)
        if project.start is not None :
            timeline.append(project)

    except ObjectDoesNotExist:
        pass


    # for item in timeline:
    #     print(item.start)
    timeline = sorted(timeline, key=lambda item: item.start)
    context['timeline'] = timeline
    # print('after:sort')
    # for item in timeline:
    #     print(item.start)

    return render(request, 'mycareers/index.html', context)

def logout(request):
    auth_logout(request)
    return redirect('mycareers:landing')

color_list = ['success', 'info', 'danger', 'warning']

basic_dict = {
    'id' : ''
	,'user_name' : '이름'
	,'en_f_nm' : '이름(Last name)'
	,'en_l_nm' : '성(Family name)'
	,'ch_nm' : '한자이름'
	,'birth' : '생년월일'
	,'addr' : '주소'
	,'detail_addr' : '상세주소'
	,'zip_code' : '우편번호'
	,'phone1' : '핸드폰'
	,'phone2' : '연락처'
	,'sex' : '성별'
	,'email' : 'E-mail'
	,'hobby' : '취미'
	,'speciality' : '특기'
	,'army_div' : '병역구분'
	,'army_group' : '군별'
	,'army_rank' : '계급'
	,'army_reason' : '면제사유'
	,'start' : '복무기간'
	,'army_end' : '복무기간'
	,'army_id' : '군번'
	,'army_etc' : '복무 중 특이사항'
	,'martial_status' : '혼인여부'
	,'user_id' : ''
}
career_dict = {
    'id' : '',
    'name' : '회사명',
    'dept' : '소속부서',
    'loc' : '소재지',
    'start' : '입사일',
    'career_end' : '퇴사일',
    'position' : '직급',
    'job' : '직무',
    'salary' : '연봉',
    'tel' : '인사부서 연락처',
    'email' : '인사부서 이메일',
    'resign' : '퇴직사유',
    'user_id' : '',
}

cert_dict = {
    'id' : '',
    'category' : '자경증 분류',
    'name' : '자격증 이름',
    'organization' : '발급기관',
    'start' : '취득년월',
    'cert_end' : '만료기간',
    'score' : '점수',
    'grade' : '등급',
    'cert_num' : '자격증 번호',
    'user_id' : '',
}

education_dict = {
    'id' : '',
    'name' : '교육과정명',
    'organization' : '교육기관',
    'start' : '교육시작',
    'edu_end' : '교육종료',
    'content' : '내용',
    'user_id' : '',
}

reward_dict = {
    'id' : '',
    'name' : '상훈명',
    'organization' : '수여기관',
    'start' : '수여일',
    'content' : '내용',
    'user_id' : '',
}

project_dict = {
    'id' : '',
    'name' : '프로젝트명',
    'order' : '교육기관',
    'start' : '교육시작',
    'project_end' : '교육종료',
    'role' : '역할',
    'summary' : '교육종료',
    'content' : '내용',
    'user_id' : '',
}

high_dict = {
    'id' : ''
   ,'name' : '학교명'
   ,'loc' : '소재지'
   ,'category' : '전공계열'
   ,'start' : '재학기간'
   ,'start_type' : '재학여부'
   ,'high_end' : '재학기간'
   ,'end_type' : '졸업여부'
   ,'user_id' : '',
}

univ_dict = {
    'id' : ''
   ,'name' : '학교명'
   ,'loc' : '지역'
   ,'start' : '재학기간'
   ,'start_type' : '재학여부'
   ,'uni_end' : '재학기간'
   ,'end_type' : '졸업여부'
   ,'day_yn' : '주/야간'
   ,'category' : '대학선택'
   ,'college' : '단과대'
   ,'transfer_yn' : '편입여부'
   ,'major' : '전공'
   ,'user_id' : ''
   ,'total_score' : '학점 기준',
}



@login_required
def detail(request, item, pk):
   
    if item == 0:
        basic = TB_BASIC.objects.filter(user=request.user).values()
        res = ''
        datas = list(basic)[0]
        
        for key in datas.keys() : 
            if key in ['army_div', 'army_group','army_rank','army_reason','start','army_end','army_id','army_etc'] :
                color = random.choice(color_list)

                html = f'<div class="kt-widget-5__item kt-widget-5__item--{color}"><div class="pl-3"><div class="kt-widget-5__item-datetime">{basic_dict[key]}</div><a href="#" class="kt-widget-5__item-title">{str(datas[key])}</a></div></div>'
                res = res + html

    elif item == 1:
        edu_high = TB_EDU_HIGH.objects.filter(user=request.user).values()
        res = ''
        datas = list(edu_high)[0]
        
        for key in datas.keys() : 
            if key != 'id' and key != 'user_id' :
                color = random.choice(color_list)

                html = f'<div class="kt-widget-5__item kt-widget-5__item--{color}"><div class="pl-3"><div class="kt-widget-5__item-datetime">{high_dict[key]}</div><a href="#" class="kt-widget-5__item-title">{str(datas[key])}</a></div></div>'
                res = res + html
    elif item == 2:
        edu_univ = TB_EDU_UNIV.objects.filter(user=request.user).values()
        res = ''
        datas = list(edu_univ)[0]
        
        for key in datas.keys() : 
            if key != 'id' and key != 'user_id' :
                color = random.choice(color_list)

                html = f'<div class="kt-widget-5__item kt-widget-5__item--{color}"><div class="pl-3"><div class="kt-widget-5__item-datetime">{univ_dict[key]}</div><a href="#" class="kt-widget-5__item-title">{str(datas[key])}</a></div></div>'
                res = res + html
    elif item == 3:
        career = TB_CAREER.objects.filter(user=request.user).values()
        res = ''
        datas = list(career)[0]
        
        for key in datas.keys() : 
            if key != 'id' and key != 'user_id' :
                color = random.choice(color_list)

                html = f'<div class="kt-widget-5__item kt-widget-5__item--{color}"><div class="pl-3"><div class="kt-widget-5__item-datetime">{career_dict[key]}</div><a href="#" class="kt-widget-5__item-title">{str(datas[key])}</a></div></div>'
                res = res + html
    elif item == 4:
        cert = TB_CERT.objects.filter(user=request.user).values()
        res = ''
        datas = list(cert)[0]
        
        for key in datas.keys() : 
            if key != 'id' and key != 'user_id' :
                color = random.choice(color_list)

                html = f'<div class="kt-widget-5__item kt-widget-5__item--{color}"><div class="pl-3"><div class="kt-widget-5__item-datetime">{cert_dict[key]}</div><a href="#" class="kt-widget-5__item-title">{str(datas[key])}</a></div></div>'
                res = res + html
    elif item == 5:
        education = TB_EDUCATION.objects.filter(user=request.user).values()
        res = ''
        datas = list(education)[0]
        
        for key in datas.keys() : 
            if key != 'id' and key != 'user_id' :
                color = random.choice(color_list)

                html = f'<div class="kt-widget-5__item kt-widget-5__item--{color}"><div class="pl-3"><div class="kt-widget-5__item-datetime">{education_dict[key]}</div><a href="#" class="kt-widget-5__item-title">{str(datas[key])}</a></div></div>'
                res = res + html
    elif item == 6:
        reward = TB_REWARD.objects.filter(user=request.user).values()
        res = ''
        datas = list(reward)[0]
        
        for key in datas.keys() : 
            if key != 'id' and key != 'user_id' :
                color = random.choice(color_list)

                html = f'<div class="kt-widget-5__item kt-widget-5__item--{color}"><div class="pl-3"><div class="kt-widget-5__item-datetime">{reward_dict[key]}</div><a href="#" class="kt-widget-5__item-title">{str(datas[key])}</a></div></div>'
                res = res + html
    elif item == 7:
        project = TB_PROJECT.objects.filter(user=request.user).values()
        res = ''
        datas = list(project)[0]
        
        for key in datas.keys() : 
            if key != 'id' and key != 'user_id' :
                color = random.choice(color_list)

                html = f'<div class="kt-widget-5__item kt-widget-5__item--{color}"><div class="pl-3"><div class="kt-widget-5__item-datetime">{project_dict[key]}</div><a href="#" class="kt-widget-5__item-title">{str(datas[key])}</a></div></div>'
                res = res + html

    return HttpResponse(res)