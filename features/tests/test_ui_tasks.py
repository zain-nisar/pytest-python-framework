"""validate coinmarketcap UI feature tests."""

from features.businesslogic.ui_functions import ValidateUIElements
from pytest_bdd import (given,scenario, then, when, parsers)

obj_ValidateUIElements = ValidateUIElements()


@scenario(r'ui_tasks.feature', 'coinmarketcap dropdown verification')
def test_coinmarketcap_dropdown_verification():
    """coinmarketcap dropdown verification."""


@scenario(r'ui_tasks.feature', 'coinmarketcap filter verification')
def test_coinmarketcap_filter_verification():
    """coinmarketcap filter verification."""


@when(parsers.parse('user clicks on "{Filters}" button'))
def user_clicks_on_filters_button(Filters):
    """user clicks on "Filters" button."""
    obj_ValidateUIElements.click_filter(Filters)


@when(parsers.cfparse('user navigates to "{url}" page'))
def user_navigates_to_httpscoinmarketcapcom_page(url):
    """user navigates to "https://coinmarketcap.com" page."""
    obj_ValidateUIElements.navigate(url)


@when(parsers.parse('user select "{Filter}" value "{value}"'))
def user_select_marketcap_value(Filter,value):
    """user select "Filter" and value."""
    obj_ValidateUIElements.select_Filter_values(Filter,value)


@when('user select "Show rows" dropdown value to "100"')
def user_select_show_rows_dropdown_value_to_100():
    """user select "Show rows" dropdown value to "100"."""
    obj_ValidateUIElements.click_dropdown()


@then(parsers.cfparse('the user should see "{rows}" rows displayed on the page'))
def the_user_should_see_100_rows_displayed_on_the_page(rows):
    """the user should see "100" rows displayed on the page."""
    assert obj_ValidateUIElements.count_table_rows(rows)


@then('the user should see correct record on the page')
def the_user_should_see_correct_record_on_the_page():
    """the user should see correct record on the page."""
    obj_ValidateUIElements.validate_filter_results()

