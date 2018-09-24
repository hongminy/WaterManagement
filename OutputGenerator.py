# this module functions to create the proper
# output using the data return from CsvDownloader()



from CsvReader import CsvDownloader
from math import cos

class OutputGenerator:
    # use the url given as the default parameter
    def __init__(self, 
                 DataURL = "http://rapid-hub.org/data/angles_UCI_CS.csv"):
        
        # set header and lines to empty
        self.Header = ""
        self.Lines = []
        # use CsvDownloader to download the information to a list
        self.ContentList = CsvDownloader(DataURL)
        
    def GenerateHeader(self):
        # this function adds one more column to the header
        self.ContentList[0].append(" cosine_values")
    
    def GenerateCosineValue(self):
        #this function adds the cosine value to each line
        for Row in range(1,len(self.ContentList)):
            Angle = float(self.ContentList[Row][1])
            self.ContentList[Row].append(str("%.3f" %cos(Angle))) # cast the float by 3 decimal
                                                                  # convert the value to string
                                                                  # add to the row
        
    def PrintLines(self):
        for Row in range(len(self.ContentList)): # two for loops to iterate through
                                                 # each columns in every row
            for Column in range(len(self.ContentList[Row])):
                # print each element in the list (align to the right)
                print("{:>14} ".format(self.ContentList[Row][Column].strip()), end = "")
            print() # print a newline

    
        