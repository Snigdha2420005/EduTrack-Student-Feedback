# EduTrack Student Feedback Manager

This project is a Student Feedback Manager developed for EduTrack, an educational tools startup. It allows for the collection, calculation, and summarization of student feedback.

## Features

### Version 1.0.0

* **Feedback Entry:** Collects student feedback using `feedback_entry.py`.
* **Score Calculation:** Computes the average score using `score_calculator.py`.

### Version 1.0.1

* **Feedback Summary:** Summarizes all feedback, including top scores and grade-wise counts, using `feedback_summary.py`.

## Getting Started

### Prerequisites

* Python 3.x
* `pytest` (for testing)

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2.  Navigate to the project directory:

    ```bash
    cd EduTrack-StudentFeedbackManager
    ```

### Usage

#### Version 1.0.0

* **Collecting Feedback:**

    ```python
    from src.feedback_entry import get_feedback

    feedback = get_feedback()
    # Process the feedback
    ```

* **Calculating Average Score:**

    ```python
    from src.score_calculator import calculate_average_score

    average_score = calculate_average_score(feedback)
    print(f"Average Score: {average_score}")
    ```

#### Version 1.0.1

* **Summarizing Feedback:**

    ```python
    from src.feedback_summary import summarize_feedback

    summary = summarize_feedback(feedback)
    print(summary)
    ```

### Testing

To run the unit tests, use `pytest`:

```bash
pytest tests/# EduTrack-Student-Feedback
