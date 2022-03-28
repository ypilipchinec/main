import os
import time
from datetime import datetime, timedelta

#main modules

from dbase import get_old_row, delete_row

def get_date():
    days_to_subtract = 90
    date = datetime.today() - timedelta(days=days_to_subtract)
    date = date.strftime("%Y-%m-%d")
    
    return date

def get_row():
    date = get_date()
    return get_old_row(date)
    
def main():
   old_row = get_row()
   path = os.path.dirname(os.path.dirname(os.getcwd()))
   #print(path)
   for row in old_row:
       #print(row[2])
       del_old_folder = path + row[2] 
       #print(del_old_folder)
       if os.path.exists(del_old_folder):
           filename = del_old_folder + "/" + row[3]
           if os.path.isfile(filename):
              delete_row(row[3])
           
       

if __name__ == '__main__':
    main()


