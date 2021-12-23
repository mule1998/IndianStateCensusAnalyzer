import panda as pd

def census():
    csv=pd.read_csv('C:/Users/Shubham/Desktop/IndianCensusAnalyzer/IndianCensus - Sheet1')
    print(csv)

data=census()
print(data)
