import OutputGenerator as OG

def main():
    out = OG.OutputGenerator() # create the OG object
    out.GenerateHeader() #create header
    out.GenerateCosineValue() # add cosine value to each row
    out.PrintLines() # print lines
    
if __name__ == "__main__":
    main()