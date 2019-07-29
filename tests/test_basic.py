from hamcrest import *

from pytest_toolbelt import matchers


def test_basic_validation_error(client):
    response = client.post(
        '/test/',
        format='json'
    )

    assert_that(response, matchers.has_status(400))
    assert_that(
        response.json(),
        has_entries(
            code='ValidationError',
            description='Invalid input.'
        )
    )


def test_basic_buzz(client):
    response = client.post(
        '/test/buzz/',
        format='json'
    )

    assert_that(response, matchers.has_status(500))
    assert_that(
        response.json(),
        has_entries(
            code='DRFBuzz',
            description='basic error'
        )
    )


def test_basic_exception(client):
    response = client.post(
        '/test/exception/',
        format='json'
    )

    assert_that(response, matchers.has_status(500))
    assert_that(
        response.json(),
        has_entries(
            code='APIException',
            description='exception error'
        )
    )
