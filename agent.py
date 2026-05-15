# ============================================================
# agent.py — REVISED
# Cultural voice chosen RANDOMLY and INVISIBLY
# User sees normal profile, gets surprise Nigerian review
# ============================================================

import os
import json
import random
from groq import Groq
from personas import (
    INTERNAL_VOICES,
    BEHAVIORAL_PATTERNS
)

GROQ_API_KEY = os.environ.get("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", "")
client = Groq(api_key=GROQ_API_KEY)


def predict_rating(user_profile, product_name,
                   product_category, product_details,
                   price, occasion, mood):
    """
    Predicts star rating from user behavioral profile.
    No cultural labels — pure behavioral modeling.
    """
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
        return json.loads(raw)
    except:
        return {
            "predicted_stars": 3,
            "confidence": "low",
            "key_factors": ["default used"],
            "reasoning": "Could not parse — defaulted to 3 stars"
        }


def generate_review(user_profile, product_name,
                    product_category, product_details,
                    price, star_rating, occasion, mood):
    """
    Generates authentic Nigerian review.
    Cultural voice selected RANDOMLY — invisible to user.
    Output always sounds Nigerian regardless of profile.
    """

    # Pick random Nigerian cultural voice — user never sees this
    voice = random.choice(INTERNAL_VOICES)
    pattern = BEHAVIORAL_PATTERNS[star_rating]

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


def run_pipeline(user_profile, product_name,
                 product_category, product_details,
                 price, manual_stars, use_prediction,
                 occasion, mood):
    """
    Full pipeline:
    1. Predict rating from behavioral profile
    2. Generate Nigerian review with random cultural voice
    3. Return all results
    """

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

    # Step 3: Generate with invisible random Nigerian voice
    review = generate_review(
        user_profile, product_name,
        product_category, product_details,
        price, final_stars, occasion, mood
    )

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