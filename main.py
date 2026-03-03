from app.calculator import Calculator
from app.history import AutoSaveObserver


def print_help():
    print("""
Available Commands:
add, subtract, multiply, divide
power, root, modulus, int_divide
percent, abs_diff
history
undo
redo
save
load
help
exit
""")


def main():
    calc = Calculator()

    # Optional auto-save observer (default file)
    auto_observer = AutoSaveObserver(calc)
    calc.add_observer(auto_observer)

    print("Advanced Calculator REPL")
    print("Type 'help' for commands.")

    while True:
        user_input = input("> ").strip()

        if not user_input:
            continue

        parts = user_input.split()

        command = parts[0].lower()

        try:
            if command == "exit":
                print("Goodbye.")
                break

            elif command == "help":
                print_help()

            elif command == "history":
                for item in calc.history:
                    print(item)

            elif command == "undo":
                if not calc.undo():
                    print("Nothing to undo.")

            elif command == "redo":
                if not calc.redo():
                    print("Nothing to redo.")

            elif command == "save":
                if calc.save_history():
                    print("History saved.")
                else:
                    print("Nothing to save.")

            elif command == "load":
                if calc.load_history():
                    print("History loaded.")
                else:
                    print("Could not load history.")

            else:
                if len(parts) != 3:
                    print("Invalid format. Example: add 2 3")
                    continue

                operation = command
                a = float(parts[1])
                b = float(parts[2])

                result = calc.calculate(operation, a, b)
                print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()