import requests
import json
from requests.models import PreparedRequest
import pprint

ListOfType = {1: "DVD", 2: "NDBench"}
ListOfMetric = {1: "CPUUtilization_Average", 2: "NetworkIn_Average", 3: "NetworkOut_Average",
                4: "MemoryUtilization_Average"}
ListOfDataKind = {1: "training", 2: "testing"}

pp = pprint.PrettyPrinter(indent=2)

##formation of request message
Name = input('Please enter your name: ')
url_t = 'http://15.223.122.199:5000/test_connection'
op = requests.get(url_t)
RFWID = op.json()['randomNo']
print("\nYour RFWID is {}".format(RFWID))
print("\nSelect the Benchmark Type from following:")
pp.pprint(ListOfType)
BenchMarkType = ListOfType[(int(input("Please enter the index of BenchMark Type: ")))]
print("\nSelect the Workload metric from following:")
pp.pprint(ListOfMetric)
Metric = ListOfMetric[(int(input("Please enter the index of Workload Metric: ")))]
numOfSamples = int(input("\nPlease enter the number of samples in one batch: "))
BatchesStart = int(input("Please enter the batch ID: "))
BatchNum = int(input("Please enter number of batches: "))
print("\nSelect the DataSet Type from following:")
pp.pprint(ListOfDataKind)
DataSetKind = ListOfDataKind[(int(input("Please enter the index of DataSet Type: ")))]

###URL formation for fetching the Data
API = "reqData"
url = 'http://15.223.122.199:5000/{}?'.format(API)
params = {'RFWID': RFWID, 'BenchMarkType': BenchMarkType, 'Metric': Metric, 'numOfSamples': numOfSamples,
          'batchStart': BatchesStart, 'batchNum': BatchNum, 'DataSetKind': DataSetKind}
requestForData = PreparedRequest()
requestForData.prepare_url(url, params)
rep = requests.get(requestForData.url)
if rep.status_code == 200:
    print("\n")
    pp.pprint(rep.json())
    print("\nData:\n", rep.json()['DATA'])
    print("\nRFWID:\n", rep.json()['ID'])
    print("\nLastBatchID:\n", rep.json()['LastBatchID'])
    with open('data.json', 'w') as outfile:
        json.dump(rep.json(), outfile)
else:
    print("Unfortunately, Request couldn't be completed. Please try again.")
