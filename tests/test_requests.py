from hamcrest import *

from pytest_toolbelt import matchers


def test_requests(client):
    response = client.post(
        '/test/requests/',
        format='json'
    )
    print(response.data)
    assert_that(response, matchers.has_status(400))
    assert_that(
        response.json(),
        has_entries(
            code='InvalidToken',
            description='Invalid token.'
        )
    )
