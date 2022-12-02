import pytest

@pytest.mark.functional
def test_login_123():
    print("executing login test 123")

def test_login_345():
    print("executing login test 345")

@pytest.mark.regressional
def test_user_registration():
    print("executing user registration")

@pytest.mark.functional
def test_compose_email():
    print("executing compose email")

@pytest.mark.skip
def test_skip_test():
    print("skipping test")

#pytest .\test_4_markers.py -s -v -k "not login"
#pytest .\test_4_markers.py -s -v -k "user_registration"
#pytest .\test_4_markers.py -s -v -k "user"


#With markers
#pytest .\test_4_markers.py -s -v -m "functional"
#pytest .\test_4_markers.py -s -v -m "not functional"
