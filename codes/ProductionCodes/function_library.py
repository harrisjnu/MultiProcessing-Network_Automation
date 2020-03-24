import json
import os
import sys
import glob

def getlatestfile(hostname):
    try:
        path = ('CONFIG_BACKUPS/' + hostname + '/')
        path = (path + str('*'))
        #logging.info('FUNTION: getlatestfile() - PATH FOR STORAGE IS ' + path)
        list_of_files = glob.glob(path)  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)  # get latest file created
        #logging.info('FUNTION: getlatestfile() - LAST STORED FILE OF DEVICE ' + hostname + ' is ' + latest_file)
        return latest_file
    except:
        #logging.info("FUNTION: getlatestfile() - NO EXISTING CONFIG DETECTED FOR " + hostname)
        return 'None'

def configstores(hostname, data):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = ('CONFIG_BACKUPS/' + hostname + '/' + timestamp + '.txt')
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except:
            print("Directory Creation Error")
            sys.exit()

    with open(filename, "w") as f:
        f.write(data)
        logging.info('FUNTION: conigstores() - Created file for ' + hostname + ' is ' + filename)
    path = ('CONFIG_BACKUPS/' + hostname + '/' )
    return path

def get_info(device):
    info = device.get_facts()
    #logging.debug('FUNTION: getinfo() - Facts Retrieved ' + info)
    return {'hostname':info['hostname'],'uptime':info['uptime'],'serial_number':['serial_number'],'model':['model']}

def ping_from_device(device,ip,sla=3.0):
    ping = device.ping(ip)
    #logging.debug('FUNTION: ping_from_device() TO ' + ip)
    #logging.debug('FUNTION: ping_from_device() RAW RESULT ' + ping)
    rtt_avg = ping['success']['rtt_avg']
    if rtt_avg == 0.0:
        return 'FAILED'
    elif rtt_avg <= sla:
        return 'WITHIN SLA LATENCY'
    elif rtt_avg > sla:
        return ('HIGH LATENCY ' + rtt_avg)
    else:
        return 'VALUE ERROR'

def trace_from_device(device,trace_ip,sla=3.0):
    trace = device.traceroute(trace_ip)
    trace  = json.dumps(trace, sort_keys=True, indent=4)
    return trace

def result_preprocessor(cmd,data):
    if cmd == 'sh run' or 'show running-config':
        data = (data.splitlines())[8:]
        data_return = '\n'.join(map(str, data)) # Removing variable content lines in backup
        return data_return
    else:
        return data
