# RPG Inventory Engine
**Week 2: Advanced Python & Data Structures**
**IEEE LGU AI/ML Cohort One**
**AI/ML Leads: Abdullah Faisal & Alina Irshad**

## 1. Project Overview
The **RPG Inventory Engine** is an object-oriented game inventory management system designed to handle player items like weapons, potions, and armor. The system dynamically loads items from external CSV save files while securely catching and recovering from corrupted or malformed records without crashing.

## 2. Concepts Implemented
- **Object-Oriented Programming (OOP):** Custom base class `Item` and specialized child classes (`Weapon`, `Potion`, `Armor`) utilizing inheritance, polymorphism, and method overriding
- **File Handling & Recovery:** Safe file reading using `open()`, `with`, and `try/except/finally` blocks to guarantee resource cleanup and skip corrupt rows gracefully.
- **Data Structures:** Lists, Sets (for unique categories), and Nested Dictionaries (organizing inventory items by category.
- **Comprehensions:** List comprehensions for high-performance filtering by item rarity and name.

## 3. How to Run the Program
python main.py

## 4. Dataset Information
File Location: data/items.csv   
Record Count: Contains 13 initial item entries.
Corrupt Test Cases Added: Intentionally included malformed records (e.g., Broken Item with non-numeric value abc and an Invalid Item with missing columns) to test and prove the exception recovery logic. 

## 5. Execution Screenshots and Proof
<img width="881" height="377" alt="Program (2)" src="https://github.com/user-attachments/assets/589b7cac-fa07-4aee-bf81-9b3693bb875e" />
<img width="738" height="142" alt="Program (1)" src="https://github.com/user-attachments/assets/bd6d2263-0cbe-45e2-bf07-f1ac0be60b7c" />
<img width="762" height="290" alt="Program (4)" src="https://github.com/user-attachments/assets/be8bf114-b988-466a-861a-49a352f5647f" />
<img width="827" height="560" alt="Program (3)" src="https://github.com/user-attachments/assets/c7d3829c-0026-4bf1-b65a-3523d033aa62" />
