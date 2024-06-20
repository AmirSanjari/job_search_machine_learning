from loadData import loadData
import numpy as np
from sklearn.preprocessing import LabelEncoder


def preprocessing(dataFrame):
    """
    Preprocesses the given DataFrame by performing various data cleaning and preparation steps.

    Parameters:
    -----------
    dataFrame : pandas.DataFrame
        Input DataFrame containing the data to be preprocessed.

    Returns:
    --------
    pandas.DataFrame
        Preprocessed DataFrame with cleaned and transformed data.

    Steps:
    ------
    1. Drop unnecessary columns: 'id', 'pathrise_status', 'cohort_tag'.
    2. Clean 'primary_track' data: Replace 'Marketing' with NaN and drop corresponding rows.
    3. Clean 'program_duration_days' data: Replace NaN with 0, filter out values > 380, drop NaNs.
    4. Clean 'employment_status' data: Drop rows with missing values.
    5. Clean 'highest_level_of_education' data: Drop rows with missing values, replace 'Some High School' with NaN.
    6. Clean 'length_of_job_search' data: Drop rows with missing values.
    7. Clean 'biggest_challenge_in_search' data: Drop rows with missing values.
    8. Clean 'professional_experience' data: Drop rows with missing values.
    9. Clean 'number_of_interviews' data: Replace NaN with mean, filter out values > 10, drop NaNs.
    10. Clean 'number_of_applications' data: Replace NaN with mean, filter out values > 250, drop NaNs.
    11. Clean 'gender' data: Drop rows with missing values, replace 'Non-Binary' and 'Decline to Self Identify' with NaN.
    12. Clean 'work_authorization_status' data: Replace 'STEM OPT' and 'Not Authorized' with NaN, drop corresponding rows.
    13. Clean 'race' data: Drop rows with missing values, replace 'Native American or Alaskan Native' and 'Decline to Self Identify' with NaN.
    14. Encode categorical columns using LabelEncoder.

    """
    # Drop unnecessary columns
    dataFrame = dataFrame.drop(columns=['id', 'pathrise_status', 'cohort_tag'])

    # Clean 'primary_track' data
    dataFrame = dataFrame.dropna(subset=["primary_track"])
    dataFrame["primary_track"] = dataFrame["primary_track"].replace("Marketing", np.nan)
    dataFrame = dataFrame.dropna(subset=["primary_track"])

    # Clean 'program_duration_days' data
    dataFrame["program_duration_days"] = dataFrame["program_duration_days"].replace(np.nan, 0)
    dataFrame["program_duration_days"] = np.where(dataFrame["program_duration_days"] > 380, np.nan, dataFrame["program_duration_days"])
    dataFrame = dataFrame.dropna(subset=["program_duration_days"])

    # Clean 'employment_status' data
    dataFrame = dataFrame.dropna(subset=["employment_status"])

    # Clean 'highest_level_of_education' data
    dataFrame = dataFrame.dropna(subset=["highest_level_of_education"])
    dataFrame["highest_level_of_education"] = dataFrame["highest_level_of_education"].replace("Some High School", np.nan)
    dataFrame = dataFrame.dropna(subset=["highest_level_of_education"])

    # Clean 'length_of_job_search' data
    dataFrame = dataFrame.dropna(subset=["length_of_job_search"])

    # Clean 'biggest_challenge_in_search' data
    dataFrame = dataFrame.dropna(subset=["biggest_challenge_in_search"])

    # Clean 'professional_experience' data
    dataFrame = dataFrame.dropna(subset=["professional_experience"])

    # Clean 'number_of_interviews' data
    dataFrame["number_of_interviews"] = dataFrame["number_of_interviews"].replace(np.nan, dataFrame["number_of_interviews"].mean())
    dataFrame["number_of_interviews"] = np.where(dataFrame["number_of_interviews"] > 10, np.nan, dataFrame["number_of_interviews"])
    dataFrame = dataFrame.dropna(subset=["number_of_interviews"])

    # Clean 'number_of_applications' data
    dataFrame["number_of_applications"] = dataFrame["number_of_applications"].replace(np.nan, dataFrame["number_of_applications"].mean())
    dataFrame["number_of_applications"] = np.where(dataFrame["number_of_applications"] > 250, np.nan, dataFrame["number_of_applications"])
    dataFrame = dataFrame.dropna(subset=["number_of_applications"])

    # Clean 'gender' data
    dataFrame = dataFrame.dropna(subset=["gender"])
    dataFrame["gender"] = dataFrame["gender"].replace("Non-Binary", np.nan)
    dataFrame["gender"] = dataFrame["gender"].replace("Decline to Self Identify", np.nan)
    dataFrame = dataFrame.dropna(subset=["gender"])

    # Clean 'work_authorization_status' data
    dataFrame["work_authorization_status"] = dataFrame["work_authorization_status"].replace("STEM OPT", np.nan)
    dataFrame["work_authorization_status"] = dataFrame["work_authorization_status"].replace("Not Authorized", np.nan)
    dataFrame = dataFrame.dropna(subset=["work_authorization_status"])

    # Clean 'race' data
    dataFrame = dataFrame.dropna(subset=["race"])
    dataFrame["race"] = dataFrame["race"].replace("Native American or Alaskan Native", np.nan)
    dataFrame["race"] = dataFrame["race"].replace("Decline to Self Identify", np.nan)
    dataFrame = dataFrame.dropna(subset=["race"])

    # Label encode categorical columns
    labelEncoders = {}
    for column in dataFrame.select_dtypes(include=['object']).columns:
        labelEncoders[column] = LabelEncoder()
        dataFrame[column] = labelEncoders[column].fit_transform(dataFrame[column])

    return dataFrame
