""" 
sampleDict = {
"name":"Kelly",
"age":25,
"salary":8000
"city":New york"
}
{
  "name":"Kelly",
"age":25,
"salary":8000
"locoation":New york"  
}
"city" keyni "location" ga o'zgartirib qo'ying
"""
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

sampleDict["location"] = sampleDict.pop("city")

print(sampleDict)
