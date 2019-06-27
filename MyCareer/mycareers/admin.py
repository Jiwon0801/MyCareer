from django.contrib import admin
from .models import TB_PROJECT, TB_BASIC, TB_EDU_HIGH, TB_CAREER, TB_CERT, TB_EDUCATION, TB_REWARD, TB_EDU_UNIV, TB_GRADE


class TB_BASIC_Admin(admin.ModelAdmin):
    list_display = ('pk', 'user_name', 'en_f_nm',)

admin.site.register(TB_BASIC, TB_BASIC_Admin)


class TB_EDU_HIGH_Admin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'loc',)

admin.site.register(TB_EDU_HIGH, TB_EDU_HIGH_Admin)


class TB_EDU_UNIV_Admin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'loc',)

admin.site.register(TB_EDU_UNIV, TB_EDU_UNIV_Admin)

class TB_GRADE_Admin(admin.ModelAdmin):
    list_display = ('year', 'semester', 'name',)

admin.site.register(TB_GRADE, TB_GRADE_Admin)

class TB_CAREER_Admin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'dept',)

admin.site.register(TB_CAREER, TB_CAREER_Admin)


class TB_CERT_Admin(admin.ModelAdmin):
    list_display = ('pk', 'category', 'name',)

admin.site.register(TB_CERT, TB_CERT_Admin)


class TB_EDUCATION_Admin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'organization',)

admin.site.register(TB_EDUCATION, TB_EDUCATION_Admin)


class TB_REWARD_Admin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content',)

admin.site.register(TB_REWARD, TB_REWARD_Admin)


class TB_PROJECT_Admin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content',)

admin.site.register(TB_PROJECT, TB_PROJECT_Admin)


