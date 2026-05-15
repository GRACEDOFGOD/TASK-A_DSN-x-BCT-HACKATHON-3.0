# 🔧 Troubleshooting Guide

Common issues and their solutions.

## Setup Issues

### 1. Python not found or wrong version

**Error:**
```
'python' is not recognized as an internal or external command
```

**Solution:**
- Install Python from https://www.python.org/ (3.8 or higher)
- On Windows, check "Add Python to PATH" during installation
- Verify: `python --version`

---

### 2. Virtual environment won't activate

**Error:**
```
cannot be loaded because running scripts is disabled on this system
```

**Windows Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

---

### 3. pip install fails

**Error:**
```
ERROR: Could not find a version that satisfies the requirement
```

**Solution:**
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

---

## Configuration Issues

### 4. GROQ_API_KEY not found

**Error:**
```
ValueError: GROQ_API_KEY environment variable is not set
```

**Solution:**

1. **Verify .env exists:**
   ```bash
   ls -la .env  # Linux/Mac
   dir .env     # Windows
   ```

2. **If not, create it:**
   ```bash
   cp .env.example .env
   ```

3. **Edit .env with your API key:**
   - Open `.env` in a text editor
   - Replace `gsk_your_actual_api_key_here_do_not_expose` with your actual key
   - Save the file

4. **Get API key:**
   - Visit https://console.groq.com/keys
   - Create a new API key if needed
   - Copy and paste into `.env`

5. **Restart the app:**
   ```bash
   python app.py
   ```

---

### 5. API key accidentally committed to GitHub

**Immediate action required:**

1. **Revoke the key immediately:**
   - Go to https://console.groq.com/keys
   - Delete the compromised key

2. **Generate new key:**
   - Create a new API key at Groq console
   - Update `.env` with new key

3. **Clean git history (if needed):**
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch .env" \
     --prune-empty --tag-name-filter cat -- --all
   ```

4. **Force push to remove from GitHub:**
   ```bash
   git push origin master --force
   ```

---

## Runtime Issues

### 6. Port 7860 already in use

**Error:**
```
Address already in use
OSError: [Errno 48] Address already in use
```

**Solution:**

**Option A: Use different port**
```bash
PORT=8000 python app.py
```

**Option B: Kill process using port**

**Linux/Mac:**
```bash
lsof -i :7860
kill -9 <PID>
```

**Windows:**
```powershell
Get-Process -Id (Get-NetTCPConnection -LocalPort 7860).OwningProcess | Stop-Process
```

---

### 7. ModuleNotFoundError: No module named 'flask'

**Error:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**

1. **Verify virtual environment is activated:**
   ```bash
   which python  # Should show path in venv/
   ```

2. **Reinstall dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Try without virtual environment (not recommended):**
   ```bash
   python -m pip install flask groq httpx python-dotenv
   ```

---

### 8. Connection refused to localhost:7860

**Error:**
```
Connection refused
Failed to connect to 127.0.0.1:7860
```

**Solution:**

1. **Check if app is running:**
   - Look for Flask output in terminal

2. **Restart the app:**
   ```bash
   python app.py
   ```

3. **Check logs for errors:**
   - Look for error messages in terminal
   - Verify Groq API key is valid

4. **Test health endpoint:**
   ```bash
   curl http://127.0.0.1:7860/health
   ```

---

## API Issues

### 9. JSON decode error / Unexpected LLM response

**Error:**
```
json.decoder.JSONDecodeError: Expecting value
Failed to parse LLM response
```

**Possible Causes:**
- Groq API is down or slow
- Network connectivity issue
- API rate limiting
- Invalid API key

**Solution:**

1. **Verify API key:**
   - Check `.env` file has correct key format
   - Key should start with `gsk_`

2. **Check internet connection:**
   ```bash
   ping console.groq.com
   ```

3. **Try a simple test:**
   ```bash
   python -c "from groq import Groq; print('Groq client imported successfully')"
   ```

4. **Check Groq API status:**
   - Visit https://status.groq.com/

5. **Retry the request:**
   - Sometimes transient errors resolve on retry

---

### 10. Timeout error - Request takes too long

**Error:**
```
TimeoutError
ReadTimeout
```

**Solution:**

1. **Check internet speed:**
   - App requires stable connection to Groq API

2. **Reduce request complexity:**
   - Use shorter product descriptions
   - Reduce number of review history items

3. **Increase timeout (for advanced users):**
   - Edit `agent.py` and increase `timeout` parameter in `client.chat.completions.create()`

---

### 11. "Product name is required" error

**Error:**
```
{"success": false, "error": "Product name is required"}
```

**Solution:**

1. **Check request body:**
   ```json
   {
     "product_name": "Actual Product Name",  // ← Must not be empty
     "user_id": "chukwuemeka"
   }
   ```

2. **Ensure product_name is not whitespace:**
   - Empty string: `""`
   - Only spaces: `"   "`
   - Both are rejected

---

### 12. Custom user validation fails

**Error:**
```
{"success": false, "error": "Custom fields required"}
```

**Solution:**

When `user_id = "custom"`, these fields are REQUIRED:
```json
{
  "user_id": "custom",
  "custom_name": "Your Name",
  "custom_age": 25,
  "custom_city": "Lagos",
  "custom_occupation": "Professional",
  "custom_price_sensitivity": "medium"
}
```

Make sure ALL custom fields are provided.

---

## Browser Issues

### 13. Page won't load / 404 errors

**Error:**
```
This page isn't available
ERR_CONNECTION_REFUSED
```

**Solution:**

1. **Verify app is running:**
   - Check terminal for Flask startup message
   - Should see: `Running on http://127.0.0.1:7860`

2. **Check correct URL:**
   - Correct: `http://127.0.0.1:7860/`
   - Not: `http://localhost:7860/` (sometimes fails)
   - Not: `https://` (not HTTPS)

3. **Clear browser cache:**
   - Hard refresh: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)
   - Or clear browser cache manually

4. **Try different browser:**
   - Use Chrome, Firefox, or Safari
   - Avoid very old browser versions

---

### 14. Styling looks broken

**Issue:**
- CSS not loading
- Page looks plain/ugly

**Solution:**

1. **Hard refresh browser:**
   - Ctrl+Shift+R (Windows/Linux)
   - Cmd+Shift+R (Mac)

2. **Check browser console for errors:**
   - F12 → Console tab
   - Look for 404 errors

3. **Restart app:**
   ```bash
   python app.py
   ```

---

## Performance Issues

### 15. Review generation is very slow

**Cause:**
- Network latency
- Groq API processing time

**Expected time:**
- Usually 2-10 seconds per review
- First request may be slower

**Solution:**

1. **Check internet connection:**
   ```bash
   ping 8.8.8.8
   ```

2. **Try simpler request:**
   - Use fewer characters in product details
   - Try preset user (faster than custom)

3. **Check Groq API status:**
   - May be experiencing load

---

## Getting Help

### Still stuck?

1. **Check all documentation:**
   - [README.md](README.md) - Project overview
   - [SETUP.md](SETUP.md) - Installation
   - [API.md](API.md) - API endpoints

2. **Review logs:**
   - Look at terminal output for error messages
   - Enable debug mode: `FLASK_DEBUG=True`

3. **Verify setup:**
   - Run: `pip install -r requirements.txt`
   - Verify `.env` file exists and has valid API key
   - Check Python version: `python --version`

4. **Test individual components:**
   ```bash
   # Test imports
   python -c "from agent import run_pipeline; print('OK')"
   
   # Test Groq API
   python -c "from groq import Groq; print('OK')"
   
   # Test Flask
   python -c "from flask import Flask; print('OK')"
   ```

---

## Common Quick Fixes

| Issue | Quick Fix |
|-------|-----------|
| App won't start | Check `.env` file and Groq API key |
| Module not found | Activate venv: `source venv/bin/activate` |
| Port in use | `PORT=8000 python app.py` |
| JSON decode error | Check internet connection and API key |
| Styling broken | Hard refresh: Ctrl+Shift+R |

---

**Still need help?** Refer to [SETUP.md](SETUP.md) or check the logs for specific error messages.
