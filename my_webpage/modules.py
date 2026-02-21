import psycopg2
import datetime
import config


def connect_db_local():

    #create connection to postgres
    #all credentials are stored in config.py file in the same repo as app.py and modules.py
    try:
        conn = psycopg2.connect(database=config.DB_NAME,
                                user=config.DB_USER,
                                password=config.DB_PASS,
                                host=config.DB_HOST,
                                port=config.DB_PORT)
        print("Database connected successfully")
        return conn
    except Exception as e:

        print("Error during database connection "+str(e))
        log_to_db("my_webpage","connect_to_db", "Error"+str(e))
        return 0



def log_to_db(app,description, status):
    #connect to db
    conn = connect_db_local()
    insert_query = '''INSERT INTO public.logs ("date","app","description","status") VALUES '''
    insert_query += "('"+str(datetime.datetime.now())+"','"+app+"','"+description+"','"+status+"'),"
    insert_query = insert_query[:-1]+";"
    print( insert_query )
    cur = conn.cursor()
    cur.execute(insert_query)
    conn.commit()
    conn.close()

def add_message_to_db(language, email, message):
    #connect to db
    conn = connect_db_local()
    insert_query = '''INSERT INTO public.web_messages (date, language, email, message, status) VALUES '''
    insert_query += "('"+str(datetime.datetime.now())+"','"+language+"','"+email+"','"+message+"','new'),"
    insert_query = insert_query[:-1]+";"
    print( insert_query )
    cur = conn.cursor()
    cur.execute(insert_query)
    conn.commit()
    conn.close()

