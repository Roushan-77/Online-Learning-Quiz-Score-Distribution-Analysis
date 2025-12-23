# Online Learning Quiz Score Distribution Analysis

## Overview
This project presents a **statistical analysis** of student performance data collected from an online learning environment([Kaggle Dataset](https://www.kaggle.com/datasets/adilshamim8/student-performance-and-learning-style/data)). The primary objective is to study exam score distributions, evaluate performance variability, and interpret assessment difficulty using **descriptive statistics** and **exploratory data analysis techniques**(EDA). In addition to static analysis, an interactive dashboard has been developed using Gradio and deployed online for exploratory use.

> **Note**: The terms “quiz” and “exam” are used interchangeably in this project to represent online assessments, as the dataset provides score-based outcomes without specifying the assessment format.

### Interactive Demo
Gradio Dashboard (Live Demo): [Score Distribution dashboard](https://huggingface.co/spaces/roushan77/online-learning-score-analysis)

### Blog Post
Detailed Blog Explanation (Medium): [will bed added soon](https://github.com/Roushan-77/Online-Learning-Quiz-Score-Distribution-Analysis.git)

### Objectives
**The objectives of this project are**:
- To analyze exam score distributions using statistical measures
- To interpret assessment difficulty using mean, median, and standard deviation
- To explore relationships between exam scores and student-related factors
- To visualize insights using interpretable plots
- To provide an interactive interface for exploratory analysis

---

## Dataset Description
The dataset contains **14,003 students** learning behavior and performance attributes taken from [kaggle](https://www.kaggle.com/datasets/adilshamim8/student-performance-and-learning-style/data) including:

1. Study behaviors & engagement -> StudyHours, Attendance, Extracurricular, AssignmentCompletion, OnlineCourses, Discussions
2. Resources & environment -> Resources, Internet, EduTech
3. Motivation & psychology -> Motivation, StressLevel
4. Demographics -> Gender, Age (18–30 years)
5. Learning preference -> LearningStyle
6. Performance indicators -. ExamScore, FinalGrade

---

## Operation performed

### Data Preprocessing
1. Before analysis, the following preprocessing steps were performed:
2. Verified that the dataset contains no missing values
3. Identified and removed duplicate records to avoid statistical bias
4. Checked minimum and maximum values to ensure valid ranges
5. Optimized memory usage by downcasting numeric features to int8 where appropriate
6. Preserved the original dataset and created a separate cleaned dataset for analysis

### Feature Selection and Correlation Analysis
A subset of relevant academic, behavioral, and psychological features was selected for correlation analysis. Pearson correlation coefficients were computed to examine linear relationships with exam scores. The analysis showed that no individual feature exhibits a strong linear relationship with exam performance, indicating that academic outcomes are influenced by multiple interacting factors rather than a single dominant variable.

### Score Distribution and Difficulty Analysis
Descriptive statistics were computed for exam scores.
1. The mean and median were found to be nearly identical, indicating a near to symmetrical distribution.
2. The standard deviation reflects moderate variability in student performance.
3. The interquartile range shows that half of the students scored within a balanced range.

> **Based on these statistical indicators and visual analysis, the assessment is classified as moderately difficult.**

### Visual Analysis
The following **visualizations** were generated as part of the analysis:
1. Histogram of exam score distribution
2. Exam score distribution with mean and standard deviation markers
3. Boxplot of exam scores
4. Genderwise student distribution and average score comparison
5. Distribution of learning styles
6. Comparison of exam scores across different learning styles

### Exploratory Insights
1. Gender based analysis showed nearly equal participation and very similar average exam scores, suggesting no significant gender based performance difference.
2. Analysis across learning styles revealed overlapping score distributions, indicating that learning preference alone does not strongly determine exam performance.

### Interactive Dashboard
An interactive dashboard was developed using Gradio to allow users to upload the dataset, view descriptive statistics, and explore all visualizations dynamically. The dashboard serves as an extension of the static analysis.

---

## Tools and Technologies
1. Python
2. Pandas
3. NumPy
4. Matplotlib
5. Seaborn
6. Gradio
7. Jupyter Notebook

---

## Project structure

```json
online-learning-quiz-score-distribution-analysis/
│
├── images/
├── .gitignore
├── app.py
├── README.md
├── requirements.txt
├── student_performance.csv
└── student_performance.ipynb
```

---

## Conclusion
This project demonstrates how descriptive statistics and exploratory data analysis can be used to objectively evaluate assessment difficulty and student performance patterns in online learning environments.
> The exam was of **Moderate diffculty**

---

## Important commands

1. clone this repo
```json
git clone https://github.com/Roushan-77/Online-Learning-Quiz-Score-Distribution-Analysis.git
```