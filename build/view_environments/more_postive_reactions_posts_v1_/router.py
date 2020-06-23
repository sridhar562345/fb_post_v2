path_method_dict = {
    "more/postive/reactions/posts/v1/": {
        "GET": "posts_with_more_postive_recations"
    }
}


def more_postive_reactions_posts_v1_(request, *args, **kwargs):
    from django_swagger_utils.drf_server.utils.server_gen.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from django_swagger_utils.drf_server.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("fb_post_v2", "more_postive_reactions_posts_v1_", operations_dict, request, *args, **kwargs)
    return response