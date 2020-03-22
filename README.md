# MultiProcessing-Network_Mangement

Proof of Concept - Multi-Processing/Parallel Coding of Network Automation

Python based multi-processing module enabled codes for automating multi-channel automation of network devices. 
The codes use CSV uploaded device data to run NAPALM module to demostrate parallel network automation operations.
Parallel code operations are essential in automating large deployments as they are key to realtime updates and 
responses. Exiting automation codes can be ported to multi-processing by re-engineering the function blocks. Multi-Threading
is not recommended for network automation as they throw high risk of memory space conflicts if not specifically take care of.
Replace the function block to suit purposes.

Read dependecy file and common deployment issues. Change device.csv file to meet simulation scenario befor running.
User "pip install requirements.txt" on Python 3.6 or use Virtual environment uploaded.
