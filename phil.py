def calculate_velocity():
    try:
        distance = float(input("Enter distance (meters): "))
        time = float(input("Enter time (seconds): "))
        
        if time == 0:
            print("Error: Time cannot be zero (division by zero is undefined).\n")
            return
            
        velocity = distance / time
        print(f"Result: Velocity = {velocity:.2f} m/s\n")
        
    except ValueError:
        print("Error: Please enter valid numerical values only.\n")

def calculate_force():
    try:
        mass = float(input("Enter mass (kg): "))
        acceleration = float(input("Enter acceleration (m/s^2): "))
        
        force = mass * acceleration
        print(f"Result: Force = {force:.2f} N\n")
        
    except ValueError:
        print("Error: Please enter valid numerical values only.\n")

def main():
    while True:
        print("=== Physics Operations Menu ===")
        print("1. Calculate Velocity")
        print("2. Calculate Force")
        
        choice = input("Choose an option (1 or 2): ").strip()
        
        if choice == '1':
            calculate_velocity()
        elif choice == '2':
            calculate_force()
        else:
            print("Invalid choice. Please select 1 or 2.\n")
            continue
            
        # Ask the user if they want to continue
        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()
