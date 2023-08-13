import os
import pytest
import pyodbc
import json


@pytest.fixture
def database_connection():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_file_path = os.path.join(current_dir, '..', 'credentials.json')
    
    with open(credentials_file_path, 'r') as file:
        credentials = json.load(file)
    
    if "username" not in credentials or "password" not in credentials:
        raise ValueError("Missing username or password in credentials.json")
    
    with pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=EPBYBREW00A1\\SQLEXPRESS;'
                        'DATABASE=TRN;'
                        f'UID={credentials["username"]};'
                        f'PWD={credentials["password"]}') as connect:
        with connect.cursor() as cursor:
            yield cursor
