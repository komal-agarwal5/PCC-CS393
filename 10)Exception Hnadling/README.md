a. Below, we have provided a buggy code. Add a try/except clause so the code runs without errors. If a blog post didn’t get any likes, a ‘Likes’ key should be added to that dictionary with a value of 0.

blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13,
'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8,
'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1,
'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in blog_posts:

total_likes = total_likes + post['Likes']

b. The code below assigns the 5th letter of each word in 'food' to the new list fifth. However, the code currently produces errors. Insert a try/except clause that will allow the code to run and produce a list of the 5th letter in each word. If the word is not long enough, it should not print anything out. Note: The 'pass' statement is a null operation;nothing will happen when itexecutes.

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes",
"beef", "lox", "lemonade"]

fifth = []

for x in food:

fifth.append(x[4])

c. In Python, write an interactive calculator. Take input as command line arguments, which is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Check whether the input arguments are valid before computing the result:

If the input does not consist of 3 elements, raise a FormulaError, which
is a custom Exception.

Try to convert the first and third input to a float (like so: float_value =
float(str_value)). Catch any ValueError that occurs, and instead raise a
FormulaError

If the second input is not '+' or '-', again raise a FormulaError

If the input is valid, perform the calculation and print the result, else
print appropriate error messages and quit.

d. Imagine you have a file named data.txt. Open it for reading using Python code, but make sure to use a try block to catch an exception that arises if the file doesn't exist. Once you've verified your solution works with an actual file, delete the file and see if your try block is able to handle it.

Note that the exception we need to watch out for is FileNotFoundError


