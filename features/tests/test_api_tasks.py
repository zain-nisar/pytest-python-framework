"""validate coinmarketcap API feature tests."""
from features.businesslogic.api_functions import ValidateApiResponse
from pytest_bdd import (given,scenario, then, when, parsers)

obj_ValidateApiResponse = ValidateApiResponse()

@scenario(r'api_tasks.feature', 'Currency price conversion verification')
def test_currency_price_conversion_verification():
    """Currency price conversion verification."""


@scenario(r'api_tasks.feature', 'Currency information verification')
def test_Currency_information_verification():
    """Currency price conversion verification."""


@scenario(r'api_tasks.feature', 'Currencies having mineable tag associated')
def test_Currency_information_verification_tags():
    """Currencies having mineable tag associated"""


@when(parsers.cfparse('User call the endpoint "{endpoint}" for getting IDs of "{symbols}"'))
def user_call_the_ids_of_btcusdteth(endpoint,symbols):
    """User call the IDs of "BTC,USDT,ETH"."""
    assert obj_ValidateApiResponse.get_api_ids(endpoint,symbols)

@when(parsers.cfparse('User call the endpoint "{endpoint}" for getting info of "{symbols}"'))
def user_call_the_info_of_eth(endpoint,symbols):
    """User call the Info of "ETH"."""
    assert obj_ValidateApiResponse.get_api_info(endpoint,symbols)

@when(parsers.cfparse('User call the endpoint "{endpoint}" for getting information of "{numbers}" ids'))
def user_call_the_info_of_ids(endpoint,numbers):
    """User call the Info of provided ids."""
    assert obj_ValidateApiResponse.get_api_info_provided(endpoint,numbers)


@then(parsers.cfparse('User should convert them to "{currency}" by calling the endpoint "{endpoint}"'))
def user_should_convert_them_to_bolvian_boliviano(currency,endpoint):
    """user should convert them to "Bolvian Boliviano"."""
    obj_ValidateApiResponse.price_conversion(currency,endpoint)

@then(parsers.cfparse('User should validate api response with the information from "{json}"'))
def user_should_convert_them_to_bolvian_boliviano(json):
    """user should validate api response with the information provided"."""
    assert obj_ValidateApiResponse.get_data_and_validate(json)

@then(parsers.cfparse('user should printed out currencies associated with "{tag}" tag'))
def user_should_printed_out_currencies_asscociated(tag):
    """user should printed out currencies asscociated with tag"."""
    obj_ValidateApiResponse.get_associated_tag_and_validate(tag)

