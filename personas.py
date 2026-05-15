INTERNAL_VOICES = [
    {
        "id": "yoruba_voice",
        "expressions": [
            "Omo this thing sweet die!",
            "Abeg I no go lie,",
            "Shey you understand? The quality ehn!",
            "Wahala no dey for here at all",
            "Gbam! That's the truth",
            "E be like say dem sabi their work sha",
            "Oya make I tell you,"
        ],
        "traits": "Uses: omo, abeg, sabi, wahala, gbam, shey, ehn, oya",
        "style": "Energetic, expressive, emotional, Lagos street energy"
    },
    {
        "id": "igbo_voice",
        "expressions": [
            "Nna men, I no fit lie,",
            "Chai! This thing scatter my mind",
            "Biko listen to me,",
            "Chineke! The price ehn",
            "Ọ dị mma I swear,",
            "Tufiakwa! That kind service no good",
            "Nna the quality dey show"
        ],
        "traits": "Uses: nna men, chai, tufiakwa, ọ dị mma, chineke, biko",
        "style": "Passionate, very honest, detailed, straight talking"
    },
    {
        "id": "pidgin_voice",
        "expressions": [
            "How far! Make I tell you,",
            "E sweet die, no be small thing",
            "Wetin dem put inside this thing?",
            "I nor go lie to you,",
            "Dem try die for this one",
            "Make una hear this,",
            "E don do! This na the real deal"
        ],
        "traits": "Uses: how far, wetin, nor be, make I, e sweet, e don do",
        "style": "Casual, funny, punchy, very relatable naija energy"
    },
    {
        "id": "formal_naija_voice",
        "expressions": [
            "I must say, this exceeded my expectations,",
            "As a Nigerian who has experienced both local and international standards,",
            "Frankly speaking,",
            "The value for money is quite reasonable sha",
            "I would strongly recommend this to my people",
            "All in all, e good"
        ],
        "traits": "Mostly formal English, occasional Nigerian expressions",
        "style": "Professional, balanced, credible, detailed"
    }
]

# ============================================================
# NORMAL USER PROFILES — grounded in Yelp dataset behavior
# These look like real review platform users
# No tribal labels visible to user
# ============================================================

NIGERIAN_USERS = {
    "custom": {
        "name": "Custom User",
        "age": 25,
        "city": "Lagos",
        "occupation": "Not specified",
        "income_level": "middle",
        "price_sensitivity": "medium",
        "rating_tendency": "honest",
        "total_reviews": 0,
        "avg_rating_given": 3.5,
        "preferences": [],
        "review_history": []
    },
    "user_001": {
        "name": "Chukwuemeka Obi",
        "age": 28,
        "city": "Lagos",
        "occupation": "Software Engineer",
        "income_level": "middle",
        "price_sensitivity": "medium",
        "rating_tendency": "honest",
        "total_reviews": 47,
        "avg_rating_given": 3.8,
        "preferences": ["tech gadgets", "food", "music"],
        "review_history": [
            {"product": "Tecno Camon 30", "category": "Electronics", "stars": 5},
            {"product": "Mr Biggs Restaurant", "category": "Food", "stars": 2},
            {"product": "Spotify Premium", "category": "Streaming", "stars": 5},
            {"product": "Jumia Delivery", "category": "E-commerce", "stars": 3}
        ]
    },
    "user_002": {
        "name": "Folake Adeyemi",
        "age": 24,
        "city": "Ibadan",
        "occupation": "Fashion Designer",
        "income_level": "middle",
        "price_sensitivity": "high",
        "rating_tendency": "generous",
        "total_reviews": 83,
        "avg_rating_given": 4.2,
        "preferences": ["fashion", "beauty", "food", "lifestyle"],
        "review_history": [
            {"product": "Zara Online Store", "category": "Fashion", "stars": 4},
            {"product": "Chicken Republic", "category": "Food", "stars": 5},
            {"product": "Netflix Nigeria", "category": "Streaming", "stars": 4},
            {"product": "MAC Cosmetics", "category": "Beauty", "stars": 5}
        ]
    },
    "user_003": {
        "name": "Emeka Nwosu",
        "age": 35,
        "city": "Port Harcourt",
        "occupation": "Oil & Gas Worker",
        "income_level": "high",
        "price_sensitivity": "low",
        "rating_tendency": "generous",
        "total_reviews": 29,
        "avg_rating_given": 4.1,
        "preferences": ["sports", "food", "drinks", "electronics"],
        "review_history": [
            {"product": "Star Beer", "category": "Drinks", "stars": 5},
            {"product": "DSTV Premium", "category": "Entertainment", "stars": 3},
            {"product": "Buka Pepper Soup", "category": "Food", "stars": 5},
            {"product": "Samsung TV", "category": "Electronics", "stars": 4}
        ]
    },
    "user_004": {
        "name": "Adaeze Okonkwo",
        "age": 42,
        "city": "Abuja",
        "occupation": "Medical Doctor",
        "income_level": "high",
        "price_sensitivity": "low",
        "rating_tendency": "critical",
        "total_reviews": 61,
        "avg_rating_given": 3.4,
        "preferences": ["health", "books", "premium services", "travel"],
        "review_history": [
            {"product": "Transcorp Hilton", "category": "Hotel", "stars": 4},
            {"product": "Jumia Health", "category": "Health", "stars": 3},
            {"product": "Amazon Kindle", "category": "Electronics", "stars": 5},
            {"product": "Uber Abuja", "category": "Transport", "stars": 2}
        ]
    },
    "user_005": {
        "name": "Tunde Bakare",
        "age": 19,
        "city": "Lagos",
        "occupation": "University Student",
        "income_level": "low",
        "price_sensitivity": "very_high",
        "rating_tendency": "extreme",
        "total_reviews": 112,
        "avg_rating_given": 3.9,
        "preferences": ["gaming", "music", "social media", "cheap food"],
        "review_history": [
            {"product": "PUBG Mobile", "category": "Gaming", "stars": 5},
            {"product": "Indomie Noodles", "category": "Food", "stars": 5},
            {"product": "MTN Data Bundle", "category": "Telecom", "stars": 1},
            {"product": "Bolt Ride", "category": "Transport", "stars": 3}
        ]
    },
    "user_006": {
        "name": "Ngozi Eze",
        "age": 31,
        "city": "Enugu",
        "occupation": "Nurse",
        "income_level": "middle",
        "price_sensitivity": "high",
        "rating_tendency": "honest",
        "total_reviews": 38,
        "avg_rating_given": 3.7,
        "preferences": ["health products", "family items", "food", "fashion"],
        "review_history": [
            {"product": "Konga Groceries", "category": "E-commerce", "stars": 4},
            {"product": "Chi Exotic Juice", "category": "Food", "stars": 4},
            {"product": "Uber Health", "category": "Health", "stars": 3},
            {"product": "Ankara Fabric Store", "category": "Fashion", "stars": 5}
        ]
    },
    "user_007": {
        "name": "Babatunde Ogunleye",
        "age": 45,
        "city": "Lagos",
        "occupation": "Business Owner",
        "income_level": "high",
        "price_sensitivity": "medium",
        "rating_tendency": "honest",
        "total_reviews": 94,
        "avg_rating_given": 3.6,
        "preferences": ["business tools", "food", "transport", "premium services"],
        "review_history": [
            {"product": "Eko Hotel", "category": "Hotel", "stars": 4},
            {"product": "Opay Business", "category": "Fintech", "stars": 5},
            {"product": "Dana Air", "category": "Transport", "stars": 2},
            {"product": "Buka Restaurant", "category": "Food", "stars": 5}
        ]
    },
    "user_008": {
        "name": "Amina Yusuf",
        "age": 27,
        "city": "Kano",
        "occupation": "Teacher",
        "income_level": "low",
        "price_sensitivity": "very_high",
        "rating_tendency": "honest",
        "total_reviews": 22,
        "avg_rating_given": 3.5,
        "preferences": ["education", "family", "food", "affordable products"],
        "review_history": [
            {"product": "Kano Suya Spot", "category": "Food", "stars": 5},
            {"product": "Cowrywise Savings", "category": "Fintech", "stars": 4},
            {"product": "NIPOST Delivery", "category": "Delivery", "stars": 1},
            {"product": "Udemy Course", "category": "Education", "stars": 4}
        ]
    }
}

CATEGORIES = [
    "Restaurant / Food",
    "Electronics / Gadgets",
    "Fashion / Clothing",
    "Hotel / Accommodation",
    "Beauty / Wellness",
    "Entertainment / Streaming",
    "Transport / Ride-hailing",
    "E-commerce / Shopping",
    "Education / Courses",
    "Health / Pharmacy",
    "Banking / Fintech",
    "Gaming"
]

OCCASIONS = [
    "Regular day purchase",
    "Special occasion / celebration",
    "Work / business related",
    "Gift for someone",
    "Emergency purchase",
    "First time trying",
    "Repeat purchase"
]

MOODS = [
    "Happy / Excited",
    "Neutral / Normal",
    "Tired / Stressed",
    "Skeptical / Cautious",
    "Disappointed",
    "Impressed"
]

BEHAVIORAL_PATTERNS = {
    1: {
        "avg_word_count": 120,
        "sentiment": "terrible, horrible, awful, worst, never return, waste, rude"
    },
    2: {
        "avg_word_count": 105,
        "sentiment": "disappointing, poor, below average, slow, overpriced, mediocre"
    },
    3: {
        "avg_word_count": 95,
        "sentiment": "okay, average, decent, mixed, could be better, alright"
    },
    4: {
        "avg_word_count": 100,
        "sentiment": "good, great, nice, recommended, satisfied, friendly, clean"
    },
    5: {
        "avg_word_count": 115,
        "sentiment": "amazing, excellent, best, love, perfect, fantastic, incredible"
    }
}