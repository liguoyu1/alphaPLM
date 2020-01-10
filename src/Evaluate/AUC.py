import sys
def calAUC(prob,labels):
    f = list(zip(prob,labels))
    rank = [values2 for values1,values2 in sorted(f,key=lambda x:x[0])]
    rankList = [i+1 for i in range(len(rank)) if rank[i]==1]
    posNum = 0
    negNum = 0
    for i in range(len(labels)):
        if(labels[i]==1):
            posNum+=1
        else:
            negNum+=1
    auc = 0
    auc = (sum(rankList)- (posNum*(posNum+1))/2)/(posNum*negNum)
    print(auc)
    return auc

def loadData(file):
    prob = []
    labels = []
    with open(file, "r") as fp:
        line = fp.readline()
        while line :
            item = line.split(" ")
            prob.append(float(item[1]))
            labels.append(int(item[0]))
            line = fp.readline()
    return prob, labels

def main():
    file = sys.argv[1]
    prob, labels = loadData(file)
    auc = calAUC(prob, labels)
    print("auc: "+str(auc))

if __name__ == '__main__':
    main()


