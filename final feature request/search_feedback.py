# search_feedback.py
import csv
import sys

def search_feedback_by_name(filename, student_name):
    """Searches for feedback entries by student name in a CSV file."""
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            found_feedback = []
            for row in reader:
                if 'student_name' in row and row['student_name'].lower() == student_name.lower():
                    found_feedback.append(row)
            return found_feedback
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python search_feedback.py <student_name>")
        sys.exit(1)

    student_to_search = sys.argv[1]
    feedback_file = 'feedback_data.csv'  # Replace with your actual filename
    results = search_feedback_by_name(feedback_file, student_to_search)

    if results:
        print(f"Feedback for '{student_to_search}':")
        for entry in results:
            print(entry)  # You might want to format this output better
    else:
        print(f"No feedback found for '{student_to_search}'.")
