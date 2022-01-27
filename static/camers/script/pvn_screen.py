import os, os.path
import csv
import subprocess
import threading

from time import sleep
from datetime import datetime
#from pathlib import Path

#собственные модули
from dbase import get_select_from_db, insert_from_db, get_arguments
from checkaddress import check_host
from dirs import create_catalogs
'''
надо подумать что писать
'''
def fmpeg(link, name, dirs):
    """
    fmpeg [выполнение внешней команды ffmpeg]
    [создание скриншотов по протоколу rtsp]
    """        
    subprocess.call('ffmpeg -y -rtsp_transport tcp -i '+link+' -s 1920x1080 -ss 00:00:04 -f image2 -frames:v 1 '+dirs+'/'+name+'.jpeg', shell=True)


def main():
    """
    main [итоговая функция создания скриншотов]
    """
    
    table_name = 'pvn'
    now = datetime.now().strftime("%d%m%Y-%H%M") #текущее время
    created_at = datetime.now()
    rows = get_select_from_db(table_name)
    path = create_catalogs(table_name, now)
    new_path = path[path.find("c/")+1:]
    #создание csv
    #filecsv = open(os.path.dirname(path)+'/ip-'+tbl+'-failed.csv', 'w', newline='')
    #filewriter = csv.writer(filecsv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #цикл по итогу каталога
    for row in rows:
        check = check_host(row[3], 554) #проверка доступности
        if check:
            print('Port: 554 in host ',row[3],' alive ')
            
            thread = threading.Thread(target=fmpeg, args=(row[4], row[2], path,))
            thread.start()

            insert_from_db(tbl = table_name, dir_path = new_path, file = row[2]+'.jpeg', status = True, create_at = created_at)        
        else:
            print('Host ',row[2],' not connect ')
            insert_from_db(tbl = table_name, dir_path = '', file = row[2]+'.jpeg', status = False, create_at = created_at)
 #           filewriter.writerow([row[1], row[2]])
            
        while threading.activeCount()>20:
            sleep(3)

    main_thread = threading.currentThread()
    for thread in threading.enumerate():
        if thread is main_thread:
            continue
        thread.join()
    

if __name__ == '__main__':
    main()
