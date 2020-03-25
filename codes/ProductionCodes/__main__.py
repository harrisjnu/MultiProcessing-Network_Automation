


## NAPALM LIBRARY BASED NETWORK AUTOMATION

## Module Imports

from napalm import get_network_driver
import csv
import multiprocessing as mp
import time
import logging
from function_library import *

#Enable Logging Module

#logging.basicConfig(level=logging.INFO)
# logging.debug('Logging Level is DEBUG')
# logging.info('Logging Level is INFO')
# logging.warning('Logging Level is WARNING')
# logging.error('Logging Level is ERROR')
# logging.critical('Logging Level is CRITICAL')

print('CPU COUNT AVAILABLE FOR MULTIPROCESSING :  ' + str(mp.cpu_count()))

devices_processed = []
base_ip = '10.101.0.1' # IP OF NETWORK CORE/MANAGEMENT SERVER
trace_ip = '8.8.8.8'
config_check = False

def device_operations(device):
    try:
        device.open()

            ### PRODUCTION CODE BEGIN
        # CHECK FOR PING AND LATENCY SLA in ms
        #respond = ping_from_device(device,base_ip,5.00)
        #print(respond)
        # CHECK FOR TRACEROUTE
        # trace = trace_from_device(device, trace_ip, 5.00)
        # print (trace)
        device_info = get_info(device)
        #print(device_info['hostname'])
        last_file = getlatestfile(hostname)
        if last_file == 'None':
            logging.debug('FUNCTION: deviceoperations() NO CONFIG RECORD EXISTS CREATING')
        else:
            logging.debug('FUNCTION: deviceoperations() LAST CONFIG RECORD IS ' + last_file)

        ### CONFIG CHANGES EVALUATION AND ROLLBACK

        if config_check == True:
            device.load_replace_candidate(filename=last_file)
            diff = device.compare_config()
            print(diff)
            if len(diff) > 0:
                print(diff)
                user = input('Commit changes?<yes|no>')
                if user == 'yes':
                    print('Commit changes...')
                    #device.commit_config() #--> DOUBLE HASHED. CAREFUL AND UNDERSTAND. IRREVERSABLE CONFIG CHANGE
                    print('Done')
                else:
                    print('No changes required')
                    ##device.discard_config() #--> DOUBLE HASHED. CAREFUL AND UNDERSTAND. IRREVERSABLE CONFIG CHANGE

            user = input('Rollback?<yes|no>')
            if user == 'yes':
                print('ROLLING BACK CONFIG')
                ##device.rollback() #--> DOUBLE HASHED. CAREFUL AND UNDERSTAND. IRREVERSABLE CONFIG CHANGE
                print('Done')
        ###
        commands = ['show run']
        res = device.cli(commands)
        running_config = (res['show run'])
        running_config = result_preprocessor(commands,running_config)
        configstores(hostname,running_config)
            ### PRODUCTION CODE ENDS

        device.close()
    except:
        pass


if __name__ == "__main__":
    with open('devices.csv', 'r') as devices:
        reader = csv.reader(devices)
        next(reader)

        device_list = list()

        for row in reader:
            ip = row[0]
            hostname = row[1]
            username = row[2]
            password = row[3]
            secret = row[4]
            os_type = row[5]
            devices_processed.append(hostname)
            if os_type == 'ios':
                driver = get_network_driver('ios')
            elif os_type == 'junos':
                driver = get_network_driver('junos')

            optional_args = {'secret': secret}
            device = driver(ip, username, password, optional_args=optional_args)
            device_list.append(device)

    start = time.time()

    processes = list()
    
### PARALLEL PROCESSING BLOCKS
    for device in device_list:
        processes.append(mp.Process(target=device_operations, args=(device,)))

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print(devices_processed)
    print(len(devices_processed))
    print('Script execution time:', end - start)
