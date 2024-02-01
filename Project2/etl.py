import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """Loads data in the staging tables.
    
    Gets song and log data from Amazon S3 cloud storage. Then it loads them into the 
    staging tables in Amazon Redshift DWH.
    
    Args:
        cur (cursor): The `cursor` object (from psycopg2) to the database session.
        conn (connection): The `connection` object (from psycopg2) to the database session.
        
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """Inserts the data from the staging tables to the actual tables in AWS Redshift.
    
    Inserts song and log data from the staging tables into the analytical tables 
    (see :func: sql_queries.insert_table_queries list).
    
     Args:
        cur (cursor): The `cursor` object (from psycopg2) to the database session.
        conn (connection): The `connection` object (from psycopg2) to the database session.
        
    """
    
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Main function 
    
    - Read the configuration file `dwh.cfg`.
    - Connects to the Redshift cluster.
    - Loads the data into the tables ( refer func : etl.load_staging_tables).
    - Insert the tables (refer func : etl.insert_tables).
    - Finally, close connection to the Redshift cluster.
    
    """
    
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
