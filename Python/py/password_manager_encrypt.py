import sqlite3
from hashlib import sha256

ADMIN_PASSWORD = "12"

connect = input("What is your password?\n")

while connect != ADMIN_PASSWORD:
    connect = input("Wrong Password...!! Try Again..\n")

conn = sqlite3.connect('pass_manager.db')


def encode1(l1):
    j = 0
    for i in l1:
        k = chr(ord(i) + 10)
        l1 = l1[:j] + k + l1[j+1:]
        j = j + 1
    return l1


def decode1(l2):
    j = 0
    for i in l2:
        k = chr(ord(i) - 10)
        l2 = l2[:j] + k + l2[j + 1:]
        j = j + 1
    return l2


def get_password(service1):
    cursor = conn.execute("SELECT (PASS_KEY) from KEYS WHERE SERVICE=" + '"' + service1 + '"')
    cursor1 = ""
    for row in cursor:
        cursor1 = row[0]
        jk = decode1(cursor1)
    return jk


def add_password(service1, np1):
    np2 = encode1(np1)
    command = 'INSERT INTO KEYS (PASS_KEY, SERVICE) VALUES   (%s, %s);' % ('"' + np2 + '"', '"' + service1 + '"',)
    conn.execute(command)
    conn.commit()
    print("\n Password stored Successfully")


if connect == ADMIN_PASSWORD:

    print("\n" + "*" * 15)
    print("Commands:")
    print("gp = get password")
    print("sp = store password")
    print("*" * 15)
    input_ = input("")

    if input_ == "sp":
        service = input("What is the name of the service?\n")
        np = input("\n Enter the password for " + service.capitalize() + "\n")
        add_password(service, np)
        exit()

    if input_ == "gp":
        service = input("What is the name of the service?\n")
        print("\n" + service.capitalize() + " password:\n" + get_password(service))
        exit()

    else:
        print('Wrong Selection')
