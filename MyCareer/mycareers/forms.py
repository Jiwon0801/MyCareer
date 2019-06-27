from django import forms
from mycareers.models import TB_BASIC, TB_EDUCATION, TB_CAREER, TB_CERT, TB_EDU_HIGH, TB_EDU_UNIV, TB_GRADE, TB_PROJECT, TB_REWARD

class BasicForm(forms.ModelForm):
	class Meta:
		model = TB_BASIC
		exclude = ('user',)

class EducationForm(forms.ModelForm):
	class Meta:
		model = TB_EDUCATION
		exclude = ('user',)
	
class CareerForm(forms.ModelForm):
	class Meta:
		model = TB_CAREER
		exclude = ('user',)

class CertForm(forms.ModelForm):
	class Meta:
		model = TB_CERT
		exclude = ('user',)

class EduHighForm(forms.ModelForm):
	class Meta:
		model = TB_EDU_HIGH
		exclude = ('user',)


class EduUnivForm(forms.ModelForm):
	class Meta:
		model = TB_EDU_UNIV
		exclude = ('user',)


class GradeForm(forms.ModelForm):
	class Meta:
		model = TB_GRADE
		exclude = ('edu_univ',)

class ProjectForm(forms.ModelForm):
	class Meta:
		model = TB_PROJECT
		exclude = ('user',)

class RewardForm(forms.ModelForm):
	class Meta:
		model = TB_REWARD
		exclude = ('user',)
