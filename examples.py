"""
Python Random Module Examples
==============================
This file contains runnable examples from the tutorial.
Run this file to see the random module in action!
"""

import random

def main():
    print("=" * 60)
    print("Python Random Module - Interactive Examples")
    print("=" * 60)
    print()
    
    # Example 1: Basic random number
    print("1. Generate a random decimal (0.0 to 1.0):")
    print(f"   Result: {random.random():.4f}")
    print()
    
    # Example 2: Dice roll
    print("2. Roll a 6-sided dice:")
    dice = random.randint(1, 6)
    print(f"   You rolled: {dice}")
    print()
    
    # Example 3: Random choice from list
    print("3. Pick a random fruit:")
    fruits = ["apple", "banana", "cherry", "orange", "grape"]
    chosen = random.choice(fruits)
    print(f"   Today's fruit: {chosen}")
    print()
    
    # Example 4: Multiple unique items (sample)
    print("4. Deal 5 playing cards (no duplicates):")
    cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    hand = random.sample(cards, k=5)
    print(f"   Your hand: {hand}")
    print()
    
    # Example 5: Shuffle a list
    print("5. Shuffle a playlist:")
    playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
    print(f"   Original: {playlist}")
    shuffled = playlist.copy()
    random.shuffle(shuffled)
    print(f"   Shuffled: {shuffled}")
    print()
    
    # Example 6: Weighted choices
    print("6. Enemy spawn with weighted probabilities:")
    enemies = ["Goblin", "Orc", "Dragon", "Skeleton"]
    weights = [40, 30, 5, 25]  # Dragon is rare (5%)
    spawned = random.choices(enemies, weights=weights, k=10)
    print(f"   10 enemies spawned: {spawned}")
    print()
    
    # Example 7: Coin toss simulation
    print("7. Flip a coin 20 times:")
    flips = [random.choice(["Heads", "Tails"]) for _ in range(20)]
    heads = flips.count("Heads")
    tails = flips.count("Tails")
    print(f"   Results: {flips}")
    print(f"   Heads: {heads} ({heads/20*100:.1f}%), Tails: {tails} ({tails/20*100:.1f}%)")
    print()
    
    # Example 8: Generate lottery numbers
    print("8. Generate lottery numbers (6 unique numbers from 1-49):")
    lottery = random.sample(range(1, 50), k=6)
    lottery.sort()
    print(f"   Your numbers: {lottery}")
    print()
    
    # Example 9: Random temperature
    print("9. Generate random temperature:")
    temp = random.uniform(15.0, 35.0)
    print(f"   Temperature: {temp:.1f}°C")
    print()
    
    # Example 10: Reproducible randomness with seed
    print("10. Reproducible randomness with seed:")
    random.seed(42)
    numbers1 = [random.randint(1, 100) for _ in range(5)]
    print(f"    First run:  {numbers1}")
    
    random.seed(42)  # Reset to same seed
    numbers2 = [random.randint(1, 100) for _ in range(5)]
    print(f"    Second run: {numbers2}")
    print(f"    Are they the same? {numbers1 == numbers2}")
    print()
    
    print("=" * 60)
    print("Tip: Run this file multiple times to see different results!")
    print("=" * 60)

if __name__ == "__main__":
    main()
