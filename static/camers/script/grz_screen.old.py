import os
import csv
import subprocess
import threading

from time import sleep

#собственные модули
from dbase import get_select_from_db
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
    
    tbl = 'grz'
    rows = get_select_from_db(tbl)
    path = create_catalogs(tbl)
    #создание csv
    #filecsv = open(os.path.dirname(path)+'/ip-'+tbl+'-failed.csv', 'w', newline='')
    #filewriter = csv.writer(filecsv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #цикл по итогу каталога
    #for row in rows:
    #    check = check_host(row[2], 554) #проверка доступности
    #    if check:
    #        print('Port: 554 in host ',row[2],' alive ')
    #        
    #        thread = threading.Thread(target=fmpeg, args=(row[3], row[1], path,))
    #        thread.start()        
    #    else:
    #        print('Host ',row[2],' not connect ')
    #        filewriter.writerow([row[1], row[2]])
    #        
    #    while threading.activeCount()>20:
    #        sleep(3)

    #main_thread = threading.currnetThread()
    #for thread in threading.enumerate():
    #    if thread is main_thread:
    #        continue
    #    thread.join()
    
    

if __name__ == '__main__':
    main()
