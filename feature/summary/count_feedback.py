# count_feedback.py
def count_total_feedback_entries(feedback_data):
    """
    Counts the total number of feedback entries.

    Args:
        feedback_data (dict): Dictionary of feedback.

    Returns:
        int: The total number of feedback entries.
    """
    return len(feedback_data)

if __name__ == '__main__':
    sample_data = {
        "Alice": {"score": 90, "grade": "A"},
        "Bob": {"score": 85, "grade": "B"},
        "Charlie": {"score": 92, "grade": "A"},
    }
    print(count_total_feedback_entries(sample_data))  # Output: 3
    print(count_total_feedback_entries({}))             # Output: 0
