from configparser import ConfigParser

# config = ConfigParser()
# config.read("config.ini")
#
# print(config.get("locator","username"));
# print(config.get("locator","password"));

def readConfig(section,key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(section,key)

print(readConfig("locator","username"))