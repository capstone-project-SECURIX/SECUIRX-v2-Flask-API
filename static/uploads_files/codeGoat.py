# Sample code with vulnerabilities

# Information Exposure Through Comments
password = "supersecret"
api_key = "myapikey"
# secret_key = "mysecretkey"
# password = "mysecretpassword"
# api_key = "apikey123"
# secret_key = "topsecretkey"
# password = "password123"
# api_key = "api_key_456"
# secret_key = "mysecret"
# This is a comment with no sensitive information

# SQL Injection
query = "select * from users where id = '1'"

# Command Injection
import os
command = "ls"
os.system(command)

# Path Traversal
def read_file(path):
    with open(path, "r") as file:
        content = file.read()
    return content

# Insecure Deserialization
import pickle
data = b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x06MyClass\x94\x93\x94.'
obj = pickle.loads(data)

# XSS (Cross-Site Scripting)
import requests
param = request.get("param")
print(param)

# CSRF (Cross-Site Request Forgery)
form_action = '<form action="https://malicious-site.com/steal" method="POST">'

# Insecure Randomness
import random
rand_num = random.randint(0, 100)

# Hardcoded Credentials
username = "admin"
password = "admin123"

# Unhandled Exceptions
try:
    value = 1 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

# Weak Cryptography
import hashlib
hash_value = hashlib.md5(b"message").hexdigest()

# Incorrect Regular Expressions
import re
pattern = re.compile(r'[a-z')

# Unvalidated Redirects and Forwards
def redirect(url):
    print("Redirecting to:", url)

# Information Disclosure in Error Messages
try:
    value = 1 / 0
except ZeroDivisionError as e:
    print("An error occurred:", str(e))
