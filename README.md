Copyright 2017 Massimo Girondi - Released under GPL v3 License

This is a very simple implementation of few basic scheduling algorithm, written in Python3.

I implemented them only for educational purposes.

The included algorithm are the following:

* First Come First Served
* Shortest Job First
* Shortest Remaining Time First
* Round Robin
* Highest Response Ratio Next

`sched.py` is the main file, it imports `process` class from `process.py` and the scheduling algorithms from `algoritmi.py`.

The process are read and put in the `memory` list at the beginning of the program and this list is passed by value to every algorithm, that remove the process from the list during the execution and put them into the `completed` queue.
