import streamlit as st
import pandas as pd

# ---------- Load Data ----------
@st.cache_data
def load_data(file):
    """
    Load data from Excel file with caching.
    
    Args:
        file: Uploaded file or file path
    
    Returns:
        Tuple of dataframes (issues, skills, worklogs, leaves)
    """
    if file is not None:
        try:
            xls = pd.ExcelFile(file)
            issues = xls.parse("Issues")
            skills = xls.parse("Skills")
            worklogs = xls.parse("Worklogs")
            leaves = xls.parse("Non_Availability")
            
            # Ensure datetime parsing
            for df in [issues]:
                if 'Start Date' in df.columns:
                    df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
                if 'Due Date' in df.columns:
                    df['Due Date'] = pd.to_datetime(df['Due Date'], errors='coerce')
            
            if 'Date' in worklogs.columns:
                worklogs['Date'] = pd.to_datetime(worklogs['Date'], errors='coerce')
            
            if 'Start Date' in leaves.columns:
                leaves['Start Date'] = pd.to_datetime(leaves['Start Date'], errors='coerce')
            if 'End Date' in leaves.columns:
                leaves['End Date'] = pd.to_datetime(leaves['End Date'], errors='coerce')
                
            return issues, skills, worklogs, leaves
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return None, None, None, None
    return None, None, None, None
