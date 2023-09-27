# Read input
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Initialize the result string
result = ""

# Loop through columns and rows to extract alphanumeric characters
for j in range(m):
    for i in range(n):
        char = matrix[i][j]
        if char.isalnum() and char != ' ':  # Check if character is alphanumeric
            result += char
        elif char != ' ' and (i == 0 or matrix[i - 1][j] != ' '):
            result += ' '  # Replace special characters and multiple spaces with a single space
print(result)
