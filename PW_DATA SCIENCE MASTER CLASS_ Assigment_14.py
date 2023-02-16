#!/usr/bin/env python
# coding: utf-8

# # Assignment _14-02-2023

# ## 1.What is multiprocessing in python? Why is it useful?
# 
# ### Ans:-
#     Multiprocessing in Python is a technique of running multiple processes in parallel to improve the performance of a 
#     program. In other words, it is the execution of multiple threads or processes simultaneously on a computer system to 
#     achieve maximum performance.The multiprocessing module in Python provides a way to create and manage subprocesses. 
#     It allows you to leverage multiple CPU cores to perform CPU-bound tasks more efficiently.
#     
#     Here are a few benefits of using multiprocessing in Python:
#     
#     1. Increased Performance:- When using multiprocessing, you can execute multiple processes or threads in parallel, 
#     which can significantly increase the performance of your program.
#     
#     2.Better Resource Utilization:- Multiprocessing allows you to take advantage of multiple CPU cores, which can help 
#     you utilize your system's resources more efficiently.
#     
#     3.Improved Responsiveness:- By separating long-running tasks into separate processes, you can improve the 
#     responsiveness of your program and prevent it from becoming unresponsive or freezing.
#     
#     4.Scalability:- Multiprocessing provides a scalable solution that can be used to handle larger workloads as your 
#     program grows.
#     
#     
#                                         Overall, multiprocessing is useful in Python for achieving higher performance and
#     better resource utilization in CPU-bound tasks. It is particularly useful in scientific computing, data processing, 
#     and machine learning, where the performance gains can be substantial.
#     
#     
# 
# 
# 

# ## 2. What are the different between multiprocessing and multithreading?
# 
# ### Ans:-
#           
#          

#                         MULTIPROCESSING                                       MULTITHREADING
#    __________________________________________________________________________________________________________________________      
#     Execution Model: In multiprocessing, multiple processes        Execution Model:-in multithreading, multiple threads
#     run concurrently, and each process has its own memory             run within a single process, sharing the same memory 
#     space,                                                            space.
#     
#     Resource Management:- Processes are manged by the operating    Resource Management:-All threads share the same resources
#       system,and each process has its own system resources such        and it is up to the programmmer to manage access to 
#       as CPU,memory and file handles.                                  shared resources to prevent conflicts.
#       
#     Parallelism:-It can take advantage of multiple CPUs or cores   Parallelism:-It can only advantage of single CPU or core 
#        allowing true parallelism.                                      providing concurrency but not true Parallelism.
#        
#     Overhead:- More Overhead                                        Overhead:-  Less Overhead
#     
#     Complexity:-multiprocessing can be simpler because each        Complexity :- Multithreading can be more complex to 
#          process has its own memory space and resources.           program because of the need to manage shared resources 
#                                                                    and prevent conflicts.
#                                                                    
#                                   
#                                   In summary, multiprocessing is useful when you need to take advantage of multiple CPUs 
#      or cores for true parallelism, while multithreading is useful for achieving concurrency within a single process when 
#      managing shared resources is not too complicated.

# ## 3. Write a python code to create a process using the multiprocessing module.
# 
# ### Ans:-
# 

# In[3]:


import multiprocessing

def worker():
    print("Worker process started")
                                    # Do some work here...
    print("Worker process finished")

if __name__ == '__main__':
                                    # Create a new process
    p = multiprocessing.Process(target=worker)

                                    # Start the process
    p.start()

                                    # Wait for the process to finish
    p.join()

    print("Main process finished")


# ## 4.What is a multiprocessing pool in python ? why it is used?
# 
# ### Ans:-
#     A multiprocessing pool in Python is a technique for distributing work across multiple processes. A pool is a 
#     collection of worker processes that can be used to execute tasks in parallel, with each worker process executing tasks 
#     independently.
#     
#     In Python, the multiprocessing.Pool class is used to create a pool of worker processes. The Pool class provides a 
#     convenient way to parallelize the execution of a function across multiple input values, by automatically distributing 
#     the work across the worker processes in the pool.
#     
#     Here are some reasons why you might use a multiprocessing pool in Python:
# 
#     1.Increased Performance: Using a pool of worker processes can help you achieve higher performance by executing tasks
#     in parallel, leveraging multiple CPUs or cores.
# 
#     2.Simplified Code: The multiprocessing.Pool class provides a high-level interface that simplifies the process of 
#     parallelizing code. You don't have to worry about creating and managing individual processes or threads, as the Pool 
#     class handles all of that for you.
# 
#     3.Improved Resource Management: The Pool class automatically manages the worker processes in the pool, allowing you to
#     focus on your code instead of managing system resources.
# 
#     4.Fault Tolerance: The multiprocessing.Pool class is fault-tolerant, meaning that it can handle failures in individual 
#     worker processes and continue executing tasks using the remaining processes.
#     
#     

# In[ ]:


import multiprocessing

def square(x):
    return x ** 2

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        # Map the square function to a list of inputs in parallel
        result = pool.map(square, [1, 2, 3, 4, 5])
        print("result",square)


# ## 5. How we can create a pool of worker processes in python using the multiprocessing module?
# 
# ### Ans:-
# 

# In[ ]:


import multiprocessing

def my_func(x):
    """A simple function to be executed in parallel."""
    return x * x

if __name__ == '__main__':
    # Create a pool of 4 worker processes
    with multiprocessing.Pool(4) as pool:
        # Map the function to a list of inputs and execute them in parallel
        result = pool.map(my_func, [1, 2, 3, 4, 5])

    # Print the results
    print(result)


# ## 6. Write a python program to create 4 processes, each process should print a different number using a multiprocessing module in python?
# 
# ### Ans:-

# In[2]:


def print_number(num):
    print("Process ID:", multiprocessing.current_process().pid, "Number:", num)

if __name__ == '__main__':
    num_list = [1, 2, 3, 4]
    processes = []
    for num in num_list:
        p = multiprocessing.Process(target=print_number, args=(num,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

