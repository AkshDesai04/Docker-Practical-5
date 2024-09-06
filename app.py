import mysql.connector

# Database configuration
config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql',  # Use service name defined in docker-compose
    'database': 'testdb'
}

def create_connection():
    try:
        connection = mysql.connector.connect(**config)
        print("Connected to MySQL database successfully")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def insert_data(name, position, salary):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        query = "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, position, salary))
        connection.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def select_data():
    connection = create_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM employees"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Example usage
# insert_data('John Doe', 'Developer', 55000)
# select_data()
