# Wings R Us Recommendation System

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run Jupyter notebook: `jupyter notebook Wings_Recommendation_System.ipynb`
3. Execute cells sequentially

## Evaluation Metric
- Score +1 if actual missing item appears in top 3 recommendations
- Maximum possible score: Number of test cases

## Data Format
- Input: CSV with columns [order_id, customer_id, items]
- Items should be comma-separated: "Classic Wings, Fries, Cola"