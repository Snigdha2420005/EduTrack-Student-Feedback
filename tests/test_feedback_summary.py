import pytest
    from feedback_summary import summarize_feedback  # Assuming feedback_summary.py exists
    
    def test_summarize_feedback_empty():
        feedback_data = {}
        summary = summarize_feedback(feedback_data)
        assert summary == {"top_scores": [], "grade_counts": {}}
    
    def test_summarize_feedback_basic():
        feedback_data = {
            "Alice": {"score": 90, "grade": "A"},
            "Bob": {"score": 85, "grade": "B"},
            "Charlie": {"score": 92, "grade": "A"},
            "David": {"score": 78, "grade": "C"},
        }
        summary = summarize_feedback(feedback_data)
        assert summary == {
            "top_scores": ["Charlie (92)", "Alice (90)", "Bob (85)"],
            "grade_counts": {"A": 2, "B": 1, "C": 1},
        }
    
    def test_summarize_feedback_ties():
        feedback_data = {
            "Alice": {"score": 90, "grade": "A"},
            "Bob": {"score": 90, "grade": "B"},
            "Charlie": {"score": 92, "grade": "A"},
        }
        summary = summarize_feedback(feedback_data)
        assert summary == {
            "top_scores": ["Charlie (92)", "Alice (90)", "Bob (90)"],
            "grade_counts": {"A": 2, "B": 1},
        }
    
    def test_summarize_feedback_different_grades():
        feedback_data = {
            "Alice": {"score": 88, "grade": "Excellent"},
            "Bob": {"score": 76, "grade": "Good"},
            "Charlie": {"score": 92, "grade": "Excellent"},
            "David": {"score": 65, "grade": "Fair"},
            "Emily": {"score": 80, "grade": "Good"},
        }
        summary = summarize_feedback(feedback_data)
        assert summary == {
            "top_scores": ["Charlie (92)", "Alice (88)", "Emily (80)"],
            "grade_counts": {"Excellent": 2, "Good": 2, "Fair": 1},
        }
