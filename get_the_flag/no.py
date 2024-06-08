import re

# Example regex pattern
pattern = r'execute\((.*?)\)'  # Look for a string 'execute()' followed by anything inside parentheses

# Example input string
input_string = "This is a test to execute(print('Hello, world!')) code from a regex match."

# Find the pattern in the input string
match = re.search(pattern, input_string)

# If there's a match, extract the code inside the parentheses
if match:
    code_to_execute = match.group(1)
    # Execute the code using exec
    exec(code_to_execute)
else:
    print("No match found.")
