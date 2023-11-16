try:
    with open("data.txt", "r") as file:
        # Perform operations with the file here
        # For example, you can read its content
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("The file 'data.txt' does not exist.")
except Exception as e:
    print("An unexpected error occurred:", e)
