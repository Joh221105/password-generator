import string
import random
from flask import Flask

app = Flask(__name__)


lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
symbols = list(string.punctuation)
numbers = list(string.digits)

password = []

def generate_elements(num, type_list):
    generated_element = random.choices(type_list, k=num)
    password.extend(generated_element)

def generate_password():
    
    password.clear()
    generate_password(num_lower_case, lower_case)
    generate_password(num_upper_case, upper_case)
    generate_password(num_symbol, symbols)
    generate_password(num_digits, numbers)

random.shuffle(password)

print(''.join(password))


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run()