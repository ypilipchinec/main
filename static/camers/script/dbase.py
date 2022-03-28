import psycopg2


def get_db_creds():
    """
    db_creds [get db credentials]

    Returns:
        [list]: [database credentials]
    """    
    db_creds = {
        "dbname": "rtsptest",
        "user": "rtsp",
        "password": "P@$$w0rd",
        "host": "10.33.251.18",
        "port": "5432"
    }
    return db_creds

def get_select_from_db(tbl) -> list:
    """
    get_select_from_db [извлечение списка из БД]

    Args:
        tbl ([string]): [table name]
    Returns:
        list: [select from table]
    """    
    creds = get_db_creds()
    with psycopg2.connect(**creds) as conn:
        with conn.cursor() as cursor:
            cursor.execute("select * from screens_camers where type = '"+tbl+"'")
            events_list = cursor.fetchall()
            return events_list
        

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

def get_old_row(date):
    creds = get_db_creds()
    with psycopg2.connect(**creds) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"select * from screens_files where create_at < '{date}'")
            get_row = cursor.fetchall()
            return get_row
        
def delete_row(filename):
    creds = get_db_creds()
    with psycopg2.connect(**creds) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"delete from screens_files where file = '{filename}'")
            conn.commit()
            cursor.close()