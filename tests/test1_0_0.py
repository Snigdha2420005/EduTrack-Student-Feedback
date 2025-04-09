# tests/test_version1_0_0.py
    import pytest
    from src.feedback_entry import get_feedback
    from src.score_calculator import calculate_average_score
    
    def test_get_feedback_empty_input(monkeypatch):
        """Test that get_feedback returns an empty list if no input is provided."""
        monkeypatch.setattr('builtins.input', lambda _: 'done')  # Simulate 'done' input
        assert get_feedback() == []
    
    def test_get_feedback_valid_input(monkeypatch):
        """Test that get_feedback collects feedback correctly with valid input."""
        # Simulate user input
        input_values = iter(['S101', '5', 'Good job!', 'done'])
        monkeypatch.setattr('builtins.input', lambda _: next(input_values))
    
        expected_feedback = [{'student_id': 'S101', 'rating': 5, 'comments': 'Good job!'}]
        assert get_feedback() == expected_feedback
    
    def test_calculate_average_score_empty_list():
        """Test that calculate_average_score returns 0 for an empty feedback list."""
        assert calculate_average_score([]) == 0
    
    def test_calculate_average_score_valid_list():
        """Test that calculate_average_score calculates the average correctly."""
        feedback_data = [
            {'student_id': 'S101', 'rating': 4, 'comments': 'Okay'},
            {'student_id': 'S102', 'rating': 5, 'comments': 'Great'},
            {'student_id': 'S103', 'rating': 3, 'comments': 'Fair'}
        ]
        assert calculate_average_score(feedback_data) == 4.0
    
    if __name__ == '__main__':
        pytest.main()
    ```

   * **Explanation:**
        * `pytest` is used for writing the tests.
        * We import the functions to be tested.
        * `test_get_feedback_empty_input`:  Uses `monkeypatch` to simulate user input.  It checks if an empty list is returned when the user immediately enters "done".
        * `test_get_feedback_valid_input`:  Again, uses `monkeypatch` to simulate providing student ID, rating, and comments.  It verifies that the function returns the data in the expected format.
        * `test_calculate_average_score_empty_list`:  Checks that the average is 0 when there's no feedback.
        * `test_calculate_average_score_valid_list`:  Checks if the average is calculated correctly.
   * **Run tests locally:**
        * Open your terminal, navigate to the project directory, and run `pytest tests/` to make sure your tests pass.

**3. GitHub Actions Workflow (`.github/workflows/test.yml`)**

   * **Create the workflow file:**
        * In your local repository, create the file `.github/workflows/test.yml`.
   * **Define the workflow:**
        * Here's the YAML code for the workflow:

```yaml
    name: Test  # Name of the workflow

    on:
      push:  # Trigger the workflow on push events
        branches: [ main ]  # ... to the main branch
      pull_request: # and on pull requests
        branches: [ main ]

    jobs:
      build:
        runs-on: ubuntu-latest  # Use the latest Ubuntu runner

        steps:
        - uses: actions/checkout@v3  # Checkout the code
        - name: Set up Python 3.x
          uses: actions/setup-python@v4
          with:
            python-version: '3.9'  # Or your preferred Python version

        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install pytest  # Install pytest

        - name: Run tests with pytest
          run: |
            pytest tests/  # Execute the tests
