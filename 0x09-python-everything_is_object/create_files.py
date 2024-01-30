# Script to create files with names like "0-answer.txt", "1-answer.txt", ..., "28-answer.txt"

for i in range(29):  # Range is up to, but not including, 29
    filename = f"{i}-answer.txt"
    with open(filename, "w") as file:
        # You can add content to the file if needed, for example:
        file.write(f"This is file number {i}.")

print("Files created successfully.")
