from matplotlib import pyplot as plt
import statistics
import csv
#import pandas as pd

filename = open('./java-repos-csv/gobblin.csv', 'r')
data_file = csv.DictReader(filename)
date, commit, coverage = [], [], []
for column in data_file:
    date.append(column['timestamp'])
    commit.append(column['Commit Hash'])
    coverage.append(float(column['Code Coverage']))

coverage_mean = statistics.mean(coverage)
coverage_variance = statistics.pvariance(coverage)
coverage_std = statistics.stdev(coverage)

cov_rows = len(coverage)
clean_cov = []
for index in range(cov_rows):
    if coverage[index] >= (coverage_mean - coverage_std/2):
        clean_cov.append(coverage[index])


fig, ax = plt.subplots()
ax.plot(coverage)
ax.plot(clean_cov)
plt.show()
