#This  module  is  the  csv  downloader which 
#contains a function csv_reader that download
#the csv file from a given  url  address  and
#return a 2-D list (each object is a list 
#contains words in the corresponding row in 
#the original csv file) 
# e.g. [["row1","a"],["row2","b"]]

import      csv
import requests




def CsvDownloader(CsvUrl:str)->[["station_id", "angle_degrees"],
                                ["0", "90"]]:
    try:
        with requests.Session() as s: 
            # use try&except when downloading from the internet
            try:
                download = s.get(CsvUrl) #open a request session
            except:
                # print error information
                print("Error: Fail to download the information")
            #decode the content using utf-8
            decode_content = download.content.decode("utf-8") 
            #read the content by built in csv reader (read by lines)
            content = csv.reader(decode_content.splitlines()) 
            #create a list containing the content and return it 
            return list(content) 
    except:
        print("Error: CsvDownloader()")
        # if errors happen in this function,
        # return an empty list 
        return []


