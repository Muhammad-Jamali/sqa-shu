import pytest

def test_validate_titles():
    expected_title = "Google.com"
    actual_title = "Gmail.com"
    title = "This is Gmail website"

    # if actual_title == expected_title:
    #     print("Test case pass")
    # else:
    #     print("Test case fail")

    #By default test will be broken after assertion failure
    print("Beginning")
    assert expected_title == actual_title, "Titles are not matching"
    assert "Gmails" in title, "Gmail does not exists in the title"
    assert False, "forcefully failing the test"
    print("Ending")

    #soft assertion
    #pip install pytest-soft-assertions

    #pytest .\test_6_asserions.py -s -v
    #pytest.\test_6_asserions.py - s - v - -soft - asserts



