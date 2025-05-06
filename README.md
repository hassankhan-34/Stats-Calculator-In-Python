# Stats-Calculator-In-Python

📝 **Description of the Statistics Calculator Code**

This Python program is a **command-line statistics calculator** that allows the user to perform various statistical operations on a list of numbers entered by the user. It includes a **menu-driven interface** and supports repeated usage until the user decides to exit.


🔧 **Key Features:**

1. **User Input Handling:**

   * Prompts the user to enter how many numbers they want to operate on.
   * Accepts integers and stores them in a list.

2. **Statistical Functions Implemented:**

   * **Mean**: Calculates the average of the numbers using NumPy.
   * **Median**: Finds the middle value.
   * **Variance**: Measures the spread of the numbers.
   * **Mode**: Identifies the most frequent value using the statistics module.
   * **Standard Deviation**: Calculates how much values deviate from the mean.
   * **Probability**: Computes basic probability using favorable and total outcomes.

3. **User Interface:**

   * Uses text-based formatting and emojis for clarity and appeal.
   * Provides a menu for users to choose the operation.
   * Automatically clears the screen and shows fresh prompts for better readability.

4. **Error Handling:**

   * Handles invalid numeric inputs gracefully using `try-except`.
   * Prevents division by zero in probability calculation.
   * Informs the user if no unique mode is found.

5. **Looping Mechanism:**

   * After each operation, the user is asked whether to perform another.
   * Continues until the user types `n` to exit.


🎯 **Purpose:**

This program is ideal for **students or beginners in Python and statistics** who want to practice data operations and improve command-line interaction. It also introduces good coding habits like modular functions and input validation.
