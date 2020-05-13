    prompt = """
    Tell me something and I will repeat it after you!"
    Enter 'quit' to end the program: """

    while True:
        message = input(prompt)
        if message.lower().strip() in ['quit', 'q', 'exit', 'finito']:
            print("\nThanks for playing!")
            break
        print(f"\n{message}")