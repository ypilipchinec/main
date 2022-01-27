from dbase import get_select_from_db, insert_from_db

def main():
    tbl = 'pes'
    ends = list()
    get_query = get_select_from_db(tbl)
    for item in get_query:
        ends += item[1]
    print(ends)

if __name__ == '__main__':
    main()
    