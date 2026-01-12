# Schedule Data for 24-Week Plan

schedule = {
    1: {
        "week": 1,
        "phase": "Phase_01_Foundations",
        "topic": "Python for ML: Python Basics, NumPy, Pandas",
        "dir": "Phase_01_Foundations/Week_01_Python_for_ML",
        "readme": "Phase_01_Foundations/Week_01_Python_for_ML/README.md",
        "tasks": [
            "60 min: Learn Python basics, NumPy, Pandas",
            "90 min: Code small scripts (data cleaning, matrix ops)",
            "30 min: Write notes in README"
        ]
    },
    2: {
        "week": 1,
        "phase": "Phase_01_Foundations",
        "topic": "Python for ML: Advanced NumPy & Pandas",
        "dir": "Phase_01_Foundations/Week_01_Python_for_ML",
        "readme": "Phase_01_Foundations/Week_01_Python_for_ML/README.md",
        "tasks": [
            "60 min: Learn Vectorization and Broadcasting",
            "90 min: Build data processing pipeline",
            "30 min: Review"
        ]
    },
    # ... This structure implies we can map day 1-7 to Week 1, 8-14 to Week 2, etc.
    # For simplicity in this demo, we will calculate week/day dynamically in the main script
    # and use this map for Week-level specifics if Day-level granularity isn't fully defined textually yet.
}

def get_day_config(day_num):
    week_num = (day_num - 1) // 7 + 1
    
    # Map Week Number to Folders
    weeks_map = {
        1: ("Phase_01_Foundations", "Week_01_Python_for_ML"),
        2: ("Phase_01_Foundations", "Week_02_Math_ML_Intuition"),
        3: ("Phase_01_Foundations", "Week_03_Core_ML"),
        4: ("Phase_01_Foundations", "Week_04_ML_to_DL_Bridge"),
        5: ("Phase_02_Deep_Learning_Core", "Week_05_PyTorch"),
        6: ("Phase_02_Deep_Learning_Core", "Week_06_CNNs"),
        7: ("Phase_02_Deep_Learning_Core", "Week_07_RNN_LSTM"),
        8: ("Phase_02_Deep_Learning_Core", "Week_08_Model_Engineering"),
        9: ("Phase_03_Transformers_and_LLMs", "Week_09_Attention_and_Transformers"),
        10: ("Phase_03_Transformers_and_LLMs", "Week_10_HuggingFace"),
        11: ("Phase_03_Transformers_and_LLMs", "Week_11_LLM_Fine_Tuning"),
        12: ("Phase_03_Transformers_and_LLMs", "Week_12_13_Flagship_Project_1"),
        13: ("Phase_03_Transformers_and_LLMs", "Week_12_13_Flagship_Project_1"),
        14: ("Phase_04_Diffusion_Models", "Week_14_Generative_Models"),
        15: ("Phase_04_Diffusion_Models", "Week_15_Diffusion_Theory"),
        16: ("Phase_04_Diffusion_Models", "Week_16_17_Flagship_Project_2"),
        17: ("Phase_04_Diffusion_Models", "Week_16_17_Flagship_Project_2"),
        18: ("Phase_05_Production_and_AWS", "Week_18_Docker_and_APIs"),
        19: ("Phase_05_Production_and_AWS", "Week_19_AWS_Deep_Dive"),
        20: ("Phase_05_Production_and_AWS", "Week_20_CI_CD"),
        21: ("Phase_05_Production_and_AWS", "Week_21_Monitoring"),
        22: ("Phase_05_Production_and_AWS", "Week_22_System_Design"),
        23: ("Phase_06_Interview_and_Job_Prep", "Week_23_Mix_Prep"),
        24: ("Phase_06_Interview_and_Job_Prep", "Week_24_Career_Polish"),
    }
    
    if week_num in weeks_map:
        phase, week_dir_name = weeks_map[week_num]
        return {
            "week": week_num,
            "phase": phase,
            "dir_name": week_dir_name,
            "full_path": f"{phase}/{week_dir_name}",
            "readme": f"{phase}/{week_dir_name}/README.md"
        }
    else:
        return None
