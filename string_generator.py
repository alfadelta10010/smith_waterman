import random
import os

def generate_random_acgt(length):
    random_string = ''.join(random.choice('ATCG') for _ in range(length))
    return random_string

with open('output.txt', 'w') as file:
    file.write("300 x 500:\n")
    file.write(f"300: {generate_random_acgt(300)}\n")
    file.write(f"500: {generate_random_acgt(500)}\n\n")
    file.write("160 x 400:\n")
    file.write(f"160: {generate_random_acgt(160)}\n")
    file.write(f"400: {generate_random_acgt(400)}\n\n")
    file.write("80 x 200:\n")
    file.write(f"80: {generate_random_acgt(80)}\n")
    file.write(f"200: {generate_random_acgt(200)}\n\n")
    file.write("40 x 100:\n")
    file.write(f"40: {generate_random_acgt(40)}\n")
    file.write(f"100: {generate_random_acgt(100)}\n\n")
    file.write("181 x 181:\n")
    file.write(f"181: {generate_random_acgt(181)}\n")
    file.write(f"181: {generate_random_acgt(181)}\n\n")
