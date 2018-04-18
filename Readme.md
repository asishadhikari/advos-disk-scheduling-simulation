# Disk Scheduling Simulation  
**For N disk access requests, calculate the total distance moved by the head** 
___
### To run:
* ```python simulation.py``` 

### To load data
* In ```data``` line 1 represents the initial head position
* Line 2 represents the space separated cylinder addresses for disk access
* see data in repo to look at a sample
* only 3 lines are parsed in this implementation

### Results:
Total distance moved for FCFS  is  13011  
Total distance moved for SSTF  is  7586  
Total distance moved for SCAN  is  7492  
Total distance moved for LOOK  is  7424  
Total distance moved for CSCAN is  9917  
Total distance moved for CLOOK is  9137  
