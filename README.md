# 📄 Resume Sorter - AI-Powered Resume Filtering Tool

An intelligent resume filtering and analysis application built with Streamlit and Google Gemini AI. Upload multiple resumes and filter them using natural language queries to find the perfect candidates.

## 🌐 Live Demo

**🔗 [Try the Live Application](https://resume-sorter-6hgh.onrender.com/)**

> ⚠️ Note: On Render's free tier, the app may take 15-30 seconds to wake up if it's been inactive. Please be patient!

## ✨ Features

- **📤 Multiple Resume Upload**: Upload resumes in PDF, DOC, DOCX, or TXT formats
- **🤖 AI-Powered Processing**: Uses Google Gemini AI to extract and analyze resume data
- **🔍 Natural Language Filtering**: Filter resumes using simple queries like "React developers with 3+ years experience"
- **📊 Comprehensive Data Extraction**: Extracts:
  - Personal information (name, email, phone, location)
  - Work experience and years of experience
  - Education details
  - Technical skills
  - Languages and certifications
  - LinkedIn and GitHub profiles
- **📈 Match Scoring**: Get AI-generated match scores for each candidate
- **📥 Excel Export**: Export filtered results to Excel for further analysis
- **🎨 Modern UI**: Clean, intuitive interface with light theme

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API Key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/radhakrishna1210/resume_sorter.git
   cd resume_sorter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**

   Create a `.streamlit/secrets.toml` file (if it doesn't exist) and add your Gemini API key:
   ```toml
   [gemini]
   api_key = "your_gemini_api_key_here"
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

## 📖 Usage

### Upload Resumes

1. **Upload Files**: Click the upload area and select one or more resume files (PDF, DOC, DOCX, TXT)
2. **Or Load Samples**: Click "⬆ Load Sample Resumes" to use sample resumes included in the project

### Filter Resumes

1. **Enter Filter Query**: Type a natural language query in the filter box, for example:
   - "React developers with 3+ years experience"
   - "Python developers with machine learning skills"
   - "Software engineers with 5+ years and Java experience"

2. **Click Filter**: Click the "⌕ Filter Resumes" button to process and filter the resumes

3. **View Results**: The filtered results will be displayed in a table with:
   - Applicant details
   - Match scores
   - Extracted information

### Export Results

Click the "Export to Excel" button to download the filtered results as an Excel file.

## 🌐 Deployment on Render

This project is configured for easy deployment on Render (free tier available).

### Deployment Steps

1. **Push to GitHub**
   - Ensure your code is pushed to a GitHub repository

2. **Create Render Account**
   - Go to [Render.com](https://render.com)
   - Sign up using your GitHub account

3. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `radhakrishna1210/resume_sorter`
   - Select the repository

4. **Configure Service** (or use `render.yaml` if auto-detected)
   - **Name**: `resume-sorter` (or any name you prefer)
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Root Directory**: (leave empty)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

5. **Add Environment Variable**
   - In "Environment Variables" section
   - Add:
     - **Key**: `GEMINI_API_KEY`
     - **Value**: Your actual Gemini API key

6. **Select Plan**
   - Choose **Free** plan
   - Click "Create Web Service"

7. **Wait for Deployment**
   - First deployment takes 5-10 minutes
   - Monitor logs for any errors
   - You'll get a URL like: `https://resume-sorter-6hgh.onrender.com/`

### Adding Hosted Link to GitHub Repository

After deployment, add the hosted link to your GitHub repository:

1. **In README.md** ✅ (Already done above)
   - The live demo link is displayed at the top of this README

2. **In Repository Settings (Recommended)**
   - Go to your GitHub repository: `https://github.com/radhakrishna1210/resume_sorter`
   - Click the **⚙️ Settings** tab
   - Scroll down to **"About"** section (in the left sidebar)
   - Enter your Render URL in the **"Website"** field:
     ```
     https://resume-sorter-6hgh.onrender.com/
     ```
   - Click **Save changes**
   - The link will now appear at the top-right of your repository page

3. **In Repository Description**
   - Go to your repository main page
   - Click the **✏️ Edit** icon next to the description
   - Add: `🌐 Live Demo: https://resume-sorter-6hgh.onrender.com/`

### Render Free Tier Notes

- ✅ Spins down after 15 minutes of inactivity
- ✅ First request after spin-down takes 15-30 seconds (cold start)
- ✅ 750 hours/month free tier
- ✅ Perfect for small to medium projects

## 📁 Project Structure

```
resume_sorter/
├── app.py                 # Main Streamlit application
├── components/            # Application components
│   ├── filter.py         # Natural language filtering
│   ├── initialization.py # App state initialization
│   ├── processor.py      # Resume processing logic
│   └── results.py        # Results display
├── utils/                 # Utility modules
│   ├── export.py         # Excel export functionality
│   ├── file_handler.py   # File upload and text extraction
│   ├── gemini_processor.py # Gemini AI integration
│   └── secrets_manager.py # API key management
├── data/                  # Data directories
│   ├── samples/          # Sample resume files
│   └── uploads/          # User uploaded files (ephemeral)
├── .streamlit/            # Streamlit configuration
│   ├── config.toml       # Streamlit settings
│   └── secrets.toml      # API keys (not in git)
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment config
├── render.yaml           # Render service configuration
└── README.md             # This file
```

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **Google Gemini AI**: Natural language processing and resume analysis
- **Pandas**: Data manipulation and analysis
- **PyPDF2 / pdfplumber / PyMuPDF**: PDF text extraction
- **python-docx**: DOCX file handling
- **openpyxl / xlsxwriter**: Excel export functionality
- **scikit-learn**: Machine learning utilities

## 🔐 Security Notes

- **API Keys**: Never commit API keys to version control
- **Secrets File**: `.streamlit/secrets.toml` is excluded from Git
- **Environment Variables**: Use environment variables for production deployments
- **File Uploads**: Uploaded files are stored temporarily and processed immediately

## 📝 License

This project is open source and available for personal and commercial use.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Support

For issues or questions, please open an issue on the GitHub repository.

---

**Made with ❤️ using Streamlit and Google Gemini AI**

