from time import time
from os import getcwd, listdir
import importlib
import matplotlib.pyplot as plt

# Getting files to run
data = [i.removesuffix('.py') for i in listdir(getcwd()) if i.startswith('main') and i.endswith('.py')]

def take_measure(file):
    try:
        start_time = time()
        importlib.import_module(file)
        end_time = time()
        return end_time - start_time
    except:
        return -1

if __name__ == "__main__":
    results = {i: take_measure(i) for i in data}

    print("Execution times:")
    for i in results:
        print(f"\t - {i}: {results[i]}")
    
    plt.figure()
    bars = plt.bar(results.keys(), results.values())

    plt.xticks(rotation=30, horizontalalignment='right')
    plt.xlabel('Files')
    plt.ylabel('Execution time (s)')
    plt.title('Runtime without optimization')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom')  # va: vertical alignment


    plt.savefig(getcwd()+'/outputs/runtime.png')
    plt.show()
