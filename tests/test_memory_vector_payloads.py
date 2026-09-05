"""Exercise the registered memory blueprint's three vector payload writers."""

from tests.test_api_endpoints import (  # noqa: F401
)

STATE_KEYS = {"t_valid", "t_invalid", "archived", "tag_prefixes", "relevance_score"}


def test_create_vector_payload(client, mock_state, auth_headers):
    pass  # TODO: implement


def test_patch_archived_vector_stays_archived(client, mock_state, auth_headers):
    pass  # TODO: implement


def test_batch_vector_payload(client, mock_state, auth_headers):
    pass  # TODO: implement


def test_embedding_failures_visible_in_health(mock_state):
    pass  # TODO: implement


