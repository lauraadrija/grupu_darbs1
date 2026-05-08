#links uz sql datubāzes skici: https://drawsql.app/teams/programmesana-26/diagrams/kafejnicutiklssql
import sqlite3
# Izveidojam savienojumu ar datubāzi
conn = sqlite3.connect('kafejnica.db')
cursor = conn.cursor()

# SQL tabulas izveide
sql_script = """
CREATE TABLE IF NOT EXISTS Cafe (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    address TEXT
);

CREATE TABLE IF NOT EXISTS Employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    number TEXT,
    position TEXT,
    on_vacation BOOLEAN DEFAULT 0,
    cafe_id INTEGER,
    FOREIGN KEY (cafe_id) REFERENCES Cafe(id)
);

CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_sum DECIMAL(10, 2) NOT NULL,
    order_date DATE NOT NULL,
    description TEXT,
    employees_id INTEGER,
    FOREIGN KEY (employees_id) REFERENCES Employees(id)
);

INSERT INTO Cafe (title, address) VALUES ('Pie Jāņa', 'Brīvības iela 10'), ('Kafijas Stūris', 'Baznīcas iela 5'), ('Gardēdis', 'Rīgas iela 20');
INSERT INTO Employees (first_name, last_name, number, position, on_vacation, cafe_id) VALUES ('Jānis', 'Bērziņš', '+37120000000', 'viesmīlis', 1, 1), ('Anna', 'Kalniņa', '+37121111111', 'barista', 0, 1), ('Juris', 'Ozoliņš', '+37122222222', 'menedžeris', 0, 2);
INSERT INTO Orders (order_sum, order_date, description, employees_id) VALUES (249.99, '2024-04-01', 'Produkti atvēršanai', 1), (15.50, '2024-04-02', 'Kafijas pupiņas', 2), (50.00, '2024-04-03', 'Saimniecības preces', 3);
"""

cursor.executescript(sql_script)
conn.commit()
print("Datubāze veiksmīgi izveidota un dati ievadīti!")

conn.close()

import sqlite3

# Pievienojos datubāzei, lai atlasītu datus, kas jāizvada
conn = sqlite3.connect('kafejnica.db')
cursor = conn.cursor()

# 2.1. Darbinieki, kas pašlaik ir atvaļinājumā
query_2_1 = """
SELECT first_name, last_name 
FROM Employees 
WHERE on_vacation = 1;
"""

# 2.2. Pasūtījumu kopējais skaits
query_2_2 = """
SELECT COUNT(*) AS total_orders 
FROM Orders;
"""

# 2.3. Katra darbinieka pasūtījumu kopējais skaits
query_2_3 = """
SELECT e.first_name, e.last_name, COUNT(o.id) AS order_count
FROM Employees e
LEFT JOIN Orders o ON e.id = o.employees_id
GROUP BY e.id;
"""

# 2.4. Katra darbinieka pasūtījumu vislielākā summa
query_2_4 = """
SELECT e.first_name, e.last_name, MAX(o.order_sum) AS max_order_sum
FROM Employees e
JOIN Orders o ON e.id = o.employees_id
GROUP BY e.id;
"""

# 2.5. Katras kafejnīcas pasūtījumu vidējā summa
query_2_5 = """
SELECT c.title, AVG(o.order_sum) AS avg_order_sum
FROM Cafe c
JOIN Employees e ON c.id = e.cafe_id
JOIN Orders o ON e.id = o.employees_id
GROUP BY c.id;
"""
#svītriņas
print("-" * 30)

#IZVADU ATLASĪTOS DATUS
# 2.1. Darbinieki, kas pašlaik ir atvaļinājumā
cursor.execute("SELECT first_name, last_name FROM Employees WHERE on_vacation = 1;")
print("2.1. Darbinieki atvaļinājumā:", cursor.fetchall())

# 2.2. Pasūtījumu kopējais skaits
cursor.execute("SELECT COUNT(*) FROM Orders;")
print("2.2. Pasūtījumu kopējais skaits:", cursor.fetchone()[0])

# 2.3. Katra darbinieka pasūtījumu kopējais skaits
cursor.execute("""
    SELECT e.first_name, e.last_name, COUNT(o.id) 
    FROM Employees e 
    LEFT JOIN Orders o ON e.id = o.employees_id 
    GROUP BY e.id;
""")
print("2.3. Darbinieku pasūtījumu skaits:", cursor.fetchall())

# 2.4. Katra darbinieka pasūtījumu vislielākā summa
cursor.execute("""
    SELECT e.first_name, e.last_name, MAX(o.order_sum) 
    FROM Employees e 
    JOIN Orders o ON e.id = o.employees_id 
    GROUP BY e.id;
""")
print("2.4. Darbinieku pasūtījumu max summas:", cursor.fetchall())

# 2.5. Katras kafejnīcas pasūtījumu vidējā summa
cursor.execute("""
    SELECT c.title, AVG(o.order_sum) 
    FROM Cafe c 
    JOIN Employees e ON c.id = e.cafe_id 
    JOIN Orders o ON e.id = o.employees_id 
    GROUP BY c.id;
""")
print("2.5. Kafejnīcu pasūtījumu vidējās summas:", cursor.fetchall())

#svītriņas
print("-" * 30)
conn.close()