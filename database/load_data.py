import pandas as pd
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.vector_db import VectorDB

def load_data_to_pinecone():
    print("📂 Loading dataset...")
    
    # Get the correct path (go up 2 levels from this file)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    csv_path = os.path.join(project_root, 'data', 'intern_data_ikarus_processed.csv')
    
    print(f"Looking for CSV at: {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"✅ Loaded {len(df)} products")
    
    vector_db = VectorDB()
    vector_db.add_products(df)
    
    print("\n🎉 Data loading complete!")

if __name__ == "__main__":
    load_data_to_pinecone()

