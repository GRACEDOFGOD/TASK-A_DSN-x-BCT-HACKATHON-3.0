# ============================================================
# app.py
# Flask web server — Task A: Nigerian Review Generator
# DSN x BCT Hackathon 3.0
# ===========================================================
from flask import Flask, render_template, request, jsonify
from agent import run_pipeline
from personas import (
    NIGERIAN_USERS,
    CATEGORIES,
    OCCASIONS,
    MOODS,
    INTERNAL_VOICES
)
import math

app = Flask(__name__)
session_predictions = []

def compute_session_rmse():
    if len(session_predictions) < 2:
        return None
    errors = [(p["actual"] - p["predicted"]) ** 2
              for p in session_predictions]
    return round(math.sqrt(sum(errors) / len(errors)), 4)


@app.route('/')
def index():
    users = {}
    for uid, u in NIGERIAN_USERS.items():
        if uid == "custom":
            users[uid] = "✏️ Custom User — Enter your own details"
        else:
            users[uid] = (
                f"{u['name']} · {u['age']}yrs · "
                f"{u['city']} · {u['occupation']} "
                f"· ⭐{u['avg_rating_given']} avg"
            )

            personas = {
                voice["id"]: voice["style"]
                for voice in INTERNAL_VOICES
            }
    return render_template(
        'index.html',
        users=users,
                personas=personas,
        categories=CATEGORIES,
        occasions=OCCASIONS,
        moods=MOODS
    )


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json

    if not data.get('product_name', '').strip():
        return jsonify({
            "success": False,
            "error": "Product name is required"
        }), 400

    user_id = data.get('user_id', 'custom')
    user_profile = NIGERIAN_USERS.get(
        user_id, NIGERIAN_USERS['custom']
    )

    # For custom user, use their entered details
    if user_id == 'custom':
        user_profile = {
            **NIGERIAN_USERS['custom'],
            "name": data.get('custom_name', 'Anonymous'),
            "age": int(data.get('custom_age', 25)),
            "city": data.get('custom_city', 'Lagos'),
            "occupation": data.get('custom_occupation', 'Professional'),
            "price_sensitivity": data.get(
                'custom_price_sensitivity', 'medium'
            ),
            "rating_tendency": "honest",
            "avg_rating_given": 3.5,
            "total_reviews": 0,
            "review_history": []
        }

    try:
        result = run_pipeline(
            user_profile=user_profile,
            product_name=data.get('product_name', ''),
            product_category=data.get('product_category', ''),
            product_details=data.get('product_details', ''),
            price=data.get('price', 'Not specified'),
            manual_stars=int(data.get('manual_stars', 3)),
            use_prediction=data.get('use_prediction', True),
            occasion=data.get('occasion', 'Regular day purchase'),
            mood=data.get('mood', 'Neutral / Normal')
        )

        session_predictions.append({
            "actual": int(data.get('manual_stars', 3)),
            "predicted": result["predicted_stars"]
        })

        fidelity = max(
            0,
            1 - abs(result["word_count"] - result["expected_words"])
            / max(result["expected_words"], 1)
        )

        return jsonify({
            "success": True,
            "review": result["review"],
            "final_stars": result["final_stars"],
            "predicted_stars": result["predicted_stars"],
            "confidence": result["confidence"],
            "key_factors": result["key_factors"],
            "reasoning": result["reasoning"],
            "word_count": result["word_count"],
            "expected_words": result["expected_words"],
            "behavioral_fidelity": round(fidelity, 4),
            "session_rmse": compute_session_rmse(),
            "session_count": len(session_predictions),
            "user_name": user_profile["name"],
            "user_city": user_profile.get("city", "Nigeria"),
            "user_occupation": user_profile.get("occupation", ""),
            "user_avg_rating": user_profile.get("avg_rating_given", 3.5),
            "user_total_reviews": user_profile.get("total_reviews", 0),
            "rating_tendency": user_profile.get("rating_tendency", "honest")
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/health')
def health():
    return jsonify({"status": "running", "task": "A"})


if __name__ == '__main__':
    app.run(debug=True, port=7860, host='0.0.0.0')