# 🛋️ Furniture Recommendation System

An intelligent AI-powered furniture recommendation system using **Vector Search**, **Natural Language Processing**, and **Generative AI** to help users discover furniture products through conversational queries.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Jupyter Notebooks](#jupyter-notebooks)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 🎯 Overview

This project implements a **semantic search and recommendation system** for furniture products. Users can search for furniture using natural language queries like "modern sofa for living room" and receive AI-powered recommendations with detailed descriptions.

### Key Capabilities:
- **Semantic Search**: Understands user intent, not just keywords
- **Vector Database**: Fast similarity search across 305+ products
- **AI Descriptions**: Generates creative product descriptions using Google Gemini
- **RESTful API**: FastAPI backend for scalable deployment
- **Data Analytics**: Comprehensive insights into furniture catalog

---

## ✨ Features

### 1. **Intelligent Search**
- Semantic understanding of natural language queries
- Vector embeddings using Sentence Transformers
- Pinecone serverless vector database for fast retrieval

### 2. **AI-Generated Content**
- Creative product descriptions using Google Gemini 2.5 Flash
- Contextual and engaging furniture descriptions

### 3. **RESTful API**
- FastAPI backend with automatic documentation
- CORS-enabled for frontend integration
- Multiple endpoints for recommendations, chat, and analytics

### 4. **Data Analytics**
- Exploratory Data Analysis (EDA) on 305 furniture products
- Visualizations for pricing, brands, materials, and colors
- Statistical insights and trends

### 5. **Model Evaluation**
- Recommendation quality metrics (precision, similarity scores)
- Performance benchmarking
- Pinecone integration validation

---

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.9+
- **Vector Database**: Pinecone (Serverless)
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **GenAI**: Google Gemini 2.5 Flash

### Data Science
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **ML Models**: Scikit-learn, Sentence Transformers

### Development Tools
- **Environment Management**: Virtual Environment (venv)
- **API Testing**: Uvicorn, FastAPI Docs
- **Notebooks**: Jupyter

---

## 📁 Project Structure

# 🛋️ Furniture Recommendation System

An intelligent AI-powered furniture recommendation system using **Vector Search**, **Natural Language Processing**, and **Generative AI** to help users discover furniture products through conversational queries.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Jupyter Notebooks](#jupyter-notebooks)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 🎯 Overview

This project implements a **semantic search and recommendation system** for furniture products. Users can search for furniture using natural language queries like "modern sofa for living room" and receive AI-powered recommendations with detailed descriptions.

### Key Capabilities:
- **Semantic Search**: Understands user intent, not just keywords
- **Vector Database**: Fast similarity search across 305+ products
- **AI Descriptions**: Generates creative product descriptions using Google Gemini
- **RESTful API**: FastAPI backend for scalable deployment
- **Data Analytics**: Comprehensive insights into furniture catalog

---

## ✨ Features

### 1. **Intelligent Search**
- Semantic understanding of natural language queries
- Vector embeddings using Sentence Transformers
- Pinecone serverless vector database for fast retrieval

### 2. **AI-Generated Content**
- Creative product descriptions using Google Gemini 2.5 Flash
- Contextual and engaging furniture descriptions

### 3. **RESTful API**
- FastAPI backend with automatic documentation
- CORS-enabled for frontend integration
- Multiple endpoints for recommendations, chat, and analytics

### 4. **Data Analytics**
- Exploratory Data Analysis (EDA) on 305 furniture products
- Visualizations for pricing, brands, materials, and colors
- Statistical insights and trends

### 5. **Model Evaluation**
- Recommendation quality metrics (precision, similarity scores)
- Performance benchmarking
- Pinecone integration validation

---

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.9+
- **Vector Database**: Pinecone (Serverless)
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **GenAI**: Google Gemini 2.5 Flash

### Data Science
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **ML Models**: Scikit-learn, Sentence Transformers

### Development Tools
- **Environment Management**: Virtual Environment (venv)
- **API Testing**: Uvicorn, FastAPI Docs
- **Notebooks**: Jupyter

---

## 📁 Project Structure
ikarus_app/
│
├── backend/
│ ├── models/
│ │ ├── init.py
│ │ ├── recommendation.py # Recommendation engine
│ │ └── genai.py # Gemini AI integration
│ │
│ ├── database/
│ │ ├── init.py
│ │ ├── vector_db.py # Pinecone connection
│ │ └── load_data.py # Data loading script
│ │
│ ├── routes/
│ │ └── init.py
│ │
│ ├── utils/
│ │ └── init.py
│ │
│ ├── .env # API keys (gitignored)
│ ├── main.py # FastAPI application
│ └── requirements.txt # Python dependencies
│
├── data/
│ └── intern_data_ikarus_processed.csv # Cleaned dataset
│
├── notebooks/
│ ├── data_analytics.ipynb # EDA notebook
│ └── model_training.ipynb # Model training notebook
│
├── frontend/ # (To be implemented)
│
├── .gitignore
└── README.md


---

## 🚀 Installation

### Prerequisites
- Python 3.9 or higher
- Pinecone account (free tier)
- Google Gemini API key (free tier)

### Step 1: Clone Repository
git clone <repository-url>
cd ikarus_app


### Step 2: Create Virtual Environment
python -m venv venv

Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

### Step 3: Install Dependencies
pip install -r backend/requirements.txt

### Step 4: Setup Environment Variables
Create `backend/.env` file:
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=serverless
GEMINI_API_KEY=your_gemini_api_key_here

### Step 5: Load Data to Pinecone
cd backend
python database/load_data.py

### Step 6: Run Backend Server
python main.py

Server will start at: `http://localhost:8000`

---

## 📖 Usage

### API Endpoints

#### 1. **Health Check**
GET http://localhost:8000/

#### 2. **Get Recommendations**
GET http://localhost:8000/api/recommend?query=modern%20sofa&top_k=5


**Response:**
{
"query": "modern sofa",
"products": [
{
"id": "uuid",
"title": "Product Name",
"brand": "Brand Name",
"price": 149.99,
"similarity_score": 0.85,
"ai_description": "AI-generated description"
}
]
}

#### 3. **Chat Interface**
POST http://localhost:8000/api/chat

**Body:**
{
"message": "I need a comfortable office chair",
"history": []
}

#### 4. **Analytics**
GET http://localhost:8000/api/analytics

**Response:**
{
"total_products": 305,
"avg_price": 68.29,
"top_brands": {...}
}

---

## 📊 API Documentation

FastAPI provides automatic interactive documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📓 Jupyter Notebooks

### 1. Data Analytics (`notebooks/data_analytics.ipynb`)

**Key Insights:**
- 305 furniture products analyzed
- 264 unique brands
- Average price: $68.29
- Most common material: Wood (31 products)
- Most popular color: Black (44 products)

**Visualizations:**
- Price distribution
- Brand analysis
- Material breakdown
- Color trends
- Missing values analysis

### 2. Model Training (`notebooks/model_training.ipynb`)

**Model Details:**
- **Embedding Model**: all-MiniLM-L6-v2
- **Embedding Dimension**: 384
- **Vector Database**: Pinecone Serverless (AWS us-east-1)

**Performance Metrics:**
- Average Precision: 85%+
- Average Similarity Score: 0.75+
- Query Response Time: < 100ms

**Evaluation:**
- Cosine similarity-based recommendations
- Precision metrics for different queries
- Pinecone integration validation

---

## 📸 Screenshots

### 1. API Response Example
{
"query": "modern sofa",
"products": [
{
"title": "FANYE Oversized 6 Seaters Modular Sofa",
"brand": "FANYE",
"similarity_score": 0.5985,
"ai_description": "Transform your living space with this..."
}
]
}

### 2. Data Analytics Insights
- Brand distribution chart
- Price histogram
- Material breakdown
- Color popularity

### 3. Model Performance
- Similarity distribution plots
- Precision metrics
- Recommendation examples

---

## 🔮 Future Enhancements

### Phase 1 (Current)
- ✅ Backend API with FastAPI
- ✅ Vector search with Pinecone
- ✅ AI-generated descriptions
- ✅ Jupyter notebooks for analysis

### Phase 2 (Planned)
- 🔄 React frontend with chat interface
- 🔄 User authentication
- 🔄 Personalized recommendations
- 🔄 Product filtering and sorting

### Phase 3 (Future)
- 📋 Computer vision for image-based search
- 📋 Multi-language support
- 📋 Price tracking and alerts
- 📋 Integration with e-commerce platforms

---

## 🧪 Testing

### Run API Tests
Test recommendation endpoint
curl http://localhost:8000/api/recommend?query=sofa&top_k=3

Test analytics endpoint
curl http://localhost:8000/api/analytics

### Test in Browser
- Open: http://localhost:8000/docs
- Try the interactive API documentation

---

## 📦 Dependencies

### Core Libraries
fastapi==0.104.1
uvicorn==0.24.0
pinecone==7.3.0
sentence-transformers==2.3.1
google-generativeai
pandas==2.1.3
numpy==1.26.2
scikit-learn==1.3.2

### Data Science
matplotlib
seaborn
jupyter
notebook

See `backend/requirements.txt` for complete list.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Priya** - AI/ML Intern Assignment for Ikarus

---

## 🙏 Acknowledgments

- **Pinecone** for vector database
- **Google Gemini** for generative AI
- **Sentence Transformers** for embeddings
- **FastAPI** for web framework
- **Ikarus** for the internship opportunity

---

## 📞 Contact

For questions or support:
- Email: your.email@example.com
- GitHub: @yourusername

---

## 🎓 Assignment Details

**Project**: Furniture Recommendation System  
**Organization**: Ikarus  
**Duration**: October 2025  
**Technologies**: Python, FastAPI, Pinecone, GenAI, Vector Search  

---

## ⚡ Quick Start Commands

Setup
python -m venv venv
venv\Scripts\activate
pip install -r backend/requirements.txt

Configure
Edit backend/.env with your API keys
Load data
cd backend
python database/load_data.py

Run server
python main.py

Access API
http://localhost:8000

---

**Made with ❤️ using AI and Vector Search**
