import pandas
import numpy
import matplotlib.pyplot as plt

"""
Plotting bars chart and saving in jpeg format
replacing the old one
"""
def create_plot(column_name, tail_size=10):
    if tail_size < 0:
        tail_size *= 1
    data_frame = pandas.read_csv('data.csv').tail(tail_size)
    if column_name not in data_frame.columns.tolist():
        return -1
    else:
        data = data_frame.loc[:,column_name].to_numpy()
        unique, counts = numpy.unique(data, return_counts=True)
        data = dict(zip(unique, counts)) 
        plt.bar(range(len(data)), list(data.values()), align='center')
        plt.xticks(range(len(data)), list(data.keys()))
        plt.savefig(column_name+'.jpeg')
        plt.cla()
        return 0
