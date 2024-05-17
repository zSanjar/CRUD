from datetime import datetime
from typing import Optional

import psycopg2

conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        password='0123',
                        host='localhost',
                        port=5432)

cur = conn.cursor()

create_table_query = '''
    create table Users(
        id serial PRIMARY KEY,
        name varchar(100) not null ,
        phone_number int ,
        created_at timestamp default current_timestamp,
        updated_at timestamp default current_timestamp
    );
'''

def create_table():
    cur.execute(create_table_query)
    conn.commit()
    print('Successfully created table')

class Users:
    def __init__(self,
                 name: str,
                 phone_number: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None
                 ):
        self.name = name
        self.phone_number = phone_number
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()


    def save(self):
        insert_product_obj = '''
        insert into Users (name,phone_number,created_at,updated_at) 
        values (%s,%s,%s,%s);
        '''
        database = (self.name, self.phone_number, self.created_at, self.updated_at)
        cur.execute(insert_product_obj, database)
        conn.commit()
        print('Successfully saved data')

    @staticmethod
def get_all():
        select_users_all = '''select * from Users;'''
        cur.execute(select_users_all)
        rows = cur.fetchall()
        for i in rows:
            print(i)

    @staticmethod
def delete():
        delete_product_obj = '''
        delete from Users where id = %s;'''

        database = int(input('Enter the id of the user to delete: '))
        cur.execute(delete_product_obj, database)
        conn.commit()
        print('Successfully deleted data')

    @staticmethod
def update():
        update_project_obj = '''
        update Users set name=%s,phone_number=%s,updated_at=%s where id=%s;'''
        name = input('Enter new name of the user: ')
        phone_number = input('Enter new phone number: ')
        update_at = datetime.now()
        id_ = input('Enter id of the user to update: ')
        database = [name, phone_number, update_at]
        cur.execute(update_project_obj, database, id_)
        conn.commit()


while True:

    choice = input('which of the action do you want to do? '
                   '[create_table -- 1, delete_data -- 2, update_data -- 3, save_data, get_data -- 4?]: ')
    if choice == 1:
        create_table()
    elif choice == 2:
        delete()
    elif choice == 3:
        update()
    elif choice == 4:
        get_all()


