# ============================================================
# config.py
# Configuration constants for Nigerian AI Review Generator
# ============================================================

import os

# ============================================================
# LLM Configuration
# ============================================================
GROQ_MODEL = "llama-3.3-70b-versatile"

# Prediction model parameters
PREDICTION_MAX_TOKENS = 250
PREDICTION_TEMPERATURE = 0.2

# Generation model parameters
GENERATION_MAX_TOKENS = 400
GENERATION_TEMPERATURE = 0.88

# ============================================================
# Flask Configuration
# ============================================================
FLASK_PORT = int(os.environ.get("PORT", 7860))
FLASK_HOST = os.environ.get("HOST", "0.0.0.0")
FLASK_ENV = os.environ.get("FLASK_ENV", "development")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG", "False") == "True"

# ============================================================
# Application Settings
# ============================================================
APP_NAME = "Nigerian AI Review Generator"
APP_VERSION = "1.0.0"
APP_TASK = "A"

# ============================================================
# Logging Configuration
# ============================================================
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
