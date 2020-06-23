import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post_v2.storages.validators_storage_implementation import ValidatorsStorageImplementation
from fb_post_v2.storages.comment_storage_implementation import CommentStorageImplementation
from fb_post_v2.presenters.presenter_implementation import PresenterImplementation
from fb_post_v2.interactors.create_comment_interactor import CreateCommentInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    post_id = kwargs["post_id"]
    request_data = kwargs["request_data"]
    comment_content = request_data["comment_content"]
    presenter = PresenterImplementation()
    storage = CommentStorageImplementation()
    validator = ValidatorsStorageImplementation()
    interactor = CreateCommentInteractor(validator, storage, presenter)
    
    comment_id_dict = interactor.create_comment_return_comment_id(
        user_id=user.id,
        post_id=post_id,
        comment_content=comment_content
    )
    
    response_data = json.dumps(comment_id_dict)
    response = HttpResponse(response_data, status=201)
    
    return response