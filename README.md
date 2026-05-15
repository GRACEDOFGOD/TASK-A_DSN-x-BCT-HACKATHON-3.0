# 🇳🇬 Nigerian AI Review Generator — Task A

**DSN × BCT Hackathon 3.0 | Task A: User Modeling Agent**

> An LLM-powered agent that generates culturally authentic Nigerian
> reviews grounded in 80,000 real Yelp reviews.

---

## What It Does

- Takes **user persona + product details** as input
- Predicts the **star rating** that persona would give
- Generates an **authentic Nigerian review** in their cultural voice
- Evaluated with **ROUGE, RMSE, and Behavioural Fidelity**

## Four Nigerian Cultural Voices

| Persona | Voice Style |
|---|---|
| 🟡 Yoruba (Lagos) | Omo, abeg, wahala, gbam, shey |
| 🔵 Igbo (Eastern) | Nna men, chai, tufiakwa, ọ dị mma |
| 🟢 Naija Pidgin | How far, wetin, e sweet die, e don do |
| ⚫ Nigerian Professional | Formal English with subtle Nigerian flavour |

## Evaluation Results (from Colab analysis)

| Metric | Score |
|---|---|
| ROUGE-1 | 0.1597 |
| ROUGE-L | 0.0937 |
| Behavioural Fidelity | 0.7833 |
| Rating RMSE | 1.1402 |
| Rating MAE | 0.6000 |

> Note: Low ROUGE scores are expected — our Nigerian cultural
> voice deliberately diverges from standard American English
> Yelp reviews. Behavioural Fidelity (0.78) is the primary
> quality signal.

## Dataset

**Yelp Review Full** — 80,000 reviews loaded from HuggingFace.
Used for behavioral pattern extraction and ROUGE evaluation.

## Tech Stack

- **LLM:** Groq LLaMA 3.3 70B
- **Backend:** Flask
- **Frontend:** HTML/CSS/JavaScript
- **Evaluation:** ROUGE-Score, RMSE, Behavioural Fidelity
- **Dataset:** Yelp (HuggingFace)

## Run Locally

```bash
git clone https://github.com/GRACEDOFGOD/DSN-BCT-Hackathon.git
cd DSN-BCT-Hackathon/task_a
pip install -r requirements.txt
export GROQ_API_KEY=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
python app.py
```

Visit: http://localhost:7860

## Project Structure

```
task_a/
├── app.py           # Flask web server
├── agent.py         # AI agent (predict + generate)
├── personas.py      # Nigerian personas + user profiles
├── requirements.txt
├── README.md
└── templates/
    └── index.html   # Web UI
```