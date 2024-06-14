from loadData import loadData
import numpy as np
from sklearn.preprocessing import LabelEncoder


def preprocessing(dataFrame):
    
    #Drop None Used Columns
    dataFrame = dataFrame.drop(columns=['id', 'pathrise_status','cohort_tag'])
    

    #Prepare And Cleaning Primary Track Data
    dataFrame = dataFrame.dropna(subset=["primary_track"])
    dataFrame["primary_track"] = dataFrame["primary_track"].replace("Marketing", np.nan)
    dataFrame = dataFrame.dropna(subset=["primary_track"])
    
    #Prepare And Cleaning Program Duration Days Data
    dataFrame["program_duration_days"] = dataFrame["program_duration_days"].replace(np.nan, 0)
    dataFrame["program_duration_days"] = np.where(dataFrame["program_duration_days"] > 380, np.nan, dataFrame["program_duration_days"])
    dataFrame = dataFrame.dropna(subset=["program_duration_days"])

    #Prepare And Cleaning Employment Status Data
    dataFrame = dataFrame.dropna(subset=["employment_status"])

    #Prepare And Cleaning Highest Level Of Education Data
    dataFrame = dataFrame.dropna(subset=["highest_level_of_education"])
    dataFrame["highest_level_of_education"] = dataFrame["highest_level_of_education"].replace("Some High School", np.nan)
    dataFrame = dataFrame.dropna(subset=["highest_level_of_education"])

    #Prepare And Cleaning Length Of Job Search Data
    dataFrame = dataFrame.dropna(subset=["length_of_job_search"])

    #Prepare And Cleaning Biggest Challenge In Search Data
    dataFrame = dataFrame.dropna(subset=["biggest_challenge_in_search"])

    #Prepare And Cleaning Professional Experience Data
    dataFrame = dataFrame.dropna(subset=["professional_experience"])

    #Prepare And Cleaning Number Of Interviews Data
    dataFrame["number_of_interviews"] = dataFrame["number_of_interviews"].replace(np.nan, dataFrame["number_of_interviews"].mean())
    dataFrame["number_of_interviews"] = np.where(dataFrame["number_of_interviews"] > 10, np.nan, dataFrame["number_of_interviews"])
    dataFrame = dataFrame.dropna(subset=["number_of_interviews"])

    #Prepare And Cleaning Number Of Applications Data
    dataFrame["number_of_applications"] = dataFrame["number_of_applications"].replace(np.nan, dataFrame["number_of_applications"].mean())
    dataFrame["number_of_applications"] = np.where(dataFrame["number_of_applications"] > 250, np.nan, dataFrame["number_of_applications"])
    dataFrame = dataFrame.dropna(subset=["number_of_applications"])

    #Prepare And Cleaning Gender Data
    dataFrame = dataFrame.dropna(subset=["gender"])
    dataFrame["gender"] = dataFrame["gender"].replace("Non-Binary", np.nan)
    dataFrame["gender"] = dataFrame["gender"].replace("Decline to Self Identify", np.nan)
    dataFrame = dataFrame.dropna(subset=["gender"])
    
    #Prepare And Cleaning Work Authorizations Status Data
    dataFrame["work_authorization_status"] = dataFrame["work_authorization_status"].replace("STEM OPT", np.nan)
    dataFrame["work_authorization_status"] = dataFrame["work_authorization_status"].replace("Not Authorized", np.nan)
    dataFrame = dataFrame.dropna(subset=["work_authorization_status"])
    
    #Prepare And Cleaning Race Data
    dataFrame = dataFrame.dropna(subset=["race"])
    dataFrame["race"] = dataFrame["race"].replace("Native American or Alaskan Native", np.nan)
    dataFrame["race"] = dataFrame["race"].replace("Decline to Self Identify", np.nan)
    dataFrame = dataFrame.dropna(subset=["race"])



    #Prepare Lable Encoder And Convert Objects To Numbers
    labelEncoders = {}
    for column in dataFrame.select_dtypes(include=['object']).columns:
        labelEncoders[column] = LabelEncoder()
        dataFrame[column] = labelEncoders[column].fit_transform(dataFrame[column])


    return dataFrame


