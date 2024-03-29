from django.urls import path,re_path
from app_compare import views

# TEMPLATE URLs
app_name = 'app_compare'

urlpatterns = [
    path('articles/',views.ArticleListView.as_view(),name='article_list'),
    re_path('articles/(?P<slug>\d+)/',views.ArticleDetailView.as_view(),name='article_detail'),
    path('graph/',views.graph_label,name='graph'),
    path('graph/datalabels.json/',views.graph_json,name='graph_json'),

]
