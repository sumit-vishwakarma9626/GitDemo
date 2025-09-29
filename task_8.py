user_input = input("Enter some data: ")
with open("sample.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append more data
extra_input = input("Enter additional data to append: ")
with open("sample.txt", "a") as file:
    file.write(extra_input + "\n")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open("sample.txt", "r") as file:
    print(file.read()) 