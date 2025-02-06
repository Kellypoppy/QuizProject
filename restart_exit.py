def restart_or_exit():
    startover_exit = input("Would you like to restart or exit the program: ").upper()
    if startover_exit == "RESTART":
        print("Restarting...")
        from main import main
        main()
    elif startover_exit == "EXIT":
        print("Exiting the application... Goodbye!")
        input()

        # Exits the program entirely
        exit()
    else:
        print("Please enter either 'Restart' or 'Exit'.")
        restart_or_exit()