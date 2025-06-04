inp = "aabbbcddddeefffffff"

output = ""     # This will store the final result like "a2b3c1..."
count = 1       # We start counting from 1 because the first character appears at least once

# Start loop from the second character (index 1)
for i in range(1, len(inp)):
    # If current character is the same as the previous one, increment the count
    if inp[i] == inp[i - 1]:
        # print(inp[i])
        # print(inp[i - 1])
        count += 1
    else:
        # If character changes, store the previous character and its count
        output += inp[i - 1] + str(count)
        count = 1  # Reset count for the new character

# After the loop, add the last character group
output += inp[-1] + str(count)

print(output)