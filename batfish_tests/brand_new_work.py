

import pandas as pd
from pybatfish.client.commands import *
from pybatfish.datamodel import *
from pybatfish.datamodel.answer import *
from pybatfish.datamodel.flow import *
from pybatfish.question import *
from pybatfish.question import bfq
from pprint import pprint
import json
import getpass
from pprint import pprint
import yaml

def open_yml_file(file_name):
    with open(file_name, "r") as stream:
        return yaml.safe_load(stream)

# Documentation https://batfish.readthedocs.io/en/latest/index.html
# Docker host running
# sudo docker run -v batfish-data:/data -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone
# Once you have run this once to start it back up you'll need to run "docker start [huge ID line]"
bf_session.host = '192.168.0.112'
print (1)
load_questions()
print (2)
network_name = 'lab'
snapshot_path = './snapshots/lab/'
bf_set_network(network_name)
bf_session.init_snapshot(snapshot_path, name=network_name, overwrite=True)

# getpass.getpass("Going over the setup code")
# .frame makes it into pandas data.... wish I knew pandas
# pprint(dir(bfq))
print(bfq.routes().answer().frame())

# How did the parsing go?
# pprint(bfq.fileParseStatus().answer().frame())
# What failed?  (something alwasy fails)
# pprint(bfq.parseWarning().answer().frame())
# getpass.getpass("Going over the parse warnings")

# Find duplicate IPs
print ("Dup IP addresses")
pprint(bfq.ipOwners(duplicatesOnly=True).answer().frame())
# See Data per row abit clearer
# pprint(bfq.ipOwners(duplicatesOnly=True).answer().frame().iloc[0])
# pwd = getpass.getpass("Show Duplicate IP addresses")
pprint(bfq.bgpSessionCompatibility().answer().frame())
# pwd = getpass.getpass("Show BGP session data")


def ip_flow_validation(bfq, src_ip, dst_ip, start_device,  end_dev=""):
    pprint(src_ip)
    return bfq.reachability(
        pathConstraints=PathConstraints(
            startLocation=start_device, 
            endLocation=end_dev
            ),
        headers=HeaderConstraints(srcIps=src_ip, dstIps=dst_ip),
        actions="FAILURE"
    ).answer().frame()


ip_tests = [
    {'src_ip': '10.0.0.1',
     'dst_ip': '10.0.0.1',
     'start_device': 'R1', },
    ]


def test_ip_flows(ip_tests):
    for test in ip_tests:
        results = ip_flow_validation(bfq, test['src_ip'],
                                     test['dst_ip'], test['start_device'])
        data = results.to_json()
        data = json.loads(data)
        pprint(data)
        print('\n')
        # getpass.getpass("Go over IP flow Test")

# results =test_ip_flows(ip_tests)


def port_flow_validation(bfq, src_ip, dst_ip, start_device, dst_port,  end_dev=""):
    pprint(src_ip)
    return bfq.reachability(
        pathConstraints=PathConstraints(
            startLocation=start_device, endLocation=end_dev),
        headers=HeaderConstraints(
            srcIps=src_ip, dstIps=dst_ip, dstPorts=dst_port,
            ipProtocols=[
                # "UDP",
                "TCP"
            ]),
        actions="SUCCESS,FAILURE"
    ).answer().frame()

port_tests = open_yml_file('tests.yml')
pprint (port_tests)


# port_tests = [
#     {'src_ip': '10.0.0.1',
#      'test_name': 'bubba',
#      'dst_ip': '10.0.0.3',
#      'start_device': 'R1',
#      "end_device": 'R3',
#      'dst_port': '23'},
#     # {'src_ip': '10.0.0.5',
#     #  'test_name': 'ted',
#     #  'dst_ip': '8.8.8.8',
#     #  'start_device': 'R1',
#     #  'dst_port': '22'},
# ]


def test_port_flows(port_tests):
    # pprint (port_tests)
    all_results = []
    for test in port_tests:
        pprint (test)
        if 'end_device' in test:
            results = port_flow_validation(bfq, test['src_ip'],
                                       test['dst_ip'], test['start_device'], test['dst_port'],test['end_device'])
        else:
            results = port_flow_validation(bfq, test['src_ip'],
                                       test['dst_ip'], test['start_device'], test['dst_port'])              
        # pprint(dir(results))
        results['name'] = test['test_name']
        # pprint(results.dict())
        # pprint(results.dict()['status'])
        all_results.append(results)
        # pickle_data(results, 'pickle_data.pickle')
        # json_data = results.to_json()
        # json1_data = json.loads(json_data)
        # pprint(json1_data)
    return all_results


def pickle_data(data_frame, file_name):
    data_frame.to_pickle(file_name)


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

results = test_port_flows(port_tests)

# Thank you Rick Donato for your code


def pprint_reachability(answer):
    good_results= [
        "ACCEPTED",
        "DELIVERED_TO_SUBNET",
        "EXITS_NETWORK",
    ]
    # getpass.getpass("Type")
    # print(type(answer))
    # pprint(dir(answer))
    # pprint(dir(answer['name']))
    print('Test Name: ', answer['name'].values[0])
    # getpass.getpass("Type")
    print(f"Flow Summary")
    for index, row in answer.iterrows():
        print(f"Flow: {row['Flow']} (Trace Count:{row['TraceCount']})")
    print("==========")
    for index, row in answer.iterrows():
        print(f"Flow: {row['Flow']} (Trace Count:{row['TraceCount']})")
        for count, trace in enumerate(row["Traces"], start=1):
            print(f"\nTrace #{count}")
            print(f"{trace}")
            if trace.dict()['disposition'] not in good_results:
                print (trace.dict()['disposition'])
                raise Exception("Not reachable")
            # pprint (trace.dict())
        print("----")


        # pprint (dir(trace.dict))
        


for result in results:

    # data = result.to_json()
    # data = json.loads(data)
    # pprint(data)
    # print(result)
    pprint_reachability(result)
    # getpass.getpass("Show IP/Port Test")
    # pprint(results)




print ('Done')