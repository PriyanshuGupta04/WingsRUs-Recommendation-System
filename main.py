import pandas as pd
from src.data_processing import load_and_clean_data
from src.recommendation_engine import Recommender
from src.evaluation import evaluate_model

def generate_output_sheet(test_cases, recommender, output_path):
    """
    Generate Excel output with recommendations for given test cases
    
    Args:
        test_cases: List of dictionaries containing order details
        recommender: Trained recommender instance
        output_path: Path to save the Excel file
    """
    recommendations = []
    for case in test_cases:
        try:
            rec_items = recommender.recommend(case['items'], k=3)
            # Pad recommendations if less than 3 items returned
            rec_items += [''] * (3 - len(rec_items))
            
            recommendations.append({
                'order_id': case['order_id'],
                'customer_id': case['customer_id'],
                'input_items': ', '.join(case['items']),
                'recommendation_1': rec_items[0],
                'recommendation_2': rec_items[1],
                'recommendation_3': rec_items[2]
            })
        except Exception as e:
            print(f"Error processing order {case['order_id']}: {e}")
    
    return pd.DataFrame(recommendations)

def main():
    # Step 1: Load and clean data
    print("Loading and cleaning data...")
    try:
        data = load_and_clean_data("data/raw_data.csv")
        data.to_csv("data/cleaned_data.csv", index=False)
        print("Data successfully loaded and cleaned.")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Step 2: Initialize and train recommender
    print("\nTraining recommendation models...")
    recommender = Recommender()
    recommender.train(data)
    print("Model training completed.")

    # Step 3: Test cases
    test_cases = [
        {'order_id': 1001, 'customer_id': 501, 'items': ['Classic Wings']},
        {'order_id': 1002, 'customer_id': 502, 'items': ['BBQ Wings', 'Fries']},
        {'order_id': 1003, 'customer_id': 503, 'items': ['Spicy Wings', 'Cola']},
        {'order_id': 1004, 'customer_id': 504, 'items': ['Honey Mustard Wings']},
        {'order_id': 1005, 'customer_id': 505, 'items': ['Garlic Parmesan Wings', 'Beer']}
    ]

    # Step 4: Generate recommendations
    print("\nGenerating recommendations...")
    recommendations_df = generate_output_sheet(
        test_cases=test_cases,
        recommender=recommender,
        output_path="output/recommendations.xlsx"
    )

    # Display sample recommendations
    print("\n=== Sample Recommendations ===")
    print(recommendations_df.head())
    print("\n" + "="*40)

    # Step 5: Save to Excel
    try:
        output_path = "output/recommendations.xlsx"
        recommendations_df.to_excel(output_path, index=False)
        print(f"\nRecommendations successfully saved to {output_path}")
    except Exception as e:
        print(f"\nError saving recommendations: {e}")

    # Step 6: Evaluation
    print("\nRunning evaluation...")
    try:
        test_data = pd.read_csv("data/test_data.csv")
        test_data['items'] = test_data['items'].apply(lambda x: x.split(', '))
        recall = evaluate_model(test_data, recommender)
        print(f"Model Recall@3 Score: {recall:.2f}")
    except FileNotFoundError:
        print("Test data not found - skipping evaluation")
    except Exception as e:
        print(f"Evaluation error: {e}")

    print("\nProcess completed successfully!")

if __name__ == "__main__":
    main()