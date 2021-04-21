import csv 
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

file  = pd.read_csv('medium_data.csv')
filedata = file['reading_time'].tolist()
mean =  statistics.mean(filedata)
std  = statistics.stdev(filedata)
print(mean)
print(std)

def randomSample(counter):
    sampledata = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(filedata)-1)
        value = filedata[randomindex]
        sampledata.append(value)
    mean = statistics.mean(sampledata)
    return(mean)
meanlist = []

for i in range(0,1000):
    setofmean = randomSample(100)
    meanlist.append(setofmean)

stdsample = statistics.stdev(meanlist)
meansample = statistics.mean(meanlist)
print('std of sample distribution:', stdsample)
print('mean of sample dirstribution:', meansample)
plot = ff.create_distplot([meanlist],['Math_score'],show_hist=False)
plot.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20],mode = 'lines'))
#plot.show()
standardDevaition = statistics.stdev(meanlist)

firstStdStart, firstStdEnd = mean - standardDevaition, mean + standardDevaition
secondStdStart, secondStdEnd = mean - (2*standardDevaition), mean + (2*standardDevaition)
thirdStdStart, thirdStdEnd = mean - (3*standardDevaition), mean + (3*standardDevaition)

FSD = [result for result in meanlist if result > firstStdStart and result < firstStdEnd]
print("{}%" .format(len(FSD)*100/len(meanlist)))

SSD = [result for result in meanlist if result > secondStdStart and result < secondStdEnd]
print("{}%" .format(len(SSD)*100/len(meanlist)))

TSD = [result for result in meanlist if result > thirdStdStart and result < thirdStdEnd]
print("{}%" .format(len(TSD)*100/len(meanlist)))

plot = ff.create_distplot([meanlist],['Math_score'],show_hist=False)
plot.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20],mode = 'lines'))
plot.add_trace(go.Scatter(x = [firstStdStart,firstStdStart], y = [0,0.20],mode = 'lines'))
plot.add_trace(go.Scatter(x = [secondStdStart,secondStdStart], y = [0,0.20],mode = 'lines'))
plot.add_trace(go.Scatter(x = [thirdStdStart, thirdStdStart], y = [0,0.20],mode = 'lines'))
plot.add_trace(go.Scatter(x = [firstStdEnd,firstStdEnd], y = [0,0.20],mode = 'lines'))
plot.add_trace(go.Scatter(x = [secondStdEnd,secondStdEnd], y = [0,0.20],mode = 'lines'))
plot.add_trace(go.Scatter(x = [thirdStdEnd, thirdStdEnd], y = [0,0.20],mode = 'lines'))

plot.show()
