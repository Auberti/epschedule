import os

path = "C:/Users/guberti/Documents/Github/EPSchedule/schedules"

for fileName in os.listdir(path):
    if (fileName[-8:] == ".pdf.pdf"):
        os.rename(path + "/" + fileName, path + "/" + fileName[:-4])