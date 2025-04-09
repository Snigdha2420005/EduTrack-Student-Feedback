# search_feedback.py
def search_feedback_by_name(feedback_data, student_name):
    """
    Searches feedback data for a specific student's feedback.

    Args:
        feedback_data (dict): Dictionary of feedback.
        student_name (str): The name of the student to search for.

    Returns:
        dict or None: The feedback data for the student, or None if not found.
    """
    return feedback_data.get(student_name)

if __name__ == '__main__':
    sample_data = {
        "Alice": {"score": 90, "grade": "A", "comment": "Good"},
        "Bob": {"score": 85, "grade": "B"},
    }
    print(search_feedback_by_name(sample_data, "Alice"))  # Output: {'score': 90, 'grade': 'A', 'comment': 'Good'}
    print(search_feedback_by_name(sample_data, "Charlie")) # Output: None
