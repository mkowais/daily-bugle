from django.conf.urls import url

from django.contrib import admin
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views.login
from rest_framework import routers

from . import views
from django.conf.urls import include, url

"""
routers is used for the rest api framework, to route the to the respective view set for each model. 
"""
router = routers.DefaultRouter()
router.register(r'Article', views.ArticleViewSet)
router.register(r'User', views.UserViewSet)
router.register(r'Comment', views.CommentViewSet)
router.register(r'Category', views.CategoryViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    # Index Page
    url(r'^/(?P<category>[0-9]+)$', views.index, name='indexWithCategory'),
    url(r'^$', views.index, name='index'),

    url(r'^accounts/login/$', views.login, name='loginRedirect'),

    # Sign Up Page
    url(r'^signup$', views.signup, name='signup'),
    # Login Page - Login
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^user/update$', views.updateProfile, name='userUpdate'),
    url(r'^loadMore/(?P<articlesAmount>([0-9]+))$', views.loadMoreArticles, name='loadMoreArticles'),
    # Login Page - Logout
    # url(r'^/logout', auth_views.logout, name='logout'),
    # User Page
    # url(r'^user/(?P<user_id>[0-9]+)$', views.user, name='user'),

    # Article Page
    url(r'^article/(?P<article_id>(new|[0-9]+))$', views.article, name='article'),
    # New Article Page
    url(r'^article/new$', views.article_add_new, name='article_add_new'),
    # Article filter by Category (Return list of Article IDs)
    url(r'^article/category/(?P<category_name>[a-zA-Z]+)$', views.article_category, name='article_category'),

    # GET Like Object <- Fixed Regex
    url(r'^article/(?P<article_id>[0-9]+)/likes$', views.AllLikes, name='get_ALLlikes'), # GET - All Likes, POST - New Likes
    url(r'^article/(?P<article_id>[0-9]+)/addorDislike/(?P<isLike>[0-9]+)$', views.addorDislike, name='get_likesAndDislikes'), # GET - All Likes, POST - New Likes

    # GET Comment Object
    url(r'^article/(?P<article_id>[0-9]+)/comments$', views.comment, name='comment'), # GET - All Comments, POST - New Comment
    #url(r'^ajax/article/(?P<article_id>[0-9]+)/addcomments$', views.addcomment, name='comment'), # GET - All Comments, POST - New Comment

    # UPDATE (POST|DELETE) Comment Object
    url(r'^article/(?P<article_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)$', views.del_comment, name='update_comment'), # POST - New Comment, DELETE -  Comment (Put Comment ID in Body)
]
