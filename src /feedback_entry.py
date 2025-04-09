# feedback_entry.py

def get_feedback():
    """
    Collects student feedback on a course or instructor.
    Returns a list of dictionaries, where each dictionary represents one student's feedback.
    """

    feedback_list = []
    while True:
        student_id = input("Enter student ID (or 'done' to finish): ")
        if student_id.lower() == 'done':
            break

        try:
            rating = int(input("Enter rating (1-5): "))
            if 1 <= rating <= 5:
                comments = input("Enter comments (optional): ")
                feedback = {
                    "student_id": student_id,
                    "rating": rating,
                    "comments": comments
                }
                feedback_list.append(feedback)
            else:
                print("Invalid rating. Please enter a rating between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number for the rating.")

    return feedback_list

if __name__ == "__main__":
    student_feedback = get_feedback()
    print("\n--- Student Feedback ---")
    for fb in student_feedback:
        print(f"Student ID: {fb['student_id']}, Rating: {fb['rating']}, Comments: {fb['comments']}")
