import csv
import os


### CODING TASKS -> PROBLEM NUMBERS ###
ARRAYS = [327, 328, 329, 330, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 
            23, 24, 25, 27, 29, 201, 202, 203, 204, 205, 206, 207]
TREES = [301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 317, 318, 319, 320, 
             321, 322, 323, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 51, 52, 
             53, 54, 55, 56, 57, 59, 60, 208, 209, 210, 211, 212, 213, 214]
MENTAL = [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 84, 85, 86, 87, 
              88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 
              109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]

#91 - 120 PSVT

CODING = [315, 316, 324, 325, 326, 331, 332, 333, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 
              131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]

def getTypeProblem(problemName: str) -> str:
    problemName = int(problemName.split(".")[0])
    if problemName in ARRAYS:
        return "ARRAY"
    elif problemName in TREES:
        return "TREE"
    elif problemName in MENTAL:
        return "MENTAL"
    elif problemName in CODING:
        return "CODING"
    

def extractIDs(csvFiles: list) -> list:
    pIDs = []
    for file in csvFiles:
        pID = file.split("_")[0]
        if pID not in pIDs and pID != '.DS':
            pIDs.append(pID)
    
    return pIDs

def extractTreatments(treatmentMappingFile: str)-> dict[dict]: #{'00001': {'version1': 'vertex', 'version2': 'm1', 'version3': 'sma'}
    file = open(treatmentMappingFile, "r")
    csv_reader = csv.reader(file, delimiter=',')

    dict_treat = {}

    #EXTRACT INFO ON TREAMTMENTS ON VERSIONS 
    for count, row in enumerate(csv_reader):
        if count > 0:
            id = row[0]
            dict_treat[id] = dict()
            for i in range(1, len(row)):
                try:
                    treatment, version = row[i].split(",")
                    tmp = version.split(" ")
                    version = tmp[1] + tmp[2]
                    dict_treat[id][version] = treatment
                except:
                    pass
                    #print("ID missing treatments")
    #print(dict_treat)
    file.close()

    return dict_treat



def extractSurvey(surveyFile: str, participantIDs: list) -> dict():
    file = open(surveyFile, "r")
    csv_reader = csv.reader(file, delimiter=',')

    dict_survey = {}
    for count, row in enumerate(csv_reader):
        ID = row[0]
        if count > 0 and ID in participantIDs: #3
            tmp = {}
            treatment = row[1]
            sessionNo = row[2]
            mrDifficulty = row[4]
            changeMrDifficulty = row[6]
            programDifficulty = row[5]
            changeProgramDifficulty = row[7]

            #tmp[treatment] = [sessionNo, mrDifficulty, changeMrDifficulty, programDifficulty, changeMrDifficulty]
            dict_survey[(ID, treatment)] = [sessionNo, mrDifficulty, changeMrDifficulty, programDifficulty, changeMrDifficulty]

    
    print(dict_survey)
    file.close()
    return dict_survey


def extractDemographics(demographicsFile: str, participantIDs: list) -> dict:
    file = open(demographicsFile, "r")
    csv_reader = csv.reader(file, delimiter=',')

    dict_demo = {}
    for count, row in enumerate(csv_reader):
        ID = row[19]
        if count > 3 and ID in participantIDs: #3
            age = int(row[20])
            gender = row[23]
            race = row[26]
            if len(row[27].split(',')) > 1:
                occupation = row[27].split(",")[0]
            else:
                occupation = row[27]
            yearsProgramming = int(row[29])
            programmingLanguages = len(row[30].split(","))
            dict_demo[ID] = [age, gender, race, occupation, yearsProgramming, programmingLanguages]

    
    dict_demo["00001"]=['', 'Female', 'Asian', 'Computing Student (graduate)', '', '']
    #print(dict_demo)
    file.close()

    return dict_demo


def collectParticipantFiles(csvFiles: list[str], pID: str, dataLocation: str) -> list:
    participantFiles = []
    for file in csvFiles:
        if pID in file:
            participantFiles.append(dataLocation+file)

    return participantFiles



def extractData(pID: str, participantFiles:list):
    allData = []
    for file in participantFiles:
        findVersion = file.split("_")
        version = findVersion[3]
        data = open(file, "r")
        csv_reader = csv.reader(data, delimiter=',')
        for line in csv_reader:
            try:
                if "bmp" in line[0].lower() or "jpg" in line[0].lower():
                    tmp = []
                    tmp.append(pID)
                    tmp.append(version)
                    tmp.append(int(float(line[10]))+1)
                    tmp.append(line[0])
                    tmp.append(line[7])
                    if ("140" in line[0] or "106" in line[0] or "118" in line[0] or "332" in line[0]): #HANDLES THE WRONG ANSWERS (RESEARCHER ERROR)
                        if (line[6].split("\'")[1] == 'b'):
                            tmp.append("1")
                            #print(tmp)
                        else:
                            tmp.append("0")
                            #print(tmp)
                    
                    else:
                        tmp.append(line[4])

                    allData.append(tmp)
            except:
                #print(pID, " question NaN or not a valid CSV line")
                pass
    
    return allData
                

def CSVOutput(compiledData: list, demoData: dict, surveyData: dict, outputLocation: str, treatmentIDMapping, blindAnalysis):
    with open(outputLocation+"TMSdata.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "treatment", "version", "problemNumber", "problem","problemType", "responseTime", "accuracy", 
                         "sessionNo", "mrDifficulty", "changeMrDifficulty","programDifficulty" , "changeProgramDifficulty", 
                         "age", "gender", "race", "occupation", "yearsProgramming", "numPL"])
        for participantData in compiledData:
            for data in participantData:
                pID = data[0]
                treatment = treatmentIDMapping[data[0]][data[1]]
                if (pID,treatment) in surveyData and pID in demoData:
                    writer.writerow(["p" +str(pID), blindAnalysis[treatment], data[1], data[2], data[3],getTypeProblem(data[3]), data[4], int(float(data[5])),
                                 surveyData[(pID,treatment)][0], surveyData[(pID,treatment)][1], surveyData[(pID,treatment)][2], surveyData[(pID,treatment)][3], surveyData[(pID,treatment)][4],
                                 demoData[pID][0], demoData[pID][1], demoData[pID][2], demoData[pID][3], demoData[pID][4], demoData[pID][5]])
                elif (pID,treatment) in surveyData:
                    writer.writerow(["p" +str(pID), blindAnalysis[treatment], data[1], data[2], data[3],getTypeProblem(data[3]), data[4], int(float(data[5])),
                                 surveyData[(pID,treatment)][0], surveyData[(pID,treatment)][1], surveyData[(pID,treatment)][2], surveyData[(pID,treatment)][3], surveyData[(pID,treatment)][4]])
                elif pID in demoData:
                    writer.writerow(["p"+str(pID), blindAnalysis[treatment], data[1], data[2], data[3],getTypeProblem(data[3]), data[4], int(float(data[5])), 
                                     '', '', '', '', '',
                                     demoData[pID][0], demoData[pID][1], demoData[pID][2], demoData[pID][3], demoData[pID][4], demoData[pID][5]])
                else:
                    writer.writerow(["p"+str(pID), blindAnalysis[treatment], data[1], data[2], data[3],getTypeProblem(data[3]), data[4], int(float(data[5]))])
    

def CSVOutputPerParticipant(compiledData: list, outputLocation: str, treatmentIDMapping, blindAnalysis):
        for participantData in compiledData:
            with open(outputLocation+participantData[0][0]+"_data.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "treatment", "version", "problemNumber", "problem","problemType", "responseTime", "accuracy"])
                for data in participantData:
                    writer.writerow([data[0], blindAnalysis[treatmentIDMapping[data[0]][data[1]]], data[1], data[2], data[3],getTypeProblem(data[3]), data[4], data[5]])







'''
def test():
    MAPPINGFILE = "TMS Version to Treatment Mapping - Sheet1.csv"
    DEMOGRAPHICSFILE = "fMRIDemographics.csv"
    DATALOCATION = "CSVRaw_Data/"
    OUTPUTLOCATION = "compiledData/"
    CSV_FILES = os.listdir("CSVRaw_Data")
    BLINDANALYSIS = {"m1": "A", "sma": "B", "vertex": "C"}
    

    treatmentIDMapping = extractTreatments(MAPPINGFILE)
    participantsIDs = extractIDs(CSV_FILES)
    dict_demographics = extractDemographics(DEMOGRAPHICSFILE, participantsIDs)

    compiledData = []
    for participant in participantsIDs:
        participantFiles = collectParticipantFiles(CSV_FILES, participant, DATALOCATION )
        data = extractData(participant, participantFiles)
        compiledData.append(data)

    for participantData in compiledData:
        for data in participantData:
            print(data[0], BLINDANALYSIS[treatmentIDMapping[data[0]][data[1]]], data[1], data[2], data[3],getTypeProblem(data[3]), data[4], data[5])
            '''



def main():
    MAPPINGFILE = "TMS Version to Treatment Mapping - Sheet1.csv"
    DEMOGRAPHICSFILE = "fMRIDemographics.csv"
    SURVEY = "post_survey_results - Sheet1.csv"
    DATALOCATION = "CSVRaw_Data/"
    OUTPUTLOCATION = "compiledData/"
    CSV_FILES = os.listdir("CSVRaw_Data")
    BLINDANALYSIS = {"m1": "A", "sma": "B", "vertex": "C"}
    

    treatmentIDMapping = extractTreatments(MAPPINGFILE)
    participantsIDs = extractIDs(CSV_FILES)
    dict_demographics = extractDemographics(DEMOGRAPHICSFILE, participantsIDs)
    dict_surveys = extractSurvey(SURVEY, participantsIDs)
    print(participantsIDs)


    compiledData = []
    for participant in participantsIDs:
        participantFiles = collectParticipantFiles(CSV_FILES, participant, DATALOCATION )
        data = extractData(participant, participantFiles)
        compiledData.append(data)
        

    print("in here")
    CSVOutput(compiledData, dict_demographics, dict_surveys, OUTPUTLOCATION, treatmentIDMapping, BLINDANALYSIS)
    #CSVOutputPerParticipant(compiledData, OUTPUTLOCATION, treatmentIDMapping, BLINDANALYSIS)
    
    
     
main()


