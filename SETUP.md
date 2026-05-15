# 🚀 Setup Instructions

## Prerequisites

- **Python 3.8 or higher** (Check with `python --version`)
- **Groq API Key** (Free at https://console.groq.com/keys)
- **Git** (for cloning the repository)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/GRACEDOFGOD/TASK-A_DSN-x-BCT-HACKATHON-3.0.git
cd TASK-A_DSN-x-BCT-HACKATHON-3.0
```

### 2. Create Virtual Environment

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **flask**: Web framework for the application
- **groq**: Groq API client for LLaMA models
- **httpx**: HTTP client (dependency of groq)
- **gunicorn**: Production WSGI server
- **python-dotenv**: Environment variable management

### 4. Configure Environment Variables

**Copy the example file:**

**Linux/Mac:**
```bash
cp .env.example .env
```

**Windows:**
```cmd
copy .env.example .env
```

**Edit `.env` file:**

Open `.env` in your text editor and replace:
```
GROQ_API_KEY=gsk_your_actual_api_key_here_do_not_expose
```

With your actual API key from https://console.groq.com/keys

### 5. Run the Application

**Development Mode:**
```bash
python app.py
```

The app will start at: **http://127.0.0.1:7860**

**Production Mode (using Gunicorn):**
```bash
gunicorn --bind 0.0.0.0:7860 app:app
```

## Verification

### Test the Health Endpoint

```bash
curl http://127.0.0.1:7860/health
```

Expected response:
```json
{"status": "running", "task": "A"}
```

### Access the Web Interface

Open your browser and navigate to:
```
http://127.0.0.1:7860/
```

You should see the "Let Naija Speak" interface with:
- User profile selector
- Product details form
- Cultural persona selector
- Review generation button

## Common Issues

### Issue: `ModuleNotFoundError: No module named 'flask'`

**Solution:** Ensure virtual environment is activated and run:
```bash
pip install -r requirements.txt
```

### Issue: `GROQ_API_KEY environment variable is not set`

**Solution:** 
1. Make sure `.env` file exists in the project directory
2. Verify the API key is correctly set in `.env`
3. Make sure you're running from the project directory

### Issue: Port 7860 already in use

**Solution:** Change the port by editing `app.py` or setting PORT environment variable:

**Linux/Mac:**
```bash
PORT=8000 python app.py
```

**Windows:**
```cmd
set PORT=8000
python app.py
```

### Issue: `json.decoder.JSONDecodeError` errors

**Solution:** This usually means the LLM response format was unexpected. Try:
1. Check your internet connection
2. Verify Groq API key is valid
3. Check application logs for more details

## Next Steps

- **API Documentation**: See [API.md](API.md) for endpoint details
- **Code Structure**: Check [README.md](README.md) for project overview
- **Troubleshooting**: See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed fixes

## Getting Help

If you encounter issues:

1. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Review the logs in the terminal
3. Verify your `.env` file configuration
4. Ensure you have a stable internet connection
5. Check that your Groq API key is valid and not expired

---

**Happy reviewing! 🇳🇬**
