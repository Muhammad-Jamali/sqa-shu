import pytest

#@pytest.fixture(scope='function') are called decorators

# def setup_module(module):
#     print("Creating DB Connection") #1
#
# def teardown_module(module):
#     print("Closing DB Connection") #5

#--------------------------------------------

@pytest.fixture(scope='module')
def setup():
    print("Creating DB Connection")

    yield
    print("Closing DB Connection")


@pytest.fixture(scope='function')
def before():
    print("Launching browser")

    yield
    print("Closing browser")


# def test_do_login(before,setup):
#     print("Executing Login Test")
#
#
# def test_register(before):
#     print("Executing Register")


# Another Way
#
@pytest.mark.usefixtures('setup', 'before')
def test_do_login():
    print("Executing Login Test")

@pytest.mark.usefixtures('setup', 'before')
def test_register():
    print("Executing Register")
