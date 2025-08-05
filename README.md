# 🍗 Wings R Us - Smart Menu Recommendation System  
*AI-powered complementary item suggestions for Quick Service Restaurants*  


## 🚀 Features  
- **Real-time recommendations** during checkout  
- **Hybrid recommendation engine**:  
  - Association Rule Mining (Apriori algorithm)  
  - Collaborative Filtering for repeat customers  
- **39+ menu item pairings** identified  
- **Flask-based web app** for demo purposes  
- **Competition-ready** with Excel output generation  

## 🛠️ Installation  
### Prerequisites:  
- Python 3.8+  
- Git  

### Steps:  
1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/your-username/WingsRUs-Recommendation-System.git  
   cd WingsRUs-Recommendation-System
2. **Set up virtual environment**:
    python -m venv venv  
    source venv/bin/activate  # Linux/Mac  
    venv\Scripts\activate     # Windows
3.**Install dependencies:**
    pip install -r requirements.txt
4.**Running the Application**:
   python main.py
5.**Expected Output**:
   Generates recommendations.xlsx in /output folder
   Sample terminal output:
   Processing order #1001: Classic Wings → Recommended: Fries, Cola, Ranch Dip
6.**Testing**:
   Use included test cases in /data/test_cases.xlsx or:
   from src.recommendation_engine import Recommender  
   recommender = Recommender()  
   print(recommender.recommend(["BBQ Wings"], k=3))
7.**📂 Project Structure**:
   .  
   ├── data/                   # Datasets  
   │   ├── raw_data.csv        # Historical orders  
   │   └── test_cases.xlsx     # Competition input  
   ├── src/                    # Core logic  
   │   ├── data_processing.py  
   │   ├── recommendation_engine.py  
   │   └── evaluation.py  
   ├── notebooks/              # Analysis  
   │   └── EDA.ipynb  
   ├── output/                 # Generated files  
   ├── app.py                  # Flask web app  
   ├── main.py                 # CLI entry point  
   └── requirements.txt        # Dependencies
8.**🤖 AI Implementation**:
   **Technologies:**
   - PyTorch for model training
   - MLxtend for association rules
   - Scikit-learn for collaborative filtering
   **Model Specifications:**
   - Trained on 10,000+ transaction records
   - 82% Recall@3 accuracy
   - Fallback to popular items when no rules match
9.**📊 Competition Submission**:
   **Output Format:**

     Order ID     Customer ID     Current Items     Recommendation 1     Recommendation 2     Recommendation 3
     1001	        501	            Classic Wings	    Fries	               Cola	                Ranch Dip
     Scoring: +1 per correct recommendation in top 3
10.**👥 Contributing**:
     We welcome contributions in:
     - Improving recommendation accuracy
     - Enhancing the web interface
     - Adding new datasets
     Guidelines:
     1. Fork the repository
     2. Create a feature branch (git checkout -b feature/improvement)
     3. Submit a pull request
11.**📜 License**:
     MIT License - Open for academic/commercial use
🔗 Repository: github.com/PriyanshuGupta04/WingsRUs-Recommendation-System
📧 Contact: priyanshugupta4751@gmail.com

   
   
   
