import os

BANNER = """
    ███████                                   █████                        
  ███░░░░░███                                ░░███                         
 ███     ░░███            ████████   ██████  ███████                       
░███      ░███ ██████████░░███░░███ ███░░███░░░███░                        
░███      ░███░░░░░░░░░░  ░███ ░███░███ ░███  ░███                         
░░███     ███             ░███ ░███░███ ░███  ░███ ███                     
 ░░░███████░              ░███████ ░░██████   ░░█████                      
   ░░░░░░░                ░███░░░   ░░░░░░     ░░░░░                       
                          ░███                                             
                          █████                                            
                         ░░░░░                                             
                                                                           
                                                                           
 █████████████    ██████   ████████    ██████    ███████  ██████  ████████ 
░░███░░███░░███  ░░░░░███ ░░███░░███  ░░░░░███  ███░░███ ███░░███░░███░░███
 ░███ ░███ ░███   ███████  ░███ ░███   ███████ ░███ ░███░███████  ░███ ░░░ 
 ░███ ░███ ░███  ███░░███  ░███ ░███  ███░░███ ░███ ░███░███░░░   ░███     
 █████░███ █████░░████████ ████ █████░░████████░░███████░░██████  █████    
░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░  ░░░░░███ ░░░░░░  ░░░░░     
                                                ███ ░███                   
                                               ░░██████                    
                                                ░░░░░░                     
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