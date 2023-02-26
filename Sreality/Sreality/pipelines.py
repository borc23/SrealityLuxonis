# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class SrealityPipeline:
    def __init__(self):
        # Connect to the PostgreSQL database
        hostname = 'db'
        username = 'luxonis'
        password = 'luxonis'
        database = 'luxonis'

        try:
            self.connection = psycopg2.connect(
                host=hostname,
                user=username,
                password=password,
                dbname=database
            )
        except psycopg2.Error as e:
            print(f"Error connecting to database: {e}")
            raise e
        
        # Create a table in the database
        self.cur = self.connection.cursor()
        self.cur.execute("""
            DROP TABLE IF EXISTS sreality;
            CREATE TABLE IF NOT EXISTS sreality(
                id serial PRIMARY KEY, 
                title text,
                img_url text
            );
        """)
        
    def process_item(self, item, spider):
        # Insert scraped data into the database
        try:
            self.cur.execute(
                "INSERT INTO sreality (title, img_url) VALUES (%s, %s)",
                (item["title"], item["img_url"])
            )
            self.connection.commit()
            
        except psycopg2.Error as e:
            print(f"Error inserting data into database: {e}")
            self.connection.rollback()
            raise e
        
        return item

    def close_spider(self, spider):
        # Close the cursor and database connection when the spider is done
        self.cur.close()
        self.connection.close()