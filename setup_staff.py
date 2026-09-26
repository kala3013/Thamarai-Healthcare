import mysql.connector
from mysql.connector import Error
import bcrypt

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'healthcare'
}

# Staff credentials
staff_data = {
    'staff_id': 'ADMIN001',
    'employee_id': 'ADMIN001',
    'name': 'System Admin',
    'email': 'admin@thamaraihealthcare.com',
    'phone': '04222626999',
    'department': 'Administration',
    'designation': 'System Administrator',
    'role': 'admin',
    'password': 'admin123'
}

try:
    # Connect to database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    # Hash the password
    hashed_password = bcrypt.hashpw(staff_data['password'].encode('utf-8'), bcrypt.gensalt(10)).decode('utf-8')
    
    # Check if staff already exists
    cursor.execute('SELECT id FROM staff WHERE staff_id = %s OR employee_id = %s', (staff_data['staff_id'], staff_data['employee_id']))
    existing = cursor.fetchone()
    
    if existing:
        # Update existing staff
        cursor.execute('''
            UPDATE staff 
            SET name = %s, email = %s, phone = %s, department = %s, designation = %s, 
                role = %s, password = %s, status = %s
            WHERE staff_id = %s OR employee_id = %s
        ''', (
            staff_data['name'],
            staff_data['email'],
            staff_data['phone'],
            staff_data['department'],
            staff_data['designation'],
            staff_data['role'],
            hashed_password,
            'active',
            staff_data['staff_id'],
            staff_data['employee_id']
        ))
        print(f"✓ Updated staff user: {staff_data['staff_id']}")
    else:
        # Insert new staff
        cursor.execute('''
            INSERT INTO staff (staff_id, employee_id, name, email, phone, department, designation, role, password, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            staff_data['staff_id'],
            staff_data['employee_id'],
            staff_data['name'],
            staff_data['email'],
            staff_data['phone'],
            staff_data['department'],
            staff_data['designation'],
            staff_data['role'],
            hashed_password,
            'active'
        ))
        print(f"✓ Created staff user: {staff_data['staff_id']}")
    
    connection.commit()
    print("\nStaff user setup completed successfully!")
    print(f"Employee ID: {staff_data['employee_id']}")
    print(f"Password: {staff_data['password']}")
    print(f"\nLogin at: http://localhost:5500/frontend/staff/login.html")
    
except Error as e:
    print(f"✗ Database error: {e}")
    print("\nMake sure:")
    print("1. MySQL is running")
    print("2. Database 'healthcare' exists")
    print("3. Username and password are correct in .env file")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()