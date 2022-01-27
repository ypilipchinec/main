import psycopg2
import csv
from datetime import datetime


def get_db_creds():
    """
    db_creds [get db credentials]

    Returns:
        [list]: [database credentials]
    """    
    db_creds = {
        "dbname": "rtspcamers",
        "user": "rtsp",
        "password": "P@$$w0rd",
        "host": "10.33.251.18",
        "port": "5432"
    }
    return db_creds
def insert_from_db(**values)->list:
    creds = get_db_creds()
    
    with psycopg2.connect(**creds) as conn:
        with conn.cursor() as cursor:
            insert_query = 'insert into screens_files (name, dir_path, file, status, create_at) values (%s, %s, %s, %s, %s)'
            values_db = (values['tbl'], values['dir_path'], values['file'], values['status'], values['create_at'])
            cursor.execute(insert_query, values_db)
            conn.commit()
            cursor.close()
        #conn.close()
        
def get_csv():
    created_at = ''
    with open('erros_files.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            #print(', '.join(row))
            print('name: ', row[0], '; dir_path: ', row[1], ' file: ', row[2], 'status: ', row[3], 'create_at: ', row[4])
            if row[3] == "True":
                status = True
                print(True)
            else:
                status = False
                print(False)
            created_at = datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f')
            print (created_at)
            insert_from_db(tbl = row[0], dir_path = row[1], file = row[2], status = status, create_at = created_at)
            
            
    


def main():
    csv = get_csv()
    print(csv)

if __name__ == '__main__':
    main()


