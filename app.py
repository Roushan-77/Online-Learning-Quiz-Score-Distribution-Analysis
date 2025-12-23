import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_student_data(file):
    df = pd.read_csv(file.name)

    # Clean data
    df = df.drop_duplicates()

    
    stats_df = (
    df["ExamScore"]
    .describe()
    .round(2)
    .reset_index()
    .rename(columns={"index": "Statistic", "ExamScore": "Value"})
        )

    plt.figure(figsize=(7, 4))
    sns.histplot(df["ExamScore"], bins=15, kde=True)
    plt.title("Distribution of Exam Scores")
    plt.xlabel("Exam Score")
    plt.ylabel("Number of Students")
    fig_hist = plt.gcf()
    plt.close()


    mean = df["ExamScore"].mean()
    std = df["ExamScore"].std()

    plt.figure(figsize=(7, 4))
    sns.histplot(df["ExamScore"], bins=15)
    plt.axvline(mean, color="red", linestyle="--", label="Mean")
    plt.axvline(mean + std, color="green", linestyle="--", label="+1 Std Dev")
    plt.axvline(mean - std, color="green", linestyle="--", label="-1 Std Dev")
    plt.legend()
    plt.title("Exam Score Distribution with Mean & Std")
    fig_mean_std = plt.gcf()
    plt.close()

    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df["ExamScore"], color="skyblue")
    plt.title("Boxplot of Exam Scores")
    fig_box = plt.gcf()
    plt.close()

    gender_counts = df["Gender"].value_counts()

    plt.figure(figsize=(5, 5))
    plt.pie(
        gender_counts,
        labels=["Female", "Male"],
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Gender Distribution")
    fig_gender_pie = plt.gcf()
    plt.close()

    gender_mean = df.groupby("Gender")["ExamScore"].mean()

    plt.figure(figsize=(6, 4))
    gender_mean.plot(kind="bar")
    plt.xticks([0, 1], ["Female", "Male"], rotation=0)
    plt.ylabel("Average Exam Score")
    plt.title("Average Exam Score by Gender")
    fig_gender_bar = plt.gcf()
    plt.close()

    ls_counts = df["LearningStyle"].value_counts().sort_index()

    plt.figure(figsize=(6, 4))
    ls_counts.plot(kind="bar")
    plt.xticks(
        ticks=[0, 1, 2, 3],
        labels=["Visual", "Auditory", "Reading/Writing", "Kinesthetic"],
        rotation=30
    )
    plt.ylabel("Number of Students")
    plt.title("Learning Style Distribution")
    fig_ls_dist = plt.gcf()
    plt.close()

    plt.figure(figsize=(7, 4))
    sns.boxplot(x=df["LearningStyle"], y=df["ExamScore"])
    plt.xticks(
        ticks=[0, 1, 2, 3],
        labels=["Visual", "Auditory", "Reading/Writing", "Kinesthetic"],
        rotation=20
    )
    plt.xlabel("Learning Style")
    plt.ylabel("Exam Score")
    plt.title("Exam Score by Learning Style")
    fig_ls_score = plt.gcf()
    plt.close()

    return (
        stats_df,
        fig_hist,
        fig_mean_std,
        fig_box,
        fig_gender_pie,
        fig_gender_bar,
        fig_ls_dist,
        fig_ls_score
    )

interface = gr.Interface(
    fn=analyze_student_data,
    inputs=gr.File(label="Upload Student Performance CSV"),
    outputs=[
        gr.Dataframe(label="Exam Score Statistics"),
        gr.Plot(label="Exam Score Distribution"),
        gr.Plot(label="Distribution with Mean & Std"),
        gr.Plot(label="Exam Score Boxplot"),
        gr.Plot(label="Gender Distribution"),
        gr.Plot(label="Average Exam Score by Gender"),
        gr.Plot(label="Learning Style Distribution"),
        gr.Plot(label="Exam Score by Learning Style"),
    ],
    title="Online Learning Quiz Score Distribution Analysis",
    description="Interactive statistical analysis of online assessment performance using descriptive statistics and visualizations."
)

interface.launch()