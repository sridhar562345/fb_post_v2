from unittest.mock import create_autospec

from fb_post_v2.interactors.storages.reaction_storage_interface import \
	ReactionStorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
	PresenterInterface
from fb_post_v2.interactors.get_total_reactions_count_interactor import \
	GetTotalReactionsCountInteractor


def test_get_total_reactions_count_returns_total_count():
	total_reactions_count = 4
	expected_response = {
		"count": 4
	}
	storage = create_autospec(ReactionStorageInterface)
	presenter = create_autospec(PresenterInterface)
	storage.get_total_reactions_count.return_value = \
		total_reactions_count
	presenter.get_total_reactions_count_response.return_value = \
		expected_response
	interactor = GetTotalReactionsCountInteractor(storage, presenter)
	
	#act
	actual_response = interactor.get_total_reactions_count_interactor()
	
	#assert
	storage.get_total_reactions_count.assert_called_once()
	presenter.get_total_reactions_count_response.assert_called_once_with(
		total_reactions_count
	)
	assert actual_response == expected_response