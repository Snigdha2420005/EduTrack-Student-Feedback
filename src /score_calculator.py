# score_calculator.py

def calculate_average_score(feedback_list):
    """
    Calculates the average rating from a list of student feedback.

    Args:
        feedback_list: A list of dictionaries, where each dictionary
                       represents one student's feedback and contains a 'rating' key.

    Returns:
        The average rating as a float.
        Returns 0 if the feedback list is empty.
    """

    if not feedback_list:
        return 0  # Return 0 if the list is empty to avoid division by zero

    total_rating = sum(fb['rating'] for fb in feedback_list)
    average_rating = total_rating / len(feedback_list)
    return average_rating

if __name__ == "__main__":
    # Example Usage (you would typically get feedback_data from feedback_entry.py)
    feedback_data = [
        {"student_id": "S101", "rating": 4, "comments": "Good course"},
        {"student_id": "S102", "rating": 5, "comments": "Excellent instructor"},
        {"student_id": "S103", "rating": 3, "comments": "Could be better"},
        {"student_id": "S104", "rating": 4, "comments": "Helpful materials"},
    ]

    average = calculate_average_score(feedback_data)
    print(f"Average Rating: {average}")
