from django.db import models
from django.conf import settings

class TB_BASIC(models.Model):
    user_name = models.TextField(blank=True, null=True)
    en_f_nm = models.TextField(blank=True, null=True)
    en_l_nm = models.TextField(blank=True, null=True)
    ch_nm = models.TextField(blank=True, null=True)
    birth = models.DateTimeField(blank=True, null=True)
    addr = models.TextField(blank=True, null=True)
    detail_addr = models.TextField(blank=True, null=True)
    zip_code = models.TextField(blank=True, null=True)
    phone1 = models.TextField(blank=True, null=True)
    phone2 = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    #img =  models.ImageField(blank=True)
    email = models.TextField(blank=True, null=True)
    hobby = models.TextField(blank=True, null=True)
    speciality = models.TextField(blank=True, null=True)

    army_div = models.TextField(blank=True, null=True)
    army_group = models.TextField(blank=True, null=True)
    army_rank = models.TextField(blank=True, null=True)
    army_reason = models.TextField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    army_end = models.DateTimeField(blank=True, null=True)
    army_id = models.TextField(blank=True, null=True)
    #army_cert = models.FileField()
    army_etc = models.TextField(blank=True, null=True)
    martial_status = models.TextField(blank=True, null=True)
    #attachments = models.FileField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class TB_EDU_HIGH(models.Model):
    name = models.TextField(blank=True, null=True)
    loc = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    start_type = models.TextField(blank=True, null=True)
    high_end = models.DateTimeField(blank=True, null=True)
    end_type = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class TB_EDU_UNIV(models.Model):
    name = models.TextField(blank=True, null=True)
    loc = models.TextField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    start_type = models.TextField(blank=True, null=True)
    uni_end = models.DateTimeField(blank=True, null=True)
    end_type = models.TextField(blank=True, null=True)
    day_yn = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    college = models.TextField(blank=True, null=True)
    transfer_yn = models.TextField(blank=True, null=True)
    major = models.TextField(blank=True, null=True)
    #grade_cert = models.FileField(blank=True)
    #graduate_cert = models.FileField(blank=True)
    #attachments = models.FileField(blank=True)
    total_score = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class TB_GRADE(models.Model):
    year = models.TextField(blank=True, null=True)
    semester = models.TextField(blank=True, null=True)
    major_yn = models.TextField(blank=True, null=True)
    credit = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    grade = models.TextField(blank=True, null=True)
    re_join = models.TextField(blank=True, null=True)
    edu_univ = models.ForeignKey(TB_EDU_UNIV, on_delete=models.CASCADE)


class TB_CAREER(models.Model):
    name = models.TextField(blank=True, null=True)
    dept = models.TextField(blank=True, null=True)
    loc = models.TextField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    career_end = models.DateTimeField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    salary = models.TextField(blank=True, null=True)
    tel = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    #attachment = models.FileField()
    resign = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class TB_CERT(models.Model):
    category = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    organization = models.TextField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    cert_end = models.DateTimeField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
    grade = models.TextField(blank=True, null=True)
    cert_num = models.TextField(blank=True, null=True)
    #cert_copy = models.FileField(blank=True)
    #attachments = models.FileField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class TB_EDUCATION(models.Model):
    name = models.TextField(blank=True, null=True)
    organization = models.TextField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    edu_end = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    #CERT = models.FileField()
    #attachments = models.FileField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class TB_REWARD(models.Model):
    name = models.TextField(blank=True, null=True)
    organization = models.TextField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    #attachments = models.FileField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class TB_PROJECT(models.Model):
    name = models.TextField(blank=True, null=True)
    order = models.TextField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    project_end = models.DateTimeField(blank=True, null=True)
    order = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    # attachments = models.FileField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class TB_ETC(models.Model):
    name = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    category = models.TextField()
    content = models.TextField()
    attachments = models.FileField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class TB_USER_FILTER(models.Model):
    start = models.DateTimeField()
    filter_end = models.DateTimeField()
    sort = models.TextField()
    category = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
