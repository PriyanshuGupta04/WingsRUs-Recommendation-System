from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

class Recommender:
    def __init__(self):
        self.rules = None
        self.popular_items = ['Fries', 'Cola', 'Ranch Dip', 'Onion Rings', 'Garlic Bread']
    
    def train(self, data):
        """Train the recommendation models"""
        try:
            # Create transaction matrix with boolean values
            transaction_matrix = pd.get_dummies(data['items'].explode()).groupby(level=0).max().astype(bool)
            
            # Generate association rules
            frequent_itemsets = apriori(transaction_matrix, min_support=0.01, use_colnames=True)
            self.rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
        except Exception as e:
            print(f"Training error: {e}")
            self.rules = None
    
    def recommend(self, input_items, k=3):
        """Generate recommendations for given items"""
        try:
            if self.rules is not None and not self.rules.empty:
                # Convert input_items to frozenset for comparison
                input_set = frozenset(input_items)
                
                # Find rules where antecedents are subset of input items
                relevant_rules = self.rules[
                    self.rules['antecedents'].apply(lambda x: x.issubset(input_set))
                ]
                
                if not relevant_rules.empty:
                    # Get top recommendations by confidence
                    recommendations = relevant_rules.sort_values('confidence', ascending=False)
                    rec_items = []
                    for itemset in recommendations['consequents']:
                        for item in itemset:
                            if item not in input_items and item not in rec_items:
                                rec_items.append(item)
                                if len(rec_items) >= k:
                                    return rec_items[:k]
        
            # Fallback to popular items if no rules match
            return [item for item in self.popular_items if item not in input_items][:k]
        except Exception as e:
            print(f"Recommendation error: {e}")
            return self.popular_items[:k]