import sqlite3

#database connection
def connect():
    return sqlite3.connect("bank.db")

#create an accout
def create_account():
    name = input("Enter Name:")
    deposit = float(input("Initial Deposit:"))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO accounts (name, balance) VALUES (? , ?)",
        (name, deposit)
    )

    conn.commit()
    conn.close()

    print("Account Created!")

#deposit
def deposit():
    acc_id = int(input("Account ID: "))
    amount = float(input("Deposit amount: "))
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE accounts SET balance = balance + ? WHERE id = ?",
        (amount, acc_id)
    )    
    conn.commit()
    conn.close()

    print("Deposit successful!")

#withdraw

def withdraw():
    acc_id = int(input("Account ID: "))
    amount = float(input("Withdraw amount: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM accounts WHERE id = ?",
        (acc_id,))
    
    result = cursor.fetchone()

    if result:
        balance = result[0]

        if balance >= amount:
            cursor.execute(
                "UPDATE accounts SET balance = balance - ? WHERE id = ?",
                (amount, acc_id)
            )

            conn.commit()
            print("Withdrawal successful!")
        else:
            print("Not enough money..")

    else:
        print("Account not found.")
    conn.close()

#check balance
def check_balance():
    acc_id = int(input("Account ID: "))
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM accounts WHERE id = ?",
        (acc_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        print(f"Balance: ${result[0]:.2f}")
    else:
        print("Account not found.")

#list accounts

def list_accounts():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM accounts")

    accounts = cursor.fetchall()

    conn.close()

    print("\n --- Accounts ---")
    for acc in accounts:
        print(f"ID: {acc[0]} | Name: {acc[1]} | Balance: ${acc[2]:.2f}")

#menu system
def menu():
    while True:
        print("\n=== Elite Bank ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3.Withdraw")
        print("4. Check Balance")
        print("5. List Accounts")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            list_accounts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

#run program
if __name__ == "__main__":
    menu()

        