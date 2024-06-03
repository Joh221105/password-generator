import string
import random
from flask import Flask, render_template

app = Flask(__name__)


lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
symbols = list(string.punctuation)
numbers = list(string.digits)

password = []


def generate_elements(num, type_list):
    generated_element = random.choices(type_list, k=num)
    password.extend(generated_element)

def generate_password(length, bool_lower, bool_upper, bool_symbols, bool_numbers):

    password.clear()

    # keeps track of the number of elements in the generated password 
    count = 0

    while(count < length):

        if bool_lower:
            number_of_lower_case = random.randint(0, length//4)
            generate_elements(number_of_lower_case, lower_case)
            count += number_of_lower_case

        if bool_upper:
            number_of_upper_case = random.randint(0, length//4)
            generate_elements(number_of_upper_case, upper_case)
            count += number_of_upper_case

        if bool_symbols:
            number_of_symbols = random.randint(0, length//4)
            generate_elements(number_of_symbols, symbols)
            count += number_of_symbols

        if bool_numbers:
            number_of_digits = random.randint(0, length//4)
            generate_elements(number_of_digits, numbers)
            count += number_of_digits

    random.shuffle(password)
    if len(password) > length:
        del password[length:]

    return ''.join(password)


# @app.route("/")
# def home(name=None):
#     return render_template("index.html",name=name)

# @app.route("/generate")
# def generate_password():
#     password = generate_password(length, bool_lower, bool_upper, bool_symbols, bool_numbers)

# if __name__ == '__main__':
#     app.run()