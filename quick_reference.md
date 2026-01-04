# Python Random Module - Quick Reference Guide

A cheat sheet for quick lookups while coding!

## 📥 Import

```python
import random
```

## 🎲 Core Functions

### Generate Random Numbers

```python
# Random decimal between 0.0 and 1.0
random.random()  # Example: 0.7392844928

# Random integer between a and b (both inclusive!)
random.randint(1, 6)  # Example: 4

# Random integer from range (stop not included)
random.randrange(10)       # 0 to 9
random.randrange(1, 10)    # 1 to 9
random.randrange(0, 21, 2) # 0, 2, 4, ..., 20 (even numbers)

# Random float between a and b
random.uniform(10.0, 20.0)  # Example: 15.73
```

## 📋 Working with Sequences

```python
items = ["A", "B", "C", "D", "E"]

# Pick ONE random item
random.choice(items)  # Returns: "C"

# Pick multiple items (with replacement - duplicates OK)
random.choices(items, k=3)  # Returns: ["A", "C", "A"]

# Pick multiple UNIQUE items (no replacement)
random.sample(items, k=3)  # Returns: ["B", "D", "A"]

# Shuffle list in-place (modifies original!)
random.shuffle(items)  # items is now shuffled
```

## ⚖️ Weighted Random Selection

```python
items = ["common", "uncommon", "rare"]
weights = [70, 25, 5]  # Probabilities

random.choices(items, weights=weights, k=1)  # More likely to get "common"
```

## 🔄 Reproducible Randomness

```python
# Set seed for reproducible results
random.seed(42)  # Same seed = same sequence

# Reset to unpredictable randomness
random.seed()  # or random.seed(None)
```

## 🎯 Quick Decision Table

| Need | Use | Example |
|------|-----|---------|
| One random item | `choice()` | `random.choice(["A", "B", "C"])` |
| Multiple items (can repeat) | `choices()` | `random.choices([1,2,3], k=5)` |
| Multiple unique items | `sample()` | `random.sample([1,2,3], k=2)` |
| Shuffle list | `shuffle()` | `random.shuffle(my_list)` |
| Random integer (range) | `randint()` | `random.randint(1, 10)` |
| Random decimal (0-1) | `random()` | `random.random()` |
| Random decimal (range) | `uniform()` | `random.uniform(1.5, 5.5)` |
| Dice roll | `randint()` | `random.randint(1, 6)` |
| Coin flip | `choice()` | `random.choice(["H", "T"])` |

## ⚡ Common Patterns

### Dice Roll
```python
dice = random.randint(1, 6)
```

### Coin Flip
```python
result = random.choice(["Heads", "Tails"])
```

### Random Percentage (0-100)
```python
percent = random.random() * 100
```

### Probability Check (30% chance)
```python
if random.random() < 0.3:
    print("Success! (30% chance)")
```

### Pick Random Index
```python
items = ["A", "B", "C", "D"]
index = random.randrange(len(items))
item = items[index]
# Better: use random.choice(items) instead!
```

### Generate Random String
```python
import string
password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
```

### Random Item from Range
```python
# Random number from 1 to 100
num = random.randint(1, 100)

# Random even number from 0 to 20
num = random.randrange(0, 21, 2)
```

## ⚠️ Common Mistakes

### ❌ Wrong: Forgetting randint includes both ends
```python
random.randint(1, 10)  # Can return 10!
```
### ✅ Right: Remember it's inclusive
```python
random.randint(1, 10)   # Returns 1-10 (both included)
random.randrange(1, 11) # Returns 1-10 (11 not included)
```

### ❌ Wrong: shuffle() returns None
```python
shuffled = random.shuffle(items)  # shuffled is None!
```
### ✅ Right: shuffle() modifies in-place
```python
items_copy = items.copy()
random.shuffle(items_copy)  # items_copy is shuffled
```

### ❌ Wrong: Using random for security
```python
password = str(random.randint(100000, 999999))  # NOT SECURE!
```
### ✅ Right: Use secrets module
```python
import secrets
password = secrets.randbelow(900000) + 100000  # SECURE
```

## 🔒 Security Considerations

| Purpose | Module | Example |
|---------|--------|---------|
| Games, simulations | `random` | `random.randint(1, 6)` |
| Passwords, tokens | `secrets` | `secrets.token_hex(16)` |
| Scientific computing | `numpy.random` | `np.random.rand(100)` |

```python
# ❌ Never use random for security
import random
token = random.randint(100000, 999999)  # PREDICTABLE!

# ✅ Always use secrets for security
import secrets
token = secrets.randbelow(900000) + 100000  # CRYPTOGRAPHICALLY SECURE
```

## 📊 Real-World Examples

### Password Generator
```python
import string
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(12))
```

### OTP Generator
```python
otp = ''.join(str(random.randint(0, 9)) for _ in range(6))
```

### Lottery Numbers
```python
numbers = random.sample(range(1, 50), k=6)
numbers.sort()
```

### Weighted Enemy Spawn
```python
enemies = ["Goblin", "Orc", "Dragon"]
weights = [70, 25, 5]
enemy = random.choices(enemies, weights=weights, k=1)[0]
```

## 🎓 Tips

1. **Use `choice()` for single items** - cleaner than `items[random.randrange(len(items))]`
2. **Use `sample()` for unique items** - no duplicates guaranteed
3. **Use `seed()` when debugging** - reproducible results make testing easier
4. **Copy before shuffling** - if you need to keep the original
5. **Use `secrets` for security** - never use `random` for passwords or tokens

---

For detailed explanations and more examples, see the [full tutorial](python_random_tutorial.md).
