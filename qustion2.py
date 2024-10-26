def continuous_input():
    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting the program.")
            break
        print(f"You entered: {user_input}")

# Call the function to run it
continuous_input()e