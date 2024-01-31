# Intersecting Chords Algorithm

This Python program calculates the number of intersecting chords in a circle using a line sweep algorithm.

## Algorithm Explanation

The algorithm employs a line sweep technique to process chords and count intersections. It organizes chords based on their labels and checks for intersections using the start and end points of each chord. The line sweep maintains a set of active chords and updates it as chords are processed.

## How to Run

1. **Requirements:**
   - Python 3.10.12
   - NumPy library (`pip install numpy` if not already installed)

2. **Run the Program:**
   - Open a terminal or command prompt.
   - Execute the following command:
     ```bash
     python intersecting_chords.py
     ```

3. **Input:**
   - Modify the `input_vals` variable in the `intersecting_chords.py` file to test the algorithm with different chord configurations.
   - Each input is a tuple containing radians and labels for chords.

4. **Output:**
   - The program will display the number of intersecting chords based on the provided input.

