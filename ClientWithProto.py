import socket
import sys
import random
from datetime import datetime
import pprint
import Data_pb2

random.seed(datetime.now())

# Creating a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting the socket to the port where the server is listening
server_address = ('15.223.122.199', 5000)
print(sys.stderr, 'connecting to port', server_address)
sock.connect(server_address)



ListOfType = {1: "DVD", 2: "NDBench"}
ListOfMetric = {1: "CPUUtilization_Average", 2: "NetworkIn_Average", 3: "NetworkOut_Average", 4: "MemoryUtilization_Average",
       5: "Final_Target"}
ListOfDataKind = {1: "training", 2: "testing"}
pp = pprint.PrettyPrinter(indent=2)

##formation of request message
Name = input("Please enter your name: ")
RFWID = random.randint(0, 100)
print("\nYour RFWID is {}".format(RFWID))
print("\nSelect the Benchmark Type from following:")
pp.pprint(ListOfType)
BenchMarkType_Name = ListOfType[(int(input("Please enter the index of BenchMark Type: ")))]
print("\nSelect the Workload metric from following:")
pp.pprint(ListOfMetric)
Metric = ListOfMetric[(int(input("Please enter the index of Workload Metric: ")))]
numOfSamples = int(input("\nPlease enter the number of samples in one batch: "))
BatchesStart = int(input("Please enter the batch ID: "))
BatchNum = int(input("Please enter number of batches: "))
print("\nSelect the DataSet Type from following:")
pp.pprint(ListOfDataKind)
DataSetKind = ListOfDataKind[(int(input("Please enter the index of DataSet Type: ")))]

requestForData = Data_pb2.Request()
responseForData = Data_pb2.Data()

requestForData.RFWID = RFWID
requestForData.BenchMarkType = BenchMarkType_Name+'-'+DataSetKind
requestForData.Metric = Metric
requestForData.numOfSamples = numOfSamples
requestForData.BatchesStart = BatchesStart
requestForData.BatchNum = BatchNum

SerializedRequest = requestForData.SerializePartialToString()

try:
    # Send data
    print(sys.stderr, 'sending ')
    sock.sendall(SerializedRequest)
    # Look for the response
    amount_received = 0
    amount_expected = 41

    while amount_received < amount_expected:
        data = sock.recv(4096)
        responseForData.FromString(data)
        print(responseForData)
        break

    amount_received += len(data)
    print(sys.stderr, 'received ', data)

finally:
    print(sys.stderr, 'closing socket')
    sock.close()
    f = open('Proto_DataLog', "wb")
    f.write(data)
    f.close()
Data = responseForData.FromString(data)
print('\nData Received\n', Data)