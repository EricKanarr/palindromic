import re


def is_palindrome(sentence):
    sentence = re.sub(r'[^A-Za-z]', "", sentence)
    if len(sentence) <= 1:
        return True
    else:
        left = 0
        right = len(sentence) - 1
        while left < right:
            if sentence[left] == sentence[right]:
                left += 1
                right -= 1
                return True
            else:
                if sentence[left] != sentence[right]:
                    left += 1
                    right -= 1
                return False


def main():

    user_input = input("enter text, palindromic it might be: ")
    print(is_palindrome(user_input))
    # TODO: put your input/output code here
    pass


if __name__ == '__main__':
    main()
