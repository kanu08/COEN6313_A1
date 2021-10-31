import socket
import sys
import Data_pb2
import pandas as pd

# Creating a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
print(sys.stderr, 'starting up on', server_address)
sock.bind(server_address)
sock.listen(1)



while True:
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print(sys.stderr, 'connection from', client_address)
        # Following connection will receive the data from client as it arrives
        while True:
            data = connection.recv(4096)
            print(sys.stderr, 'Received ', data)
            if data:
                r = Data_pb2.Request().FromString(data)
                RFWID = r.RFWID
                BenchMarkType = r.BenchMarkType
                Metric = r.Metric
                numOfSamples = r.numOfSamples
                BatchesStart = r.BatchesStart
                BatchNum = r.BatchNum

                filename = "https://raw.githubusercontent.com/haniehalipour/Online-Machine-Learning-for-Cloud-Resource-Provisioning-of-Microservice-Backend-Systems/master/Workload%20Data/{}.csv".format(BenchMarkType)
                dataInFile = pd.read_csv(filename)

                d = Data_pb2.Data()
                d.RFWID = RFWID

                fromRec = ((BatchesStart - 1) * numOfSamples)
                toRec = ((BatchesStart + BatchNum - 1) * numOfSamples)
                if toRec >= len(dataInFile):
                    toRec = len(dataInFile)
                d.LastBatchN = ((toRec - fromRec) // numOfSamples) + BatchesStart - 1
                for i in dataInFile[Metric][fromRec:toRec].values:
                    d.data.append(i)

                data = d.SerializeToString()
                connection.sendall(data)

            else:
                print(sys.stderr, 'All requests served, waiting for new data from', client_address)
                break

    finally:
        connection.close()
        # close the connection
