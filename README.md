# Mikrotik Login Bruteforce Tool

This is a Python-based bruteforce tool designed for testing the login credentials of Mikrotik routers. The tool uses a list of usernames and passwords to attempt login to the router.

## Requirements

- Python version >= 3.10.3
- Dependencies specified in `requirement.txt`

## Features

- Bruteforce Mikrotik login with a list of usernames and passwords
- Easy setup and usage

## Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/kansaok/mikrotik-bruteforce.git
cd mikrotik-bruteforce
```

### Step 2: Create a Python Virtual Environment

#### On Windows

```bash
python -m venv env
. env/Scripts/activate
```

#### On Mac/linux

```bash
python -m venv env
. env/bin/activate
```

### Step 3: Install Dependencies

Install the necessary dependencies listed in requirement.txt by running the following command:

```bash
pip install -r requirement.txt
```

### Usage

To run the bruteforce tool, use the following command:

```bash
python mkbf.py --h <mikrotik_ip> --u username.txt --p password.txt
```

Where:

- `-h`: The IP address of the Mikrotik router.
- `-u`: The file containing the list of usernames (username.txt).
- `-p`: The file containing the list of passwords (password.txt).

### Example

```bash
python mkbf.py --h 192.168.88.1 --u username.txt --p password.txt
```

### Files

- `mkbf.py`: The main script that performs the bruteforce attack.
- `username.txt`: Contains a list of usernames to test.
- `password.txt`: Contains a list of passwords to test.
- `requirement.txt`: Lists the Python dependencies required for the tool.

### Disclaimer

This tool is intended for educational and testing purposes only. Do not use it on networks or devices without permission. Unauthorized use of this tool is illegal and may result in criminal charges.

### License

This project is licensed under the [MIT License](https://github.com/kansaok/mikrotik-bruteforce?tab=MIT-1-ov-file) - see the LICENSE file for details.
