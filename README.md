# Intersecting Chords Algorithm

This Python program calculates the number of intersecting chords in a circle using a line sweep algorithm.

## Algorithm Explanation

The algorithm utilized here, known as the line sweep technique, efficiently counts intersections among chords in a circle. Imagine a vertical line sweeping from left to right across the circle. As it encounters each chord's start and end points, it checks for intersections with active chords already encountered. If an intersection is found, it increments the intersection count. The algorithm maintains a set of active chords, updating it as it progresses through the chords. By organizing chords based on their labels and using the start and end points of each chord, the algorithm accurately determines the number of intersections.

## Time Complexity estimate:
The algorithm exhibits a time complexity of **O(n log n)**, where n is the total number of chord endpoints, due to the sorting step in the line sweep process.

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
   - Modify the `inputX` variables in the `intersecting_chords.py` file to test the algorithm with different chord configurations.
   - Each input is a tuple containing radians and labels for chords.

4. **Output:**
   - The program will display the number of intersecting chords based on the provided input.

### Example:

```python
# Example input
input_vals = [
    (np.pi / 4, np.pi / 3, np.pi / 2, 5 * np.pi / 6),
    ('s1', 'e1', 's2', 'e2')
]

# Run the algorithm
num_intersections_result = num_intersections(input_vals)
print('Number of intersections:', num_intersections_result)
