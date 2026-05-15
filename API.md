# 📖 API Documentation

## Base URL

```
http://127.0.0.1:7860
```

## Endpoints

### 1. Health Check

**Endpoint:** `GET /health`

**Description:** Verify the application is running

**Response (200 OK):**
```json
{
  "status": "running",
  "task": "A"
}
```

---

### 2. Home Page

**Endpoint:** `GET /`

**Description:** Serves the web interface for the application

**Response:** HTML page with the review generator UI

---

### 3. Generate Review

**Endpoint:** `POST /generate`

**Description:** Generate an authentic Nigerian review based on user profile and product details

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "user_id": "chukwuemeka",
  "product_name": "Tecno Spark 10 Pro",
  "product_category": "Smartphones",
  "product_details": "6.5-inch display, 50MP camera, 5000mAh battery",
  "price": "₦89,999",
  "manual_stars": 4,
  "use_prediction": true,
  "occasion": "Regular day purchase",
  "mood": "Neutral / Normal",
  "custom_name": "Chidimma",
  "custom_age": 28,
  "custom_city": "Lagos",
  "custom_occupation": "Software Engineer",
  "custom_price_sensitivity": "medium"
}
```

#### Request Parameters:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `user_id` | string | Yes | User identifier or "custom" for custom profile |
| `product_name` | string | Yes | Name of product being reviewed (cannot be empty) |
| `product_category` | string | No | Product category (e.g., "Electronics", "Food") |
| `product_details` | string | No | Detailed description of the product |
| `price` | string | No | Product price (any format, e.g., "₦5,000", "$50") |
| `manual_stars` | integer | No | Manual star rating (1-5). Default: 3 |
| `use_prediction` | boolean | No | Use AI prediction instead of manual stars. Default: true |
| `occasion` | string | No | Purchase occasion (e.g., "Holiday", "Regular day") |
| `mood` | string | No | User's mood (e.g., "Happy", "Neutral") |
| `custom_name` | string | Required if user_id="custom" | User's name |
| `custom_age` | integer | Required if user_id="custom" | User's age |
| `custom_city` | string | Required if user_id="custom" | User's city |
| `custom_occupation` | string | Required if user_id="custom" | User's occupation |
| `custom_price_sensitivity` | string | Required if user_id="custom" | Price sensitivity level |

#### Response (200 OK):

```json
{
  "success": true,
  "review": "Abeg, this Tecno phone is sick! E come with proper features wey no dey cause wahala. The camera sharp sharp, battery last the whole day without issue. Shey the price is fair? I go return and buy again because e no disappoint. A strong 4⭐ for Tecno team.",
  "final_stars": 4,
  "predicted_stars": 4,
  "confidence": "high",
  "key_factors": ["Battery performance", "Camera quality", "Fair pricing"],
  "reasoning": "Strong previous buyer profile, good experience with similar products, fair price in Nigerian market",
  "word_count": 65,
  "expected_words": 85,
  "behavioral_fidelity": 0.7647,
  "session_rmse": 0.5,
  "session_count": 1,
  "user_name": "Chukwuemeka",
  "user_city": "Lagos",
  "user_occupation": "Software Engineer",
  "user_avg_rating": 3.8,
  "user_total_reviews": 15,
  "rating_tendency": "honest"
}
```

#### Response Fields:

| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Whether the request was successful |
| `review` | string | Generated authentic Nigerian review |
| `final_stars` | integer | Star rating used in review (1-5) |
| `predicted_stars` | integer | AI predicted rating |
| `confidence` | string | Confidence level of prediction ("low", "medium", "high") |
| `key_factors` | array | Top 3 factors influencing the rating |
| `reasoning` | string | One-sentence explanation of prediction |
| `word_count` | integer | Actual word count in generated review |
| `expected_words` | integer | Expected word count for this rating |
| `behavioral_fidelity` | float | 0-1 score of review authenticity |
| `session_rmse` | float | RMSE of all predictions in session (null if < 2) |
| `session_count` | integer | Number of reviews generated in session |
| `user_name` | string | Name of reviewer |
| `user_city` | string | City of reviewer |
| `user_occupation` | string | Occupation of reviewer |
| `user_avg_rating` | float | Average rating user gives |
| `user_total_reviews` | integer | Total reviews by user |
| `rating_tendency` | string | User's rating tendency ("honest", "generous", "harsh") |

#### Error Response (400 Bad Request):

```json
{
  "success": false,
  "error": "Product name is required"
}
```

#### Error Response (500 Internal Server Error):

```json
{
  "success": false,
  "error": "GROQ_API_KEY environment variable is not set"
}
```

---

## Available User Profiles

### Preset Users (use user_id instead of custom fields):

1. **chukwuemeka** - Chukwuemeka Obi, 28, Lagos, Software Engineer ⭐3.8
2. **folake** - Folake Adeyemi, 24, Ibadan, Fashion Designer ⭐4.2
3. **emeka** - Emeka Nwosu, 35, Port Harcourt, Oil & Gas Worker ⭐4.1
4. **adaeze** - Adaeze Okonkwo, 42, Abuja, Medical Doctor ⭐3.4
5. **tunde** - Tunde Bakare, 19, Lagos, University Student ⭐3.9
6. **ngozi** - Ngozi Eze, 31, Enugu, Nurse ⭐3.7
7. **babatunde** - Babatunde Ogunleye, 45, Lagos, Business Owner ⭐3.6
8. **amina** - Amina Yusuf, 27, Kano, Teacher ⭐3.5

### Cultural Personas (voices):

1. **Energetic, expressive, emotional, Lagos street energy** (Yoruba)
2. **Passionate, very honest, detailed, straight talking** (Igbo)
3. **Casual, funny, punchy, very relatable naija energy** (Pidgin)
4. **Professional, balanced, credible, detailed** (Nigerian Professional)

---

## Usage Examples

### Example 1: Predict Rating with Preset User

```bash
curl -X POST http://127.0.0.1:7860/generate \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "chukwuemeka",
    "product_name": "Chicken Republic Grilled Chicken",
    "product_category": "Fast Food",
    "price": "₦2,500",
    "use_prediction": true,
    "occasion": "Lunch break"
  }'
```

### Example 2: Manual Rating with Custom User

```bash
curl -X POST http://127.0.0.1:7860/generate \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "custom",
    "custom_name": "Bola",
    "custom_age": 35,
    "custom_city": "Ibadan",
    "custom_occupation": "Trader",
    "custom_price_sensitivity": "high",
    "product_name": "Samsung Galaxy A15",
    "product_category": "Smartphones",
    "product_details": "6.5-inch display, 50MP main camera",
    "price": "₦150,000",
    "manual_stars": 5,
    "use_prediction": false
  }'
```

### Example 3: Python Request

```python
import requests
import json

url = "http://127.0.0.1:7860/generate"
payload = {
    "user_id": "folake",
    "product_name": "Ankara Fabric",
    "product_category": "Textiles",
    "price": "₦800/yard",
    "use_prediction": true,
    "mood": "Happy"
}

response = requests.post(url, json=payload)
result = response.json()

print(f"Review: {result['review']}")
print(f"Stars: {result['final_stars']}⭐")
print(f"Confidence: {result['confidence']}")
```

---

## Error Codes

| Code | Message | Cause | Solution |
|------|---------|-------|----------|
| 400 | Product name is required | Missing product_name field | Add product_name to request |
| 400 | Custom fields required | user_id="custom" but missing custom fields | Fill in all custom_* fields |
| 500 | GROQ_API_KEY not set | Missing environment variable | Set GROQ_API_KEY in .env |
| 500 | Invalid JSON response | LLM returned unexpected format | Retry or contact support |

---

## Rate Limiting

Currently no rate limiting is enforced. The application is rate-limited by the Groq API (check their documentation).

---

## Best Practices

1. **Always include `product_name`** - This is the only required field
2. **Use preset users** when testing to avoid redundant field entry
3. **Set `use_prediction=false`** to test specific ratings
4. **Check `behavioral_fidelity`** - Higher values (> 0.7) indicate more authentic reviews
5. **Monitor `session_rmse`** - Low RMSE indicates consistent predictions

---

## Support

For issues or questions, refer to:
- [SETUP.md](SETUP.md) - Installation help
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common issues
- [README.md](README.md) - Project overview
