Purpose : Compare TMS Behavioral output

REQUIRES:
(*) Participant CSV raw data of each treatment session -> "CSVRaw_Data"
(*) Post survey data results file -> "post_survey_results - Sheet1.csv"
(*) Treatment to session number mapping (what region was stimulated when) -> "TMS Version to Treatment Mapping - Sheet1.csv"

SETUP
(*) "TMSAnalyze.py" Given such files and the list of problem numbers (seperated by types), python file generates either a CSV file
of all data trials by each participants combined OR CSV files for each participant of their data trials (or both) 

OUTPUT 
(*) "compiledData/" contains CSV data of each participant and a combined one called "TMSData.csv". "TMSData.csv" was the sheet used to conduct 
all the considered statistics in Jupyter Notebook