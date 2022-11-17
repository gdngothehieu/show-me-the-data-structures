# Explanation Problem 2

## File Recursion


I made use of the recommended modules to print files in my current directory, and check a file and its extension.

    Time Complexity

        os.listdir("") -> O(n). Has to iterate over each item provided a list.

        os.path.isfile("") -> O(1). Checks one file at a time.

        "".endswith("") -> O(1). Checks suffix one at a time.

        Recursion - > O(n^2) Recursively calling fuction with inner for loop.

    Data Structures

        I used a list to store all files found. Append has a time complexity of O(1)

    Space Complexity

    O(N) - Recursive function's memory complexity is O(recursion depth)
