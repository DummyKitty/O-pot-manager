from configparser import ConfigParser
import sqlite3
import json

if __name__ == '__main__':
    config = ConfigParser()
    # config.read_file()
    config.add_section("wordpress")

    d = {
        'mail.capstonetrading.org', '5da9a.22189.cn',
        'static-123.12.156.182-tataidc.co.in', 'duediva.com', 'countcore.com',
        'www.sharkbowfishing.com', 'twentytwo.ro',
        'let-s-all-vape41841.affiliatblogger.com', 'www.cese-ecg.com',
        'carwraps.bravesites.com', 'mail.edenvalehub.co.za',
        'bushsidecoaches.com.au', 'dreyerfoote.com',
        'hostmaster.remoteediting.online', 'nutrition.ira.hol.es',
        'crenshawlandscapes.com', 'dyog.jp',
        'internetmarketingstrategy61024.blogofoto.com', '173.204.serviscom.cz',
        'mail.cassaincloud.net'
    }
    for key, value in enumerate(d):
        config.set("wordpress", str(key), value)
    config.write(open("test.conf", "w"))

    con = sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute("create table services (type, domain, ip, port)")
    cur.execute("insert into services values (?, ?)", (who, age))
    con.commit()
    con.close()
