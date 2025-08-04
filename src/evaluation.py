import numpy as np

def evaluate_model(test_data, recommender, k=3):
    """Evaluate model performance using Recall@k"""
    recalls = []
    for _, row in test_data.iterrows():
        true_items = set(row['items'])
        input_item = list(true_items)[0]  # Use first item as input
        recommendations = recommender.recommend([input_item], k)
        hits = len(set(recommendations) & true_items)
        recalls.append(hits / min(k, len(true_items - {input_item})))
    
    return np.mean(recalls)