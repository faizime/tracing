from threading import Thread
import numpy as np
import time

def parallel_process(parallel_process_id,wait): #this should be a child trade
    """
    :param process_id:
    :return:
    """
    build_log(parallel_process_id)
    print(f"waiting {wait}")
    time.sleep(wait)

def execute_head_process(process_id):
    """
    executes several parallel processes
    :param process_id:
    :return:
    """
    print(f"Starting head process {process_id}")
    build_log(process_id)
    #this is actually done with subprocess but for this example multi thread is ok
    threads=[]
    for i in range(10):
        t=Thread(target=call_script, args=(parallel_process_id,np.random.randint(0,10)))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def build_log(log_file):
    pass
def main_process():
    """
    Main process runs forever
    :return:
    """
    process_ids=[1,2]
    build_log(main_process)
    counter=0
    while True:
        for pid in process_ids:
            execute_head_process(pid) #should be a trace child

        counter=counter+1
        if counter==10:
            break


