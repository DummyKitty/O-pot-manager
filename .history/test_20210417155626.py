from configparser import ConfigParser

if __name__ == '__main__':
    config = ConfigParser()
    # config.read_file()
    config.add_section("wordpress")
    config.write(open("test.conf", "w"))
