from django.conf.urls import url

from fb_post_v2.build.view_environments.post_create_v1_.router import post_create_v1_
from fb_post_v2.build.view_environments.posts__post_id__comment_create_v1_.router import posts__post_id__comment_create_v1_
from fb_post_v2.build.view_environments.comments__comment_id__reply_create_v1_.router import comments__comment_id__reply_create_v1_
from fb_post_v2.build.view_environments.posts__post_id__react_v1_.router import posts__post_id__react_v1_
from fb_post_v2.build.view_environments.comments__comment_id__react_v1_.router import comments__comment_id__react_v1_
from fb_post_v2.build.view_environments.reactions_count_v1_.router import reactions_count_v1_
from fb_post_v2.build.view_environments.posts__post_id__reaction_metrics_v1_.router import posts__post_id__reaction_metrics_v1_
from fb_post_v2.build.view_environments.posts__post_id__delete_v1_.router import posts__post_id__delete_v1_
from fb_post_v2.build.view_environments.more_postive_reactions_posts_v1_.router import more_postive_reactions_posts_v1_
from fb_post_v2.build.view_environments.reacted_posts.router import reacted_posts
from fb_post_v2.build.view_environments.posts__post_id__reactions_v1_.router import posts__post_id__reactions_v1_
from fb_post_v2.build.view_environments.posts__post_id__v1_.router import posts__post_id__v1_
from fb_post_v2.build.view_environments.posts_v1_.router import posts_v1_
from fb_post_v2.build.view_environments.comments__comment_id__replies_v1_.router import comments__comment_id__replies_v1_


urlpatterns = [
    url(r'^post/create/v1/$', post_create_v1_),
    url(r'^posts/(?P<post_id>\d+)/comment/create/v1/$', posts__post_id__comment_create_v1_),
    url(r'^comments/(?P<comment_id>\d+)/reply/create/v1/$', comments__comment_id__reply_create_v1_),
    url(r'^posts/(?P<post_id>\d+)/react/v1/$', posts__post_id__react_v1_),
    url(r'^comments/(?P<comment_id>\d+)/react/v1/$', comments__comment_id__react_v1_),
    url(r'^reactions/count/v1/$', reactions_count_v1_),
    url(r'^posts/(?P<post_id>\d+)/reaction_metrics/v1/$', posts__post_id__reaction_metrics_v1_),
    url(r'^posts/(?P<post_id>\d+)/delete/v1/$', posts__post_id__delete_v1_),
    url(r'^more/postive/reactions/posts/v1/$', more_postive_reactions_posts_v1_),
    url(r'^reacted/posts/$', reacted_posts),
    url(r'^posts/(?P<post_id>\d+)/reactions/v1/$', posts__post_id__reactions_v1_),
    url(r'^posts/(?P<post_id>\d+)/v1/$', posts__post_id__v1_),
    url(r'^posts/v1/$', posts_v1_),
    url(r'^comments/(?P<comment_id>\d+)/replies/v1/$', comments__comment_id__replies_v1_),
]
