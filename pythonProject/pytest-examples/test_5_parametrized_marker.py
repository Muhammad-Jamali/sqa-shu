import pytest


#DDT : Data-Driven Tests

#array array = ["a","b"]
#tuble tuple = ("a","b","c") #immmutable

#array[0]="c"
#tuple[0]="c"

def get_data():
    #json, excel
    #Array of tuples
    return [
        ("abc@yahoo.com", "12345"),
        ("def@yahoo.com", "11111"),
        ("ghi@yahoo.com", "55555"),
        ("ppp@yahoo.com", "66666")
    ]


# @pytest.mark.parametrize("u,p", get_data())
# def test_dologin(u, p):
#     print(u, "---", p)

@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password):
    print(username, "---", password)


@pytest.mark.parametrize("username,password", [
        ("abc@yahoo.com", "12345"),
        ("def@yahoo.com", "11111"),
        ("ghi@yahoo.com", "55555"),
        ("ppp@yahoo.com", "66666")
    ])
def test_dologin(username, password):
    print(username, "---", password)