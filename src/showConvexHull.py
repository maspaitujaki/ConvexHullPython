import pandas as pd
import matplotlib.pyplot as plt
from myConvexHull.CHull import ConvexHull

def showConvexHull(dataSet, xIdx, yIdx):
    data = dataSet
    # create a DataFrame
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    plt.figure(figsize=(10, 6))
    colors = ['b', 'r', 'g', 'y', 'c', 'm', 'k']
    plt.title(str(data.feature_names[xIdx]) + " vs " + str(data.feature_names[yIdx]))
    plt.xlabel(data.feature_names[xIdx])
    plt.ylabel(data.feature_names[yIdx])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:, [xIdx, yIdx]].values
        hull = ConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        for simplex in hull.simplices:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i % 7])
    plt.legend()
    plt.show()