import re


def is_palindrome(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    sentence = re.sub(r'[^A-Za-z]', "", sentence)
    if len(sentence) <= 1:
        return True
    if sentence[0] != sentence[-1]:
        return False
    is_palindrome(sentence[1:len(sentence)-1])


def main():
    user_input = input("enter some text to determine if it is a palindrome: ")
# updated below line; previously said function == user input
    if is_palindrome(user_input):
        print("True!")
    else:
        print("False!")


if __name__ == '__main__':
    main()
