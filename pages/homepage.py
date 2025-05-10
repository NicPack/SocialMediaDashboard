import os

import psycopg2
import streamlit as st

# Fetch env variables
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")


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


st.write(
    """<style>
            .block-container{
                height:400px;
                overflow:scroll
            }
            </style>
            """,
    unsafe_allow_html=True,
)

with st.expander("Expander with scrolling content"):
    with st.container(height=200):
        st.write("Inside scrolling container")
