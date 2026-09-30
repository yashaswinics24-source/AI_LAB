room = {
    "A": input("Enter status of Room A (Clean/Dirty): ").strip().capitalize(),
    "B": input("Enter status of Room B (Clean/Dirty): ").strip().capitalize()
}

location = input("Enter initial location (A/B): ").strip().upper()

print("\n--- Vacuum Cleaner Agent ---")
print("Goal: Clean both Room A and Room B.\n")

while True:

    if room["A"] == "Clean" and room["B"] == "Clean":
        print("Goal Achieved! Both rooms are clean.")
        break

    print(f"Current Location: {location}")
    print(f"Room A: {room['A']} | Room B: {room['B']}")

    if room[location] == "Dirty":
        print(f"Action: SUCK in Room {location}")
        room[location] = "Clean"
    else:
        if location == "A":
            print("Action: MOVE RIGHT to Room B")
            location = "B"
        else:
            print("Action: MOVE LEFT to Room A")
            location = "A"

    print()