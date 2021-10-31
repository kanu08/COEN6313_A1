from flask import Flask, render_template, request
import json
import pandas as pd
from random import seed
from random import randint

seed(1)
app = Flask(__name__)

@app.route("/reqData")
def req():
    RFWID = int(request.args.get("RFWID"))
    BenchMarkType = request.args.get("BenchMarkType")
    Metric = request.args.get("Metric")
    numOfSamples = int(request.args.get("numOfSamples"))
    batchStart = int(request.args.get("batchStart"))
    batchNum = int(request.args.get("batchNum"))
    DataSetKind = request.args.get("DataSetKind")

    temp_name = BenchMarkType+'-'+DataSetKind
    filename = "DataSet/{}.csv".format(temp_name)
    dataInFile = pd.read_csv(filename)

    ResultData = []
    for i in range(batchNum):
        fromRec = ((batchStart + i - 1) * numOfSamples)
        ToRec = (((batchStart + i) * numOfSamples))
        if ToRec >= len(dataInFile):
            ToRec = len(dataInFile)
            ResultData.append(((dataInFile[Metric][fromRec:ToRec]).values).tolist())
            lastbatch = batchStart + i
            break
        else:
            ResultData.append(((dataInFile[Metric][fromRec:ToRec]).values).tolist())
            lastbatch = batchStart + i
    return (json.dumps({'ID': RFWID, 'LastBatchID': lastbatch, 'DATA': ResultData}))


@app.route("/test_connection")
def test_connection():
    no = randint(0, 10000)
    return json.dumps({"randomNo": no})


if __name__ == "__main__":
    app.run()