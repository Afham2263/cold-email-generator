# 📧 Cold Email Generator

This application automates generating customized cold emails for job applications. It scrapes job postings, identifies required skills, and generates personalized emails based on your portfolio.

##  Live Demo

Check out the live app on **Streamlit Cloud**:

 [Launch Cold Email Generator](https://cold-email-generator-ai-proj.streamlit.app/)


## Features
- Job posting extraction from a URL.
- Portfolio integration for relevant skills and project links.
- AI-generated personalized cold emails.
- Skill-based project querying from your portfolio.

## Getting Started

### Prerequisites
- Python 3.x
- Streamlit
- ChromaDB
- Pandas
- LangChain

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Afham2263/cold-email-generator.git
   cd cold-email-generator
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run main.py
   ```

4. Open the app at `http://localhost:8501/`.

### Project Structure
```bash
cold-email-generator/
├── app/resource/my_portfolio.csv   # Portfolio data
├── chains.py                       # LLM chains for job extraction and email generation
├── main.py                         # Entry point for the Streamlit app
├── portfolio.py                    # Portfolio class for querying data
├── utils.py                        # Utility functions (e.g., text cleaning)
└── README.md                       # Project documentation
```

### Usage
1. Enter a job posting URL in the app.
2. The app scrapes and extracts job information and skills.
3. It queries your portfolio for relevant projects.
4. A cold email is generated, including project links from your portfolio.

### Example Email
```
Subject: Application for [Job Title] Position

Dear [Hiring Manager's Name],

I came across the [Job Title] opening at [Company Name] and noticed that my skills in [skill 1], [skill 2] match your needs. Below are some of my projects that demonstrate my expertise:
- [Project 1 Link]
- [Project 2 Link]

Looking forward to discussing how I can contribute.

Best regards,
[Your Name]
```

## Technologies Used
- Streamlit
- ChromaDB
- LangChain
- Pandas

## License
This project is licensed under the MIT License.

