import sqlite3
connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()

cursor.execute("INSERT INTO tickets (title, reporter) VALUES ('Printer offline', 'Musa')")
cursor.execute("INSERT INTO tickets (title, reporter, priority) VALUES ('VPN dropping', 'Ngozi', 'high')")
cursor.execute( "INSERT INTO tickets (title, reporter, priority) VALUES ('Network issue', 'Aisha', 'high')")
connection.commit()

cursor.execute("SELECT * FROM tickets")
for row in cursor.fetchall():
    print(row)

    connection.close()

    from db import get_all_tickets, get_ticket

    for row in get_all_tickets():
        print(row["id"], row["title"], row["status"])

    print(get_ticket(1)["title"])
    print(get_ticket(999))
        
from db import get_tickets_by_status

rows = get_tickets_by_status("open")

for row in rows:
    print(row["id"], row["title"], row["status"])

    import sqlite3

connection = sqlite3.connect("tickets.db")

title = "O'Brien's laptop"

query = "SELECT * FROM tickets WHERE title = ?"

connection.execute(query, (title,))

print("Query worked!")

connection.close()

from db import get_tickets_by_status

rows = get_tickets_by_status("open")

for row in rows:
    print(row["id"], row["title"], row["status"])

from db import get_all_tickets

tickets = get_all_tickets()

for ticket in tickets:
    print(ticket["id"], ticket["title"], ticket["reporter"], ticket["priority"], ticket["status"])    

 connection.execute("UPDATE tickets SET category_id = ? WHERE id = ?", (2, 1))   