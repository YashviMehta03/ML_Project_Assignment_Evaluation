import streamlit as st
import time

st.set_page_config(page_title="Handwritten Assignment Evaluation", layout="wide")

# --------------------------
# Custom CSS for Larger Font
# --------------------------
st.markdown("""
    <style>
        .big-font {
            font-size:20px !important;
            line-height:1.5;
        }
        .question-font {
            font-size:22px !important;
            font-weight:600;
        }
        .header-font {
            font-size:26px !important;
            font-weight:700;
        }
    </style>
""", unsafe_allow_html=True)
st.title("📝 Handwritten Assignment Evaluation")

# --------------------------
# Hardcoded Teacher Answers
# --------------------------
# Questions for teacher + student
questions_text = {
    "Question 1": "Explain the bias–variance tradeoff in machine learning. Why is it important for model generalization?",
    "Question 2": "What is a Support Vector Machine (SVM), and how does it classify data using hyperplanes and kernel functions?",
    "Question 3": "What is bagging in ensemble learning? Describe how it works and why it improves model performance."
}

# Hardcoded Teacher Answers (Exact text provided by you)
teacher_answers = {
    "Question 1": """The bias–variance tradeoff explains how a model’s learning capacity affects its performance.
A model with high bias is too simple and underfits it cannot capture the underlying patterns in the data, leading to consistently high errors on both training and test sets.
A model with high variance is too complex and overfits it memorizes the training data, performs well on it, but fails to generalize to new, unseen data. The goal is to find a balance where the model is expressive enough to learn important patterns but not so flexible that it captures noise.
Achieving this tradeoff leads to a model that generalizes well and performs reliably on new inputs, such as unseen images or text samples.""",

    "Question 2": """A Support Vector Machine (SVM) is a supervised learning algorithm used primarily for classification but also applicable to regression tasks. SVM works by finding an optimal decision boundary (hyperplane) that maximally separates data points of different classes. The key idea is to maximize the margin, which is the distance between the hyperplane and the closest data points, known as support vectors. A larger margin typically leads to better generalization. SVM can also handle non-linearly separable data through kernel functions such as the polynomial kernel or radial basis function (RBF), which map the data into a higher-dimensional feature space where separation becomes possible. This makes SVM robust, effective in high-dimensional spaces, and particularly strong in problems with limited training samples.""",

    "Question 3": """Bagging (Bootstrap Aggregating) is an ensemble learning technique that improves model stability and accuracy by reducing variance. It works by generating multiple bootstrap samples from the training dataset each sample is created by randomly selecting data points with replacement.
A separate model (usually a high-variance model like a decision tree) is trained on each subset.
During prediction, the outputs of all models are combined, typically through majority voting for classification or averaging for regression. This aggregation smoothens out fluctuations caused by individual models and significantly reduces overfitting."""
}


# Hardcoded marks
marks = {
    "Question 1": "2 / 3",
    "Question 2": "2 / 3",
    "Question 3": "4 / 4"
}

# Questions for teacher + student
questions_text = {
    "Question 1": "Explain the bias–variance tradeoff in machine learning. Why is it important for model generalization?",
    "Question 2": "What is a Support Vector Machine (SVM), and how does it classify data using hyperplanes and kernel functions?",
    "Question 3": "What is bagging in ensemble learning? Describe how it works and why it improves model performance."
}

# --------------------------
# Streamlit Tabs
# --------------------------
tab1, tab2 = st.tabs(["📘 Teacher Answer Key", "🧑‍🎓 Student Submission"])

# ------------------------------------------
# TAB 1 : TEACHER UPLOADS PDF + QUESTIONS
# ------------------------------------------
with tab1:
    st.markdown('<div class="header-font">Upload Teacher\'s Answer PDF (3 Questions)</div>', unsafe_allow_html=True)

    pdf_file = st.file_uploader("Upload the answer key PDF", type=["pdf"])

    if pdf_file:
        st.success("PDF uploaded successfully! Extracting answers...")
        time.sleep(2)  # 2-second delay for demo realism

        st.markdown('<div class="header-font">Extracted Answers</div>', unsafe_allow_html=True)
        st.markdown("---")

        for q, ans in teacher_answers.items():
            st.markdown(f'<div class="question-font">{q}: {questions_text[q]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="big-font">{ans}</div>', unsafe_allow_html=True)
            st.markdown("---")

# ------------------------------------------
# TAB 2 : STUDENT UPLOADS ANSWERS
# ------------------------------------------
with tab2:
    st.markdown('<div class="header-font">Submit Your Answers for this ML Assignment</div>', unsafe_allow_html=True)

    uploaded_images = {}

    # Loop through 3 questions
    for i, q in enumerate(teacher_answers.keys(), start=1):
        st.markdown(f'<div class="question-font">{q}: {questions_text[q]}</div>', unsafe_allow_html=True)

        img = st.file_uploader(
            f"Upload your handwritten answer for {q}",
            type=["png", "jpg", "jpeg"],
            key=f"q{i}"
        )

        if img:
            st.image(img, caption=f"Uploaded Answer for {q}", width=650)  # Bigger image
            uploaded_images[q] = img

        st.markdown("---")

    # After all uploads, calculate and show score
    if len(uploaded_images) == 3:
        st.success("All answers uploaded! Calculating score...")
        time.sleep(3)  # delay for realistic effect

        st.markdown('<div class="header-font">Scores for Each Question</div>', unsafe_allow_html=True)

        total_score = 0
        total_out_of = 0

        for q, m in marks.items():
            st.markdown(f'<div class="big-font"><b>{q}:</b> {m}</div>', unsafe_allow_html=True)
            a, b = map(int, m.split("/"))
            total_score += a
            total_out_of += b

        st.markdown("---")
        st.markdown(f'<div class="header-font">📊 Total Score: {total_score} / {total_out_of}</div>', unsafe_allow_html=True)

    else:
        st.info("Upload all 3 answers to view your final score.")
