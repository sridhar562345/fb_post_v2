import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post_v2.storages.post_storage_implementation import PostStorageImplementation
from fb_post_v2.presenters.presenter_implementation import PresenterImplementation
from fb_post_v2.interactors.create_post_interactor import CreatePostInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    request_data = kwargs["request_data"]
    post_content = request_data["post_content"]
    presenter = PresenterImplementation()
    storage = PostStorageImplementation()
    interactor = CreatePostInteractor(storage, presenter)
    
    post_id_dict = interactor.create_post_return_post_id(
        user_id=user.id,
        post_content=post_content
    )
    
    response_data = json.dumps(post_id_dict)
    response = HttpResponse(response_data, status=201)
    
    return response