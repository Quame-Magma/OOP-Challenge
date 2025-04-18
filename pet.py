class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # start in the middle (0 = full, 10 = very hungry)
        self.energy = 5  # start in the middle (0 = tired, 10 = fully rested)
        self.happiness = 5  # start in the middle (0-10)
        self.tricks = []  # list to store learned tricks
    
    def eat(self):
        """Reduces hunger by 3 points (but not below 0), and increases happiness by 1."""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food! Yummy!")
    
    def sleep(self):
        """Increases energy by 5 points (but not above 10)."""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap and feels refreshed!")
    
    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1."""
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} had fun playing!")
    
    def get_status(self):
        """Prints the current state of the pet."""
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {'🍖' * self.hunger}{'⚪' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'⚡' * self.energy}{'⚪' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'😊' * self.happiness}{'⚪' * (10 - self.happiness)} ({self.happiness}/10)")
    
    def train(self, trick):
        """Teaches the pet a new trick and stores it in a list."""
        if trick in self.tricks:
            print(f"{self.name} already knows how to {trick}!")
        else:
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 1)  # Training takes energy
            self.happiness = min(10, self.happiness + 1)  # But makes the pet happy to learn
            print(f"{self.name} learned how to {trick}!")
    
    def show_tricks(self):
        """Prints all learned tricks."""
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"\n--- {self.name}'s Tricks ---")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")

# Example usage
if __name__ == "__main__":
    # Create a pet
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    
    print(f"Welcome to your new pet, {my_pet.name}!")
    my_pet.get_status()
    
    # Interactive menu
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Let your pet sleep")
        print("3. Play with your pet")
        print("4. Check your pet's status")
        print("5. Train your pet a new trick")
        print("6. Show your pet's tricks")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            my_pet.eat()
        elif choice == '2':
            my_pet.sleep()
        elif choice == '3':
            my_pet.play()
        elif choice == '4':
            my_pet.get_status()
        elif choice == '5':
            trick = input("What trick would you like to teach? ")
            my_pet.train(trick)
        elif choice == '6':
            my_pet.show_tricks()
        elif choice == '7':
            print(f"Goodbye! Take care of {my_pet.name}!")
            break
        else:
            print("Invalid choice. Please try again.")