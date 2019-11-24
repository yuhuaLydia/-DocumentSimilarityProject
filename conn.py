
import pymysql
def connSQL():
    db = pymysql.connect("localhost","root","","Calculator")
    return db