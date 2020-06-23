path_method_dict = {
    "reacted/posts/": {
        "GET": "user_posts"
    }
}


def reacted_posts(request, *args, **kwargs):
    from django_swagger_utils.drf_server.utils.server_gen.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from django_swagger_utils.drf_server.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("fb_post_v2", "reacted_posts", operations_dict, request, *args, **kwargs)
    return response