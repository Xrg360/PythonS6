import gradio as gr
import numpy as np
from joblib import load

# Load the models from files
trained_model = load('trained_model.pkl')
model4 = load('model4.pkl')

# Define dictionaries to map each dropdown option to a specific number
gender_mapping = {"Male": 0, "Female": 1}
backlogs_mapping = {"None": 0, "Less than 5": 1, "Greater than 5": 2}
sleep_mapping = {"Less than 7hr": 0, "7hr": 1, "More than 7hr": 2}
concentration_mapping = {"15min - 30min": 0, "30min - 45min": 1, "More than 45min": 2}
age_mapping = {"15-20": 0, "20-25": 1, "25-30": 2}
academic_level_mapping = {"HIGHER SECONDARY": 0, "UNDER GRADUATE": 1, "POST GRADUATE": 2}
satisfaction_mapping = {"Not at all": 0, "Neutral": 1, "Slightly": 2, "Extremely": 3}
absent_days_mapping = {"Less than 10": 0, "Less than 30": 1, "More than 30": 2}
info_delivery_mapping = {
    "Read/Write": 0,
    "Visual(Pictures / Diagrams)": 1,
    "Auditory": 2,
    "Kinaesthetic (learning by physical activity and hands-on experiences.)": 3
}
study_time_mapping = {"Less than 1 hour": 0, "1-3 hours": 1, "more than 3 hours": 2}
grades_mapping = {"Less than 50%": 0, "50-70%": 1, "70-90%": 2, "Greater than 90%": 3}

# Define dictionaries to map predictions from models to specific text and redirecting links
trained_model_text_mapping = {
    0: ("Eisenhower Matrix", "C:/Users/pjee1/OneDrive/Desktop/juypter/openai/main/eisen.html"),
    1: ("Feynman Technique", "C:/Users/pjee1/OneDrive/Desktop/juypter/openai/main/feynman.html"),
    2: ("Flowtime Technique", "C:/Users/pjee1/OneDrive/Desktop/juypter/openai/main/flowtime.html"),
    3: ("SMART Goals Technique", "C:/Users/pjee1/OneDrive/Desktop/juypter/openai/main/smart.html")
}

model4_text_mapping = {
    0: ("Pomodoro Technique", "C:/Users/pjee1/OneDrive/Desktop/juypter/openai/main/pomodoro.html"),
    1: ("Time Blocking Technique", "C:/Users/pjee1/OneDrive/Desktop/juypter/openai/main/timeblocking.html")
}

# Define the predict function
def predict(gender=None, age=None, sleep=None, academic_level=None, backlogs=None, concentration=None, currently_satisfied=None, absent_days=None,
            info_delivery=None, raise_hands=None, study_time=None, grades=None):
    # Set default values if None
    gender = gender or "Male"
    age = age or "15-20"
    sleep = sleep or "Less than 7hr"
    academic_level = academic_level or "HIGHER SECONDARY"
    backlogs = backlogs or "None"
    concentration = concentration or "15min - 30min"
    currently_satisfied = currently_satisfied or "Not at all"
    absent_days = absent_days or "Less than 10"
    info_delivery = info_delivery or "Read/Write"
    raise_hands = raise_hands or 0
    study_time = study_time or "Less than 1 hour"
    grades = grades or "Less than 50%"

    # Convert each input using the mapping dictionaries
    gender_num = gender_mapping[gender]
    age_num = age_mapping[age]
    sleep_num = sleep_mapping[sleep]
    academic_level_num = academic_level_mapping[academic_level]
    backlogs_num = backlogs_mapping[backlogs]
    concentration_num = concentration_mapping[concentration]
    satisfaction_num = satisfaction_mapping[currently_satisfied]
    absent_days_num = absent_days_mapping[absent_days]
    info_delivery_num = info_delivery_mapping[info_delivery]
    study_time_num = study_time_mapping[study_time]
    grades_num = grades_mapping[grades]

    # Combine the input data into an array
    input_data = [
        gender_num, age_num, sleep_num, academic_level_num, backlogs_num,
        concentration_num, satisfaction_num, absent_days_num, info_delivery_num,
        raise_hands, study_time_num, grades_num
    ]

    # Convert the list to a numpy array and reshape it for the models
    input_data_reshaped = np.array(input_data).reshape(1, -1)

    # Predict using the models
    y_pred_trained_model = trained_model.predict(input_data_reshaped)
    y_pred_model4 = model4.predict(input_data_reshaped)

    # Retrieve text corresponding to the predictions from the dictionaries
    trained_model_text, trained_model_link = trained_model_text_mapping[y_pred_trained_model[0]]
    model4_text, model4_link = model4_text_mapping[y_pred_model4[0]]

    # Generate redirection links based on predictions
    redirect_link_trained_model = f'<a href="{trained_model_link}" target="_blank">Go to {trained_model_text}</a>'
    redirect_link_model4 = f'<a href="file:///{model4_link}" target="_blank">Go to {model4_text}</a>'

    # Return the predictions, text, and redirection links
    return trained_model_text, redirect_link_trained_model, model4_text, redirect_link_model4


# Define CSS styles
css = """
.header {
    background-color: #888;
    padding: 10px;
    color: white;
    text-align: center;
}

.body {
    background-image: url('image5.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    padding: 20px;
    margin-top: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
"""

# Create the Gradio interface with CSS styles
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Dropdown(["Male", "Female"], label="Gender"),
        gr.Dropdown(["15-20", "20-25", "25-30"], label="Age"),
        gr.Dropdown(["Less than 7hr", "7hr", "More than 7hr"],
                   label="How long do you sleep for on a regular day?"),
        gr.Dropdown(["HIGHER SECONDARY", "UNDER GRADUATE", "POST GRADUATE"], label="Academic Level"),
        gr.Dropdown(["None", "Less than 5", "Greater than 5"], label="Backlogs"),
        gr.Dropdown(["15min - 30min", "30min - 45min", "More than 45min"],
                   label="How long are you able to concentrate on your studies for a continuous period of time?"),
        gr.Dropdown(["Not at all", "Neutral", "Slightly", "Extremely"],
                   label="How much do you enjoy the way you're learning stuff right now?"),
        gr.Dropdown(["Less than 10", "Less than 30", "More than 30"],
                   label="How often would say you were absent in your last semester?"),
        gr.Dropdown([
            "Read/Write",
            "Visual(Pictures / Diagrams)",
            "Auditory",
            "Kinaesthetic (learning by physical activity and hands-on experiences.)"
        ], label="What type of information delivery works best for you?"),
        gr.Slider(0, 5, step=1, label="How often do you raise hands or speak up in class?"),
        gr.Dropdown(["Less than 1 hour", "1-3 hours", "more than 3 hours"],
                   label="How long do you study for on a regular day?"),
        gr.Dropdown(["Less than 50%", "50-70%", "70-90%", "Greater than 90%"],
                   label="How did you do in your most recent important exam, like the final semester exam or boards?")
    ],
    outputs=[
        gr.Textbox(label="Learning strategy"),
        gr.HTML(label="Redirection link from trained_model"),
        gr.Textbox(label="Time Management Strategies"),
        gr.HTML(label="Redirection link from model4")
    ],
    title="Student app",
    css=css
)

# Launch the Gradio app
iface.launch(share=True)