import statistics as st
import numpy as np
import os

def clear_screen():
    # Clears screen for Windows/Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_list():
    clear_screen()
    print("="*50)
    print("      📊 Welcome to Stats Calculator 📊")
    print("="*50)
    my_list = []
    try:
        num_items = int(input("\nEnter the number of items you want to operate on: "))
        for i in range(num_items):
            items = int(input(f"Enter number {i+1}: "))
            my_list.append(items)
    except ValueError:
        print("❌ Invalid input! Please enter integers only.")
        return get_user_list()
    
    print("\n✅ List Of Numbers:", my_list)
    return my_list

# Statistical operations
def mean(my_list):
    print("\n📌 Mean of the list is:", np.mean(my_list))

def median(my_list):
    print("\n📌 Median of the list is:", np.median(my_list))

def variance(my_list):
    print("\n📌 Variance of the list is:", np.var(my_list))

def mode(my_list):
    try:
        print("\n📌 Mode of the list is:", st.mode(my_list))
    except:
        print("\n❌ No unique mode found.")

def standard_deviation(my_list):
    print("\n📌 Standard Deviation of the list is:", np.std(my_list))

def probability():
    try:
        Favourable_Outcomes = int(input("\nEnter the number of favourable outcomes: "))
        Total_Outcomes = int(input("Enter the number of total outcomes: "))
        if Total_Outcomes == 0:
            print("❌ Total outcomes cannot be zero.")
        else:
            print("\n📌 The Probability is:", Favourable_Outcomes / Total_Outcomes)
    except ValueError:
        print("❌ Invalid input! Please enter integers only.")

# Menu Display
def show_menu():
    print("\n" + "="*50)
    print("Select the operation you want to perform:")
    print("1️⃣  Mean")
    print("2️⃣  Median")
    print("3️⃣  Variance")
    print("4️⃣  Mode")
    print("5️⃣  Standard Deviation")
    print("6️⃣  Probability")
    print("="*50)

def Operation_On_Calculator(number, my_list):
    if number == 1:
        mean(my_list)
    elif number == 2:
        median(my_list)
    elif number == 3:
        variance(my_list)
    elif number == 4:
        mode(my_list)
    elif number == 5:
        standard_deviation(my_list)
    elif number == 6:
        probability()
    else:
        print("❌ Invalid Operation! Try again by entering a number between 1 and 6.")

# Main Loop
while True:
    my_list = get_user_list()
    show_menu()
    try:
        number = int(input("🔢 Enter the number of the operation you want to perform: "))
        Operation_On_Calculator(number, my_list)
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
    
    # Ask if user wants to continue
    again = input("\n🔁 Do you want to perform another operation? (y/n): ").lower()
    if again != 'y':
        print("\n👋 Thank you for using the Stats Calculator! Goodbye!")
        break
