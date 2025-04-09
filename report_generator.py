# report_generator.py
def export_feedback_to_txt(feedback_data, filename="feedback_report.txt"):
    """
    Exports feedback data to a text file.

    Args:
        feedback_data (dict): Dictionary of feedback.
        filename (str, optional): Name of the output file. Defaults to "feedback_report.txt".
    """
    try:
        with open(filename, "w") as f:
            f.write("--- Feedback Report ---\n\n")
            for name, data in feedback_data.items():
                f.write(f"Student: {name}\n")
                f.write(f"Score: {data['score']}\n")
                f.write(f"Grade: {data['grade']}\n")
                if 'comment' in data:
                    f.write(f"Comment: {data['comment']}\n")
                f.write("\n")
        print(f"Feedback exported to {filename}")
    except Exception as e:
        print(f"Error exporting feedback: {e}")

if __name__ == '__main__':
    sample_data = {
        "Alice": {"score": 90, "grade": "A", "comment": "Good job!"},
        "Bob": {"score": 85, "grade": "B"},
        "Charlie": {"score": 92, "grade": "A", "comment": "Excellent!"},
    }
    export_feedback_to_txt(sample_data, "test_report.txt")
