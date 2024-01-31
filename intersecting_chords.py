import numpy as np

def intersecting_segments(seg, arr):
    """
    Check if two line segments intersect.

    Args:
    - seg: Tuple representing a line segment with start and end points.
    - arr: Tuple representing another line segment with start and end points.

    Returns:
    - True if the two line segments intersect, False otherwise.
    """
    if (arr[0] < seg[0] < arr[1]) ^ (arr[0] < seg[1] < arr[1]):
        return True
    return False

def count_intersections(chords):
    """
    Perform line sweep algorithm to count intersecting chords.

    Args:
    - chords: List of tuples representing chords with start and end points.

    Returns:
    - The number of intersecting chords.
    """
    events = []

    # Create events by separating start and end points
    for point in chords:
        events.append((point[0], 's', point))
        events.append((point[1], 'e', point))

    # Sort events based on x-coordinates
    events.sort()

    active_chords = []
    intersections = 0

    # Process events using line sweep algorithm
    for event in events:
        val, event_type, segment = event

        if event_type == 's':
            # Check for intersections with active chords
            for active_chord in active_chords:
                if intersecting_segments(segment, active_chord):
                    intersections += 1
            active_chords.append(segment)
        else:
            # Remove the ending segment from active chords
            if segment in active_chords:
                active_chords.remove(segment)

    return intersections

def num_intersections(input_vals):
    """
    Count the number of intersecting chords in a circle.

    Args:
    - input_vals: Tuple containing radians and labels for chords.

    Returns:
    - The number of intersecting chords.
    """
    radians = input_vals[0]
    label   = input_vals[1]
    chord_info = {}

    # Organize chords by label
    for rad, edge in zip(radians, label):
        chord_label = edge[1:]
        if chord_label in chord_info:
            chord_info[chord_label].append(rad % (2 * np.pi))
        else:
            chord_info[chord_label] = [rad % (2 * np.pi)]

    chords_list = list(chord_info.values())
    return int(count_intersections(chords_list))


# Test Case 1
input1 = [(0.9, 1.3, 1.70, 2.92), ('s1', 'e1', 's2', 'e2')]
num_inter_1 = num_intersections(input1)
print('\nTest Case 1:')
print('Input Chords:', input1[0])
print('Chord Labels:', input1[1])
print('Number of intersections:', num_inter_1)

# Test Case 2
input2 = [(0.78, 1.47, 1.77, 3.92), ('s1', 's2', 'e1', 'e2')]
num_inter_2 = num_intersections(input2)
print('\nTest Case 2:')
print('Input Chords:', input2[0])
print('Chord Labels:', input2[1])
print('Number of intersections:', num_inter_2)

# Test Case 3
input3 = [(3.41, 1.74, 2.66, 5.30, 0.02, 0.76, 4.21, 5.18, 0.85, 3.61),
          ('s0', 'e0', 's1', 'e1', 's2', 'e2', 's3', 'e3', 's4', 'e4')]
num_inter_3 = num_intersections(input3)
print('\nTest Case 3:')
print('Input Chords:', input3[0])
print('Chord Labels:', input3[1])
print('Number of intersections:', num_inter_3)
