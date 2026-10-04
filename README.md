# Week 2: Advanced Python & Data Structures
## IEEE LGU AI/ML Cohort One
**AI/ML Leads:** Abdullah Faisal & Alina Irshad

### 1. Project Overview
The **RPG Inventory Engine** is an object-oriented game inventory management system designed to handle player items like weapons, potions, and armor. The system dynamically loads items from external CSV save files while securely catching and recovering from corrupted or malformed records without crashing.

### 2. Concepts Implemented
- **Object-Oriented Programming (OOP):** Custom base class `Item` and specialized child classes (`Weapon`, `Potion`, `Armor`) utilizing inheritance, polymorphism, and method overriding
- **File Handling & Recovery:** Safe file reading using `open()`, `with`, and `try/except/finally` blocks to guarantee resource cleanup and skip corrupt rows gracefully.
- **Data Structures:** Lists, Sets (for unique categories), and Nested Dictionaries (organizing inventory items by category.
- **Comprehensions:** List comprehensions for high-performance filtering by item rarity and name.

### 3. How to Run the Program
python main.py

### 4. Dataset Information
File Location: data/items.csv   
Record Count: Contains 13 initial item entries.
Corrupt Test Cases Added: Intentionally included malformed records (e.g., Broken Item with non-numeric value abc and an Invalid Item with missing columns) to test and prove the exception recovery logic. 
