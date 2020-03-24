# MultiProcessing-Network_Mangement

CREDITS - COVID-19 LOCKDOWN - DAY1

Proof of Concept - Multi-Processing/Parallel Coding of Network Automation

Python based multi-processing module enabled codes for automating multi-channel automation of network devices. 
The codes use CSV uploaded device data to run NAPALM module to demostrate parallel network automation operations.
Parallel code operations are essential in automating large deployments as they are key to realtime updates and 
responses. Exiting automation codes can be ported to multi-processing by re-engineering the function blocks. Multi-Threading
is not recommended for network automation as they throw high risk of memory space conflicts if not specifically take care of.
Replace the function block to suit purposes.

Read dependecy file and common deployment issues. Change device.csv file to meet simulation scenario befor running.
User "pip install requirements.txt" on Python 3.6 or use Virtual environment uploaded.

UPDATES 25th Mar 2020

Improvement!!!

CREDITS - COVID-19 LOCKDOWN - DAY3

1. Library Functions for 3rd Party calls.
2. Timestamped configuration backups.
3. Parallel Operations. Tested on 93 Router/L3 production network. Avg execution time 60.5 Secs. Avg of less than 1 sec/device.
4. Configuration changes through txt file, gap/difference finding, confirmation before push.
5. Configuration roll back by auto creating roll back file post commit .
