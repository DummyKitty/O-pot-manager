import os

yellow = '\033[01;33m'
white = '\033[01;37m'
green = '\033[01;32m'
blue = '\033[01;34m'
red = '\033[1;31m'
end = '\033[0m'
version = "1.0"
message = white + '{' + red + version + ' #dev' + white + '}'
BANNER = f"""{white}
O-pot manager is a convenient management tool{yellow}
   ____                    __                  
  / __ \      ____  ____  / /_                
 / / / /_____/ __ \/ __ \/ __/   {message}{green}               
/ /_/ /_____/ /_/ / /_/ / /_                   
\____/     / .___/\____/\__/                
   ____ __/_/____ _____  ____ _____ ____  _____ {blue}
  / __ `__ \/ __ `/ __ \/ __ `/ __ `/ _ \/ ___/ 
 / / / / / / /_/ / / / / /_/ / /_/ /  __/ /    {white}
/_/ /_/ /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                            /____/             
{red} having fun~{end} 
"""
CONFIF_PATH = 'conf.rc'
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
DATA_DIR = BASE_DIR + '/data/'
TEMPLATE_DIR = BASE_DIR + '/template/'
DATABASE_PATH = DATA_DIR + 'data.db'
CURRENT_REVERSE_PROXIES_PATH = DATA_DIR + 'current_reverse_proxy.txt'
CENSYS_UID = "b7baa610-b4c6-463e-af4b-dea66412ea0a"
CENSYS_SECRET = "hkOJASynWbs7obh26grY7h2xIWS4Ne9T"
ZOOMEYE_USERNAME = "3214436480@qq.com"
ZOOMEYE_PASSWORD = "aa15074520721"

if __name__ == "__main__":
    print(BANNER)