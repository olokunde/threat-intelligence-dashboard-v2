import sqlite3
import json

DB_NAME = "threat_intel.db"


def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS threats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        indicator TEXT,
        type TEXT,
        score INTEGER,
        level TEXT
    )
    """)

    conn.commit()
    conn.close()


def calculate_level(score):
    if score >= 80:
        return "Critical"
    elif score >= 60:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"


def add_threat():
    indicator = input("Indicator (IP/Domain): ")
    threat_type = input("Type (IP/Domain): ").strip()
    if threat_type.upper() == "IP":
        threat_type = "IP"
    else:
        threat_type = threat_type.capitalize()

    while True:
        try:
            score = int(input("Threat Score (1-100): "))
            if 1 <= score <= 100:
                break
            print("Score must be between 1 and 100.")
        except ValueError:
            print("Please enter a valid integer.")

    level = calculate_level(score)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO threats(indicator,type,score,level)
    VALUES(?,?,?,?)
    """, (indicator, threat_type, score, level))

    conn.commit()
    conn.close()

    print("Threat saved successfully.\n")


def view_threats():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM threats")

    records = cursor.fetchall()

    print("\nThreat Intelligence Records\n")

    for record in records:
        print(
            f"ID:{record[0]} | "
            f"{record[1]} | "
            f"{record[2]} | "
            f"Score:{record[3]} | "
            f"Level:{record[4]}"
        )

    conn.close()


def search_threat():
    keyword = input("Enter indicator to search: ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM threats
    WHERE indicator LIKE ?
    """, ('%' + keyword + '%',))

    results = cursor.fetchall()

    if results:
        for record in results:
            print(
                f"ID:{record[0]} | "
                f"{record[1]} | "
                f"{record[2]} | "
                f"Score:{record[3]} | "
                f"Level:{record[4]}"
            )
    else:
        print("No results found.")

    conn.close()


def dashboard_summary():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM threats")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM threats WHERE level='Critical'"
    )
    critical = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM threats WHERE level='High'"
    )
    high = cursor.fetchone()[0]

    print("\nThreat Dashboard")
    print(f"Total Indicators: {total}")
    print(f"Critical Threats: {critical}")
    print(f"High Threats: {high}")

    conn.close()


def export_json():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT indicator,type,score,level
    FROM threats
    """)

    records = cursor.fetchall()

    data = []

    for record in records:
        data.append({
            "indicator": record[0],
            "type": record[1],
            "score": record[2],
            "level": record[3]
        })

    with open("threat_report.json", "w") as file:
        json.dump(data, file, indent=4)

    conn.close()

    print("JSON report exported.")


initialize_database()

while True:

    print("\nThreat Intelligence Dashboard V2")
    print("1. Add Threat")
    print("2. View Threats")
    print("3. Search Threat")
    print("4. Dashboard Summary")
    print("5. Export JSON Report")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_threat()

    elif choice == "2":
        view_threats()

    elif choice == "3":
        search_threat()

    elif choice == "4":
        dashboard_summary()

    elif choice == "5":
        export_json()

    elif choice == "6":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")