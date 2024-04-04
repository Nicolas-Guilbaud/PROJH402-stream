from time import time
from os import getcwd, listdir, path, makedirs
import importlib
import matplotlib.pyplot as plt
import multiprocessing

'''
runtime_measures.py

This script is used to measure the runtime of the main scripts in the project.
It serves to show the improvements made.

'''

# Getting files to run
data = [i.removesuffix('.py') for i in listdir(getcwd()) if i.startswith('main') and i.endswith('.py')]
output_folder = getcwd()+'/outputs/runtime'

def take_measure(file):
    """
    Measure the time it takes to run a file.
    """
    try:
        start_time = time()
        importlib.import_module(file)
        end_time = time()
        return end_time - start_time
    except Exception as e:
        print(f"Error in {file}: {e}")
        return -1

def run(**kwargs):
    """
    Run a battery of tests with corresponding arguments.
    """
    for test_name in kwargs.keys():
        core_pool = None
        if kwargs[test_name][0]:
            cpus = multiprocessing.cpu_count()
            core_pool = multiprocessing.Pool(cpus)
        run_a_test(test_name,core_pool,)

    

def run_a_test(*args):
    """
    Run a test with the given arguments:
    - args[0]: the name of the file to save the plot
    - args[1]: pool of cores to use during the execution

    The test executes all the main files and measure their runtime.
    The result is showed in a bar plot, which is saved under the 'outputs/runtime' folder.
    """

    global core_pool
    core_pool = args[1]

    results = {i: take_measure(i) for i in data}

    print("Execution times:")
    for i in results:
        print(f"\t - {i}: {results[i]}")
    
    plt.figure()
    bars = plt.bar(results.keys(), results.values())

    plt.xticks(rotation=30, horizontalalignment='right')
    plt.xlabel('Files')
    plt.ylabel('Execution time (s)')
    plt.title('Runtime with multiprocessed GA')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom')  # va: vertical alignment

    #create output folder if it does not exist
    if not path.exists(output_folder):
        makedirs(output_folder)
    
    # Save the plot & display it
    plt.savefig(output_folder+args[0]+".png")
    plt.show()

# Format: {file_name: (multithreaded)}
tests_args = {
    # 'runtime_without_improvement': (False,),
    'runtime_ga_improved': (True,)
}

if __name__ == "__main__":
    run(**tests_args)
    
    print("All tests finished")