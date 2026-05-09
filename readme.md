# Student Performance Prediction ML Project

This project predicts the math score of students based on various features like gender, ethnicity, parental education level, lunch, and test preparation course.

## Project Structure

- `src/components`: Contains Data Ingestion, Data Transformation, and Model Trainer components.
- `src/pipeline`: Contains Training and Prediction pipelines.
- `artifacts`: Stores the raw data, processed arrays, preprocessor object, and the best trained model.
- `templates`: HTML templates for the Flask web application.
- `app.py`: Flask application entry point.

## How to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the Model**:
   ```bash
   python src/pipeline/train_pipeline.py
   ```

3. **Run the Web App**:
   ```bash
   python app.py
   ```
   Then open `http://127.0.0.1:5000` in your browser.