"""
Database initialization script
Supports both SQLite and MySQL databases
"""

import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()


def init_sqlite():
    """Initialize SQLite database"""
    try:
        db_path = 'medical_reports.db'
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Read SQL schema
        with open('schema_sqlite.sql', 'r') as f:
            sql_script = f.read()
        
        # Execute schema
        cursor.executescript(sql_script)
        conn.commit()
        conn.close()
        
        print(f"✓ SQLite database initialized: {db_path}")
        return True
    except Exception as e:
        print(f"✗ Error initializing SQLite database: {e}")
        return False


def init_mysql():
    """Initialize MySQL database"""
    try:
        import mysql.connector
        
        config = {
            'host': os.getenv('MYSQL_HOST', 'localhost'),
            'user': os.getenv('MYSQL_USER', 'root'),
            'password': os.getenv('MYSQL_PASSWORD', ''),
            'database': os.getenv('MYSQL_DATABASE', 'medical_reports_db')
        }
        
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        # Read SQL schema
        with open('schema_mysql.sql', 'r') as f:
            sql_script = f.read()
        
        # Execute schema
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print(f"✓ MySQL database initialized: {config['database']}")
        return True
    except Exception as e:
        print(f"✗ Error initializing MySQL database: {e}")
        return False


def main():
    """Main initialization function"""
    db_type = os.getenv('DATABASE_TYPE', 'sqlite').lower()
    
    print("=" * 50)
    print("Medical Report Processor - Database Initialization")
    print("=" * 50)
    
    if db_type == 'sqlite':
        success = init_sqlite()
    elif db_type == 'mysql':
        success = init_mysql()
    else:
        print(f"✗ Unknown database type: {db_type}")
        success = False
    
    if success:
        print("\n✓ Database initialization completed successfully!")
    else:
        print("\n✗ Database initialization failed!")
    
    return success


if __name__ == '__main__':
    main()
