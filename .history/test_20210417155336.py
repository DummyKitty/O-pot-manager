from configparser import ConfigParser

if __name__ == '__main__':
    config = ConfigParser()
    config.read_file(open("test.conf", "a"))
    config.write()