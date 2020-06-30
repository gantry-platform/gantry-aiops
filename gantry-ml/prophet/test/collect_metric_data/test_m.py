import requests
import json
import time

prom_query_range_url = 'http://13.125.152.20:30693/api/v1/query_range?query='
prom_query_url = 'http://172.20.11.121:30693/api/v1/query?query='

def call_data(url, query):
    r = requests.get(url + query)
    return r

def convert_range_time():
    start_time = '2020-06-11T11:00:08Z'
    end_time = '2020-06-11T11:51:25Z'
    step = '20m'

    c_start_time = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.mktime(time.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ"))))
    c_end_time = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.mktime(time.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ"))))
    start_end_step = '&start=' + c_start_time + '&end=' + c_end_time + '&step=' + step
    return start_end_step


def cpu_data():
    cpu_query = 'instance:node_cpu:rate:sum'
    query_range = str(convert_range_time())
    query_structure = cpu_query + query_range
    cpu_r = call_data(prom_query_range_url, query_structure)
    cpu_result = json.loads(cpu_r.text)
    #print('result size=', len(cpu_result['data']['result'])) 
    print("===== CPU RESULT =====")
    for item in cpu_result['data']['result']:
        #print(item['metric']['instance'], item['values'])
        #print('value size=', len(item['values']))
        len_value = len(item['values'])
        #for item2 in item['values']:
        #    print('item2=', item2)
        for i in range(len_value):
            print(item['metric']['instance'], i, item['values'][i])
    print("======================")


def memory_data():
    memory_query = 'instance:node_memory_utilisation:ratio'
    query_range = str(convert_range_time())
    query_structure = memory_query + query_range
    memory_r = call_data(prom_query_range_url, query_structure)
    memory_result = json.loads(memory_r.text)
    #print('result size=', len(cpu_result['data']['result'])) 
    print("===== MEMORY RESULT =====")
    for item in memory_result['data']['result']:
        len_value = len(item['values'])
        for i in range(len_value):
            print(item['metric']['instance'], i, item['values'][i])
    print("=========================")


if __name__=="__main__":
    print(cpu_data())
    print(memory_data())

