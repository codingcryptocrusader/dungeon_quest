import random

# Step 1: Player Setup
player_name = input("Enter your name, brave adventurer: ")
health = 10
inventory = []

# Step 2: Treasure Dictionary
treasures = {
    "Emerald": 50,
    "Ruby": 60,
    "Gold Coin": 30,
    "Sapphire": 40,
    "Diamond": 70
}

# Step 3: Game Loop - Moving through 5 rooms
print(f"\nWelcome to the dungeon, {player_name}!\n")

for room in range(1, 6):
    print(f"\n--- Room {room} ---")
    while True:
        print("\nChoose an action:")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")
        choice = input("Enter your choice (1-4): ")

        # Step 4: Implement treasure search
        if choice == '1':
            found = random.choice(["treasure", "trap"])
            if found == "treasure":
                treasure_found = random.choice(list(treasures.keys()))
                inventory.append(treasure_found)
                print(f"You found a {treasure_found}! It's added to your inventory.")
            else:
                health -= 2
                print("A trap! You lose 2 health points.")
        
        elif choice == '2':
            print("You move cautiously to the next room...")
            break

        elif choice == '3':
            print(f"Health: {health}")
            print(f"Inventory: {inventory if inventory else 'Empty'}")

        elif choice == '4':
            print("You chose to leave the dungeon early.")
            break

        else:
            print("Invalid choice. Try again.")

        # Step 5: Check health
        if health <= 0:
            print("\nYou've run out of health. GAME OVER!")
            break

    if choice == '4' or health <= 0:
        break

# Step 6: End of Game Summary
print("\n--- Game Summary ---")
total_value = sum(treasures[item] for item in inventory)
print(f"Final Health: {health}")
print(f"Final Inventory: {inventory if inventory else 'None'}")
print(f"Total Treasure Value: {total_value} gold")

print(f"\nThanks for playing, {player_name}! Until next dungeon...")
