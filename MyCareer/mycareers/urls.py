from django.urls import path
from mycareers.views import views, views_basic, views_career, views_certification, views_education, views_extension, views_project,views_reward, views_training

app_name='mycareers'
urlpatterns = [

    path('', views.landing, name="landing" ),
    path('index/', views.index, name="index" ),
    path('logout/', views.logout, name="logout" ),
    path('detail/<int:item>/<int:pk>/', views.detail, name="detail" ),

    path('basic/create', views_basic.create, name="basic_create"),
    path('basic/<int:pk>/update/', views_basic.update, name="basic_update"),
    path('basic/<int:pk>/delete/', views_basic.delete, name="basic_delete"),

    path('edu/high/create', views_education.create_high, name="edu_create_high"),
    path('edu/high/<int:pk>/update/', views_education.update_high, name="edu_update_high"),
    path('edu/high/<int:pk>/delete/', views_education.delete_high, name="edu_delete_high"),

    path('edu/univ/create', views_education.create_univ, name="edu_create_univ"),
    path('edu/univ/<int:pk>/update/', views_education.update_univ, name="edu_update_univ"),
    path('edu/univ/<int:pk>/delete/', views_education.delete_univ, name="edu_delete_univ"),

    path('grade/create/', views_education.create_grade, name="grade"),
    path('grade/<int:pk>/update/', views_education.update_grade, name="grade_update"),
    path('grade/<int:pk>/delete/', views_education.delete_grade, name="grade_delete"),
    path('grade/delete/', views_education.delete_all_grade, name="grade_delete_all"),

    path('career/create', views_career.create, name="career_create"),
    path('career/<int:pk>/update/', views_career.update, name="career_update"),
    path('career/<int:pk>/delete/', views_career.delete, name="career_delete"),

    path('cert/create', views_certification.create, name="cert_create"),
    path('cert/<int:pk>/update/', views_certification.update, name="cert_update"),
    path('cert/<int:pk>/delete/', views_certification.delete, name="cert_delete"),

    path('training/create', views_training.create, name="training_create"),
    path('training/<int:pk>/update/', views_training.update, name="training_update"),
    path('training/<int:pk>/delete/', views_training.delete, name="training_delete"),

    path('reward/create', views_reward.create, name="reward_create"),
    path('reward/<int:pk>/update/', views_reward.update, name="reward_update"),
    path('reward/<int:pk>/delete/', views_reward.delete, name="reward_delete"),

    path('project/create', views_project.create, name="project_create"),
    path('project/<int:pk>/update/', views_project.update, name="project_update"),
    path('project/<int:pk>/delete/', views_project.delete, name="project_delete"),

    path('extension/', views_extension.get_info, name="chrome_extension"),
]