from mycareers.models import TB_BASIC, TB_CAREER, TB_EDU_HIGH, TB_EDU_UNIV
from django.http import JsonResponse

def get_info(request):
    
    basic = TB_BASIC.objects.filter(user=request.user).values()
    career = TB_CAREER.objects.filter(user=request.user).values()
#     edu_high = TB_EDU_HIGH.objects.filter(user=request.user).values()
#     edu_univ = TB_EDU_UNIV.objects.filter(user=request.user).values()
    return JsonResponse({
        "basic": list(basic),
        "career": list(career)
        })
