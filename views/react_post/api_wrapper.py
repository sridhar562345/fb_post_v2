import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post_v2.storages.validators_storage_implementation import ValidatorsStorageImplementation
from fb_post_v2.storages.reaction_storage_implementation import ReactionStorageImplementation
from fb_post_v2.presenters.presenter_implementation import PresenterImplementation
from fb_post_v2.interactors.react_to_post_interactor import ReactToPostInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    post_id = kwargs["post_id"]
    request_data = kwargs["request_data"]
    reaction_type = request_data["reaction_type"]
    presenter = PresenterImplementation()
    storage = ReactionStorageImplementation()
    validator = ValidatorsStorageImplementation()
    interactor = ReactToPostInteractor(validator, storage, presenter)
    
    interactor.react_to_post_interactor(
        user_id=user.id,
        post_id=post_id,
        reaction_type=reaction_type
    )
    
    response = HttpResponse(status=200)
    
    return response