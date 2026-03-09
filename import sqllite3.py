import sqlite3

# podcliuchenie k base
conn = sqllite3.connect('mydatabase.db')
cursor = conn.cursor()

# sozdanie tablici
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	age InTEGER NOT NULL
	grade TEXT 
)''')
conn.commit()


def add_user():
    name = input("Vvedite imya polzovatelya: ")
    age = int(input("Vvedite vozrast polzovatelya: "))
    grade = input("Vvedite ocenku: ")
    cursor.execute(
        "INSERT INTO users (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print("Polzovatel dobavlen uspeshno!")


def view_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    if users:
        print("Spisok polzovateley:")
        for user in users:
            print(
                f"ID: {user[0]}, Imya: {user[1]}, Vozrast: {user[2]}, Ocenka: {user[3]}")
    else:
        print("Net polzovateley v baze dannyh.")


def delete_user():
    user_id = int(input("Vvedite ID polzovatelya dlya udalenia: "))
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print("Polzovatel udalen uspeshno!")


def search_user():
    name = input("Vvedite imya polzovatelya dlya poiska: ")
    cursor.execute("SELECT * FROM users WHERE name LIKE ?",
                   ('%' + name + '%',))
    users = cursor.fetchall()
    if users:
        print("Naydennye polzovateli:")
        for user in users:
            print(
                f"ID: {user[0]}, Imya: {user[1]}, Vozrast: {user[2]}, Ocenka: {user[3]}")
    else:
        print("Polzovatel ne nayden.")


while true:
    print("\nMenu:")
    print("1. Dobavit polzovatelya")
    print("2. Posmotret spisok polzovateley")
    print("3. Udalit polzovatelya")
    print("4. Poisk polzovatelya")
    print("5. Viyti")

    choice = input("Vvedite nomer deystviya: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        view_users()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        search_user()
    elif choice == '5':
        print("Viyti iz programmy.")
        break
    else:
        print("Nepravilnyy vybor. Poprobuyte snova.")
