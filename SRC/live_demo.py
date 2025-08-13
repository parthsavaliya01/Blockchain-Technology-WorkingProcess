from Blockchain import Blockchain

print("BLOCKCHAIN TECHNOLOGY DEMONSTRATION")
print("=" * 50)

# Create blockchain
blockchain = Blockchain()

while True:
    print(f"\nBLOCKCHAIN DEMO MENU:")
    print("1. Add block without mining")
    print("2. Add block with custom difficulty") # nirmal->shivangi 10 books (difficulty = 4,5)
    print("3. Show full blockchain")
    print("4. Demonstrate tampering")
    print("5. Check blockchain validity")
    print("6. Exit")
    
    choice = input(f"\nEnter your choice (1-6): ").strip()
    
    if choice == "1":
        data = input("Enter transaction data: ")
        blockchain.add_block(data, difficulty=0)
        
    elif choice == "2":
        data = input("Enter transaction data: ")
        try:
            difficulty = int(input("Enter difficulty: "))
            print(f"\nMINING WITH DIFFICULTY {difficulty} (needs {difficulty} zeros)")
            blockchain.add_block(data, difficulty=difficulty)
        except ValueError:
            print("Please enter a valid number!")
            
    elif choice == "3":
        blockchain.print_chain()
        
    elif choice == "4":
        blockchain.demonstrate_tampering()
        
    elif choice == "5":
        valid = blockchain.is_valid()
        if valid:
            print("Blockchain is VALID!")
        else:
            print("Blockchain is INVALID!")

    elif choice == "6":
        print("Thanks! Exiting...")
        break
        
    else:
        print("Invalid choice! Please try again.")


