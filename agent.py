# ============================================================
# agent.py — REVISED
# Cultural voice chosen RANDOMLY and INVISIBLY
# User sees normal profile, gets surprise Nigerian review
# ============================================================

import os
import json
import random
import logging
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from groq import Groq
from personas import (
    INTERNAL_VOICES,
    BEHAVIORAL_PATTERNS
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key from environment
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY environment variable is not set. "
        "Please copy .env.example to .env and add your API key."
    )

client = Groq(api_key=GROQ_API_KEY)


def predict_rating(
    user_profile: Dict[str, Any],
    product_name: str,
    product_category: str,
    product_details: str,
    price: str,
    occasion: str,
    mood: str
) -> Dict[str, Any]:
    """
    Predicts star rating from user behavioral profile.
    
    Uses LLM analysis of user demographics, past behavior, and product context
    to predict the rating a user would give. No cultural labels — pure behavioral modeling.
    
    Args:
        user_profile: Dictionary with keys 'age', 'city', 'occupation', 'income_level',
                     'price_sensitivity', 'rating_tendency', 'avg_rating_given',
                     'total_reviews', 'preferences', 'review_history'
        product_name: Name of the product being reviewed
        product_category: Category/type of product
        product_details: Description of product features/specs
        price: Product price (can be string like "₦5,000")
        occasion: Purchase occasion (e.g., "Regular day purchase", "Holiday gift")
        mood: User's current mood (e.g., "Happy", "Neutral / Normal")
    
    Returns:
        Dictionary containing:
            - predicted_stars (int 1-5): Predicted rating
            - confidence (str): 'low', 'medium', or 'high'
            - key_factors (list): Top 3 factors influencing prediction
            - reasoning (str): One-sentence explanation
    
    Raises:
        ValueError: If GROQ_API_KEY is not set
        json.JSONDecodeError: If LLM response cannot be parsed
    """
    logger.info(f"Predicting rating for {product_name} by user from {user_profile.get('city', 'Unknown')}")
    
    history_block = ""
    if user_profile.get("review_history"):
        history_block = "\nUSER PAST RATINGS:\n"
        for h in user_profile["review_history"]:
            history_block += (
                f"  - {h['stars']}⭐ "
                f"for {h['product']} ({h['category']})\n"
            )

    prompt = f"""You are predicting what star rating a user will give a product.

USER BEHAVIORAL PROFILE:
- Age: {user_profile.get('age', 'Unknown')}
- City: {user_profile.get('city', 'Nigeria')}
- Occupation: {user_profile.get('occupation', 'Unknown')}
- Income Level: {user_profile.get('income_level', 'middle')}
- Price Sensitivity: {user_profile.get('price_sensitivity', 'medium')}
- Rating Tendency: {user_profile.get('rating_tendency', 'honest')}
- Average Rating Given: {user_profile.get('avg_rating_given', 3.5)}
- Total Reviews Written: {user_profile.get('total_reviews', 0)}
- Preferences: {', '.join(user_profile.get('preferences', []))}
{history_block}

PRODUCT BEING REVIEWED:
- Name: {product_name}
- Category: {product_category}
- Details: {product_details}
- Price: {price}
- Purchase Occasion: {occasion}
- User Mood: {mood}

Consider Nigerian market context:
- Price fairness relative to Nigerian income levels
- Quality expectations in Nigerian market
- User's past behavior and tendencies

Reply ONLY in this exact JSON:
{{
  "predicted_stars": <integer 1 to 5>,
  "confidence": "<low or medium or high>",
  "key_factors": ["factor1", "factor2", "factor3"],
  "reasoning": "<one clear sentence>"
}}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
        temperature=0.2
    )

    try:
        raw = response.choices[0].message.content.strip()
        raw = raw.replace("```json", "").replace("```", "").strip()
        result = json.loads(raw)
        logger.info(f"Rating prediction successful: {result['predicted_stars']}⭐")
        return result
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse LLM response as JSON: {e}")
        logger.error(f"Raw response: {raw}")
        return {
            "predicted_stars": 3,
            "confidence": "low",
            "key_factors": ["parsing error"],
            "reasoning": "Could not parse LLM response — defaulted to 3 stars"
        }
    except (IndexError, AttributeError) as e:
        logger.error(f"Unexpected LLM response format: {e}")
        return {
            "predicted_stars": 3,
            "confidence": "low",
            "key_factors": ["format error"],
            "reasoning": "Unexpected LLM response format — defaulted to 3 stars"
        }
    except Exception as e:
        logger.exception(f"Unexpected error in predict_rating: {e}")
        return {
            "predicted_stars": 3,
            "confidence": "low",
            "key_factors": ["unexpected error"],
            "reasoning": "Unexpected error — defaulted to 3 stars"
        }


def generate_review(
    user_profile: Dict[str, Any],
    product_name: str,
    product_category: str,
    product_details: str,
    price: str,
    star_rating: int,
    occasion: str,
    mood: str
) -> str:
    """
    Generates authentic Nigerian review with random cultural voice.
    
    The cultural voice (Yoruba, Igbo, Pidgin, or Professional) is selected RANDOMLY
    and INVISIBLY — user never sees this. Output always sounds authentically Nigerian
    regardless of user profile selection.
    
    Args:
        user_profile: User demographic and behavioral data
        product_name: Name of product being reviewed
        product_category: Category of product
        product_details: Product specifications/features
        price: Product price
        star_rating: Star rating (1-5) to express in review
        occasion: Purchase occasion
        mood: User's current mood
    
    Returns:
        str: Authentic Nigerian review in randomly selected cultural voice
    
    Raises:
        ValueError: If star_rating is outside 1-5 range
    """
    if not (1 <= star_rating <= 5):
        raise ValueError(f"star_rating must be 1-5, got {star_rating}")
    
    logger.info(f"Generating {star_rating}⭐ review for {product_name}")

    # Pick random Nigerian cultural voice — user never sees this
    voice = random.choice(INTERNAL_VOICES)
    pattern = BEHAVIORAL_PATTERNS[star_rating]
    logger.debug(f"Selected voice: {voice['id']}, pattern: {star_rating} stars")

    # Build history context
    history_block = ""
    if user_profile.get("review_history"):
        history_block = "\nUSER PAST REVIEW BEHAVIOR:\n"
        for h in user_profile["review_history"][:3]:
            history_block += (
                f"- Rated {h['product']} "
                f"{h['stars']}⭐\n"
            )

    system_prompt = f"""You are a Nigerian person writing an online product review.

YOUR PROFILE:
- Age: {user_profile.get('age', 25)}
- City: {user_profile.get('city', 'Lagos')}, Nigeria
- Occupation: {user_profile.get('occupation', 'Professional')}
- You have written {user_profile.get('total_reviews', 10)} reviews before
- Your average rating: {user_profile.get('avg_rating_given', 3.5)}/5

YOUR NATURAL WAY OF SPEAKING:
Style: {voice['style']}
Characteristic traits: {voice['traits']}

YOUR NATURAL EXPRESSIONS (use these organically):
{chr(10).join(['• ' + e for e in voice['expressions']])}

BEHAVIORAL DATA FROM REAL YELP REVIEWS:
- Target length: ~{pattern['avg_word_count']} words
- For {star_rating} stars: {pattern['sentiment']}

HOW YOU WRITE REVIEWS:
1. You write exactly like a real Nigerian — raw, natural, unfiltered
2. Your slang comes out naturally mixed with English
3. You reflect your mood ({mood}) in your tone
4. The occasion ({occasion}) shapes your perspective
5. Your energy PERFECTLY matches {star_rating} stars:
   ★☆☆☆☆ Very angry — strong complaints — never going back
   ★★☆☆☆ Disappointed — specific issues — unlikely to return
   ★★★☆☆ Mixed feelings — some good some bad — maybe return
   ★★★★☆ Pleased — minor issues — will return and recommend
   ★★★★★ Extremely excited — telling everyone — best experience
6. You sound like you are typing on your phone casually
7. You NEVER translate your Nigerian expressions
8. You end with whether you will return or recommend"""

    user_prompt = f"""Write your review for this product:

PRODUCT: {product_name}
CATEGORY: {product_category}
DETAILS: {product_details}
PRICE: {price}
YOUR RATING: {star_rating}/5 stars
OCCASION: {occasion}
YOUR MOOD: {mood}
{history_block}

Write ONLY the review. Start directly."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=400,
        temperature=0.88
    )

    return response.choices[0].message.content.strip()


def run_pipeline(
    user_profile: Dict[str, Any],
    product_name: str,
    product_category: str,
    product_details: str,
    price: str,
    manual_stars: int,
    use_prediction: bool,
    occasion: str,
    mood: str
) -> Dict[str, Any]:
    """
    Full review generation pipeline.
    
    Orchestrates the complete workflow:
    1. Predict rating from user behavioral profile
    2. Select between predicted or manual rating
    3. Generate authentic Nigerian review
    4. Return all results with evaluation metrics
    
    Args:
        user_profile: User demographic and behavioral data
        product_name: Name of product
        product_category: Product category
        product_details: Product details
        price: Product price
        manual_stars: Manual star rating (1-5) if user provides it
        use_prediction: Whether to use AI prediction or manual stars
        occasion: Purchase occasion
        mood: User's mood
    
    Returns:
        Dictionary with keys:
            - review: Generated review text
            - final_stars: Final star rating used
            - predicted_stars: AI predicted rating
            - confidence: Prediction confidence
            - key_factors: Top factors in prediction
            - reasoning: Explanation of prediction
            - word_count: Actual word count in review
            - expected_words: Expected word count for rating
    """
    logger.info(f"Starting pipeline for {product_name}, use_prediction={use_prediction}")
    
    # Step 1: Predict
    prediction = predict_rating(
        user_profile, product_name,
        product_category, product_details,
        price, occasion, mood
    )

    # Step 2: Choose rating
    final_stars = (
        prediction["predicted_stars"]
        if use_prediction
        else int(manual_stars)
    )
    logger.info(f"Final rating: {final_stars}⭐ (predicted={use_prediction})")

    # Step 3: Generate with invisible random Nigerian voice
    review = generate_review(
        user_profile, product_name,
        product_category, product_details,
        price, final_stars, occasion, mood
    )
    logger.info(f"Review generated: {len(review.split())} words")

    return {
        "review": review,
        "final_stars": final_stars,
        "predicted_stars": prediction["predicted_stars"],
        "confidence": prediction["confidence"],
        "key_factors": prediction["key_factors"],
        "reasoning": prediction["reasoning"],
        "word_count": len(review.split()),
        "expected_words": BEHAVIORAL_PATTERNS[final_stars]["avg_word_count"]
    }