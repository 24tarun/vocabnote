import os
import django
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'baseapp.settings')
django.setup()

from django.db import connection

def test_database_connection():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            
        print("✅ Successfully connected to the database!")
        print(f"Database version: {db_version[0]}")
        
        # Display connection details (except password)
        db_settings = connection.settings_dict
        print("\nDatabase connection details:")
        print(f"Name: {db_settings['NAME']}")
        print(f"User: {db_settings['USER']}")
        print(f"Host: {db_settings['HOST']}")
        print(f"Port: {db_settings['PORT']}")
        return True
    except Exception as e:
        print("❌ Failed to connect to the database:")
        print(str(e))
        return False

if __name__ == "__main__":
    test_database_connection()
