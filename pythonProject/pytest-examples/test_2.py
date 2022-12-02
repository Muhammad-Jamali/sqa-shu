import pytest

def setup_module(module):
    print("Creating DB Connection") #1

def teardown_module(module):
    print("Closing DB Connection") #5

def setup_function(function):
    print("Launching browser") #2

def teardown_function(function):
    print("Quiting  browser") #4

def test_do_login():
    print("Executing Login Test")#3

def test_register():
    print("Executing Register")


