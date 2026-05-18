import gradio as gr
import os
from dotenv import load_dotenv
from agent import run_pipeline
from personas import (
    NIGERIAN_USERS,
    CATEGORIES,
    OCCASIONS,
    MOODS,
    INTERNAL_VOICES
)

# Load environment variables
load_dotenv()

# Prepare choices for dropdowns
user_choices = [(display, uid) for uid, display in {
    "custom": "✏️ Custom User — Enter your own details",
    **{uid: (
        f"{u['name']} · {u['age']}yrs · "
        f"{u['city']} · {u['occupation']} "
        f"· ⭐{u['avg_rating_given']} avg"
    ) for uid, u in NIGERIAN_USERS.items()}
}.items()]

persona_choices = [(voice["style"], vid) for vid, voice in INTERNAL_VOICES.items()]

def generate_review(user_id, persona_id, name, product_name, category, details, price, occasion, mood):
    # Get user profile
    if user_id == "custom":
        user_profile = {
            "name": name or "Anonymous",
            "age": 25,
            "city": "Lagos",
            "occupation": "Professional",
            "avg_rating_given": 4.0
        }
    else:
        user_profile = NIGERIAN_USERS[user_id]
    
    # Get persona
    persona = INTERNAL_VOICES[persona_id]
    
    # Call the pipeline
    try:
        result = run_pipeline(
            user_profile=user_profile,
            product_name=product_name,
            product_category=category,
            product_details=details,
            price=price,
            occasion=occasion,
            mood=mood,
            persona=persona
        )
        return result.get('review', 'Error generating review')
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio interface
with gr.Blocks(title="Let Naija Speak — AI Review Generator") as demo:
    gr.Markdown("""
    # 🇳🇬 Let Naija Speak
    
    **AI-Powered Nigerian Review Generator**
    
    Built with ✨ by Eniitan Oluwatoyin Shadrack (AUTOMAX LABS)
    
    Grounded in 80,000 real Yelp reviews · Four authentic Nigerian cultural voices
    """)
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 👤 User Profile")
            user_dropdown = gr.Dropdown(
                choices=user_choices,
                label="Select User",
                value="custom"
            )
            persona_dropdown = gr.Dropdown(
                choices=persona_choices,
                label="Cultural Persona",
                value=list(INTERNAL_VOICES.keys())[0]
            )
            name_input = gr.Textbox(
                label="Your Name",
                placeholder="e.g. Amaka, Dele, Kemi...",
                visible=True
            )
            
            gr.Markdown("### 🛍️ Product / Service Details")
            product_name_input = gr.Textbox(
                label="Product Name *",
                placeholder="e.g. Chicken Republic Grilled Chicken"
            )
            category_dropdown = gr.Dropdown(
                choices=CATEGORIES,
                label="Category"
            )
            details_input = gr.Textbox(
                label="Product Details",
                placeholder="Describe the product/service...",
                lines=3
            )
            price_input = gr.Textbox(
                label="Price (₦)",
                placeholder="e.g. 2500"
            )
            occasion_dropdown = gr.Dropdown(
                choices=OCCASIONS,
                label="Occasion"
            )
            mood_dropdown = gr.Dropdown(
                choices=MOODS,
                label="Mood"
            )
            
            generate_btn = gr.Button("🚀 Generate Review", variant="primary")
        
        with gr.Column():
            gr.Markdown("### 📝 Generated Review")
            output_text = gr.Textbox(
                label="Review",
                lines=15,
                interactive=False
            )
    
    # Update name input visibility based on user selection
    def update_name_visibility(user_id):
        return gr.update(visible=user_id == "custom")
    
    user_dropdown.change(
        update_name_visibility,
        inputs=user_dropdown,
        outputs=name_input
    )
    
    # Generate review
    generate_btn.click(
        generate_review,
        inputs=[
            user_dropdown,
            persona_dropdown,
            name_input,
            product_name_input,
            category_dropdown,
            details_input,
            price_input,
            occasion_dropdown,
            mood_dropdown
        ],
        outputs=output_text
    )

if __name__ == "__main__":
    demo.launch()