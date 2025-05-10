import os

import pandas as pd
import psycopg2
from datasets import load_dataset
from dotenv import load_dotenv
from psycopg2.extras import execute_values

# Load environment variables
load_dotenv()


def create_postgres_connection():
    """Create a connection to PostgreSQL database."""
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT", "5432")

    print(f"Connecting to PostgreSQL: {db_name}@{db_host}:{db_port} as {db_user}")
    return psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port
    )


def create_table(conn):
    """Create the reddit_posts table if it doesn't exist."""
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS reddit_posts (
                id TEXT PRIMARY KEY,
                author TEXT,
                content TEXT,
                subreddit TEXT,
                subreddit_id TEXT
            )
        """)
    conn.commit()


def load_dataset_to_postgres():
    print("Loading dataset...")
    dataset = load_dataset("reddit", split="train[:10000]", trust_remote_code=True)

    print("Connecting to PostgreSQL...")
    conn = create_postgres_connection()

    print("Converting to pandas DataFrame...")
    df = pd.DataFrame(dataset)

    try:
        print("Creating table...")
        create_table(conn)

        print("Preparing data...")

        columns = ["id", "author", "content", "subreddit", "subreddit_id"]
        data = df[columns].values.tolist()

        print("Inserting data...")
        with conn.cursor() as cur:
            execute_values(
                cur,
                """
                INSERT INTO reddit_posts (id, author, content, subreddit, subreddit_id)
                VALUES %s
                ON CONFLICT (id) DO UPDATE SET
                    author = EXCLUDED.author,
                    content = EXCLUDED.content,
                    subreddit = EXCLUDED.subreddit,
                    subreddit_id = EXCLUDED.subreddit_id
                """,
                data,
            )

        conn.commit()
        print("Data successfully loaded into PostgreSQL!")

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()

    finally:
        conn.close()


if __name__ == "__main__":
    load_dataset_to_postgres()
