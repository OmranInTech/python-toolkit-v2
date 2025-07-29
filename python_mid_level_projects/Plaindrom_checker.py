#palindrome_checker

#define function
def palindrome_checker(arr):
    arr = arr.lower().replace(" ", "")  # Normalize input by removing spaces and converting to lowercase
    palindrome = arr[::-1]  # Reverse the input

    if arr == palindrome:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"

#call function and print resutl
print(palindrome_checker("abca"))  # Example usage
