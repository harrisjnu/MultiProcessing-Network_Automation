

## NAPALM LIBRARY BASED NETWORK AUTOMATION

## Module Imports

from napalm import get_network_driver
import csv
import multiprocessing as mp
import time
import json

print('CPU COUNT FOR MULTIPROCESSING :  ' + str(mp.cpu_count()))

def device_operations(device):
    device.open()
    #print(device.get_facts())
    #ping_base = device.traceroute('1.1.1.1')
    #ping_base  = json.dumps(ping_base, sort_keys=True, indent=4)
    #print(ping_base)
    res = device.get_facts()
    print(res['hostname'])
    #commands = ['show run']
    #res = device.cli(commands)
    #print(res['show run'])
    device.load_replace_candidate(filename='r1_config.txt')
    diff = device.compare_config()
    if len(diff) > 0:
        print(diff)
    # device.load_replace_candidate(filename='r1_config.txt')
    # print(device.compare_config())
    device.close()

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
            if os_type == 'ios':
                driver = get_network_driver('ios')
            elif os_type == 'junos':
                driver = get_network_driver('junos')

            optional_args = {'secret': secret}
            device = driver(ip, username, password, optional_args=optional_args)
            device_list.append(device)

    start = time.time()

    processes = list()

    for device in device_list:
        processes.append(mp.Process(target=device_operations, args=(device,)))

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    end = time.time()

    print('Script execution time:', end - start)
##
##
# #########################################################################
# with open('devices.csv','r') as devices:
#     reader = csv.reader(devices)
#     next(reader)
#     for row in reader:
#         print(row)
#         ip = row[0]
#         hostname = row[1]
#         username = row[2]
#         password = row[3]
#         secret = row[4]
#         os_type = row[5]
#
#         if os_type == 'ios':
#             driver = get_network_driver('ios')
#         elif os_type == 'junos':
#             driver = get_network_driver('junos')
#
#         optional_args = {'secret':secret}
#
#         device = driver(ip,username,password,optional_args=optional_args)
#         deviceoperations(device)


# 192.168.150.52,r2.cisco.com,admin,cisco,cisco,ios
# 192.168.150.53,r3.cisco.com,admin,cisco,cisco,ios
# 192.168.150.54,r4.cisco.com,admin,cisco,cisco,ios
# 192.168.150.55,r5.cisco.com,admin,cisco,cisco,ios
# 192.168.150.56,r1.cisco.com,admin,cisco,cisco,ios