# count_feedback.py
import csv

def count_total_feedback(filename):
    """Counts the total number of entries in a CSV feedback file."""
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            # If your file has a header row, you might want to skip it
            header = next(reader, None)
            count = 0
            for row in reader:
                count += 1
            return count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    feedback_file = 'feedback_data.csv'  # Replace with your actual filename
    total_count = count_total_feedback(feedback_file)

    if total_count is not None:
        print(f"Total feedback entries: {total_count}")
