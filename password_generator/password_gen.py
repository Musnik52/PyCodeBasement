from random import randint, shuffle

from sqlalchemy import true


def main():
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    special_chars = '!@#$%^&*?~+=_-'
    answers = ['y', 'n', 'N', 'Y', 'no', 'NO', 'No', 'yes', 'Yes', 'YES']
    while True:
        try:
            print("Welcome to Password-Generator.")
            print(
                "Answer the following queries, so we know how complex you'd like your password to be.")
            password_length = int(
                input("How many characters long would you like your password to be? (must be 4 and above) Answer: "))
            while password_length < 4:
                password_length = int(input(
                    "How many characters long would you like your password to be? (must be 4 and above) Answer: "))
            include_numbers = input("Want to include numbers? Y/N: ")
            while include_numbers not in answers:
                include_numbers = input("Want to include numbers? Y/N: ")
            include_cap = input("Want to include capital letters? Y/N: ")
            while include_cap not in answers:
                include_cap = input("Want to include capital letters? Y/N: ")
            include_special = input(
                "Want to include special characters? Y/N: ")
            while include_special not in answers:
                include_special = input(
                    "Want to include special characters? Y/N: ")
            k = 1
            final_password = lower_letters[randint(0, len(lower_letters)-1)]
            full_password = lower_letters
            if include_cap in ['Y', 'y', 'yes', 'Yes', 'YES']:
                full_password = full_password+lower_letters.upper()
                k += 1
                final_password += lower_letters[randint(
                    0, len(lower_letters)-1)].upper()
            if include_special in ['Y', 'y', 'yes', 'Yes', 'YES']:
                full_password = full_password+special_chars
                k += 1
                final_password += special_chars[randint(
                    0, len(special_chars)-1)]
            if include_numbers in ['Y', 'y', 'yes', 'Yes', 'YES']:
                full_password = full_password+numbers
                k += 1
                final_password += numbers[randint(0, len(numbers)-1)]
            full_password = list(full_password)
            shuffle(full_password)
            for i in range(password_length-k):
                final_password += full_password[i]
            print(f"Your password is: {final_password}")
            break
        except:
            print('INVALID INPUT')
            continue


if __name__ == "__main__":
    main()
