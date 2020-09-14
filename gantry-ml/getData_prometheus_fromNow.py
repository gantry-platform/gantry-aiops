#!/usr/bin/env python

# coding: utf-8
# # Prometheus에서 Data 수집 
# 메트릭 데이터를 개발 캔트리(Dev Gangry)에서 수집. 수집 메트릭 데이터는 CPU, Memory.

import requests
import json
import time
import pandas as pd

prom_query_range_url = 'http://13.125.42.163:30915/api/v1/query_range?query='
prom_query_url = 'http://13.125.42.163:30915/api/v1/query?query='

def call_data(url, query):
    r = requests.get(url + query)
    return r

def convert_range_time():
    start_time = '2020-08-04T00:00:00Z'
    #end_time = '2020-08-27T23:59:59Z' 
    
    now = time.localtime()
    current_date = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
    current_time = "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
    
    current_d_t = current_d_t = current_date + 'T' + current_time + 'Z'
    
    step = '10m'
    
    c_start_time = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.mktime(time.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ"))))
    #c_end_time = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.mktime(time.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ"))))
    
    #start_end_step = '&start=' + c_start_time + '&end=' + c_end_time + '&step=' + step
    start_end_step = '&start=' + c_start_time + '&end=' + current_d_t + '&step=' + step
    
    return start_end_step

# 날짜 테스트 현재 시간, 현재 시스템 시간 확인 
print(convert_range_time())

# web cur code for test
'''
cpu_query = 'instance:node_cpu:rate:sum'
query_range = '&start=2020-08-04T00:00:00Z&end=2020-08-04T05:56:48Z&step=10m'
query_structure = cpu_query + query_range
print(query_structure)
print(prom_query_range_url + query_structure)

rr = call_data(prom_query_range_url, query_structure)
print(rr)
'''

# CPU
def cpu_data():
    cpu_query = 'instance:node_cpu:rate:sum'
    query_range = str(convert_range_time())
    query_structure = cpu_query + query_range
    cpu_r = call_data(prom_query_range_url, query_structure)
    cpu_result = json.loads(cpu_r.text)
    #print('result size=', len(cpu_result['data']['result'])) 
    ###print("===== CPU RESULT =====")
    
    instance_list = []
    cpu_value_list = []
    time_list = []

    list_cpu = []
    for item in cpu_result['data']['result']:
        #print(item['metric']['instance'], item['values'])
        #print('value size=', len(item['values']))
        len_value = len(item['values'])
        #for item2 in item['values']:
        #    print('item2=', item2)
        
        for i in range(len_value):
            #print(item['metric']['instance'], i, item['values'][i])
            time_list.append(item['values'][i][0])
            instance_list.append(item['metric']['instance'])
            cpu_value_list.append(item['values'][i][1])

            #dict
            item_cpu = {'time': item['values'][i][0], 'cpu_instance':item['metric']['instance'], 'cpu_value':item['values'][i][1]}
            list_cpu.append(item_cpu)
            #print(item_cpu)
            
    ###print("======================")
    #return (cnt_cpu, time_list, instance_list, cpu_value_list)
    return (list_cpu)

# Memory
def memory_data():
    memory_query = 'instance:node_memory_utilisation:ratio'
    query_range = str(convert_range_time())
    query_structure = memory_query + query_range
    memory_r = call_data(prom_query_range_url, query_structure)
    memory_result = json.loads(memory_r.text)
    #print('result size=', len(cpu_result['data']['result'])) 
    ###print("===== MEMORY RESULT =====")
    instance_list = []
    memory_value_list = []
    time_list = []

    list_memory = []
    for item in memory_result['data']['result']:
        len_value = len(item['values'])

        for i in range(len_value):
            #print(item['metric']['instance'], i, item['values'][i])
            time_list.append(item['values'][i][0])
            instance_list.append(item['metric']['instance'])
            memory_value_list.append(item['values'][i][1])
            
            # dict
            item_memory = {'time':item['values'][i][0], 'memory_instance':item['metric']['instance'], 'memory_value': item['values'][i][1]}
            list_memory.append(item_memory)
            
    ###print("=========================")
    #return (cnt_mem, time_list, instance_list, memory_value_list)
    return(list_memory)


# Merge Data
def merge_metric_data():
    list_cpu = cpu_data()
    list_memory = memory_data()

    df_cpu = pd.DataFrame(list_cpu)
    df_memory = pd.DataFrame(list_memory)
    
    inst_cpu = df_cpu["cpu_instance"].unique()
    inst_memory = df_memory["memory_instance"].unique()
    
    inst = pd.concat([df_cpu['cpu_instance'], df_memory['memory_instance']]).unique()
    #print(inst)
    
    len_list_inst = len(inst)
    
    dict_result = {}
    for k in range(len_list_inst):
        key = inst[k]
        
        temp_df_cpu = df_cpu[df_cpu.cpu_instance == key]
        temp_df_memory = df_memory[df_memory.memory_instance == key]
        temp_merge = pd.merge(temp_df_cpu, temp_df_memory, how='outer')
        
        dict_result[key] = temp_merge
        merge_data = dict_result[key]
        merge_data.to_csv("./m_data_" + key + ".csv", mode='w')

if __name__=="__main__":
    #print(cpu_data())
    #print(memory_data())
    print(merge_metric_data())

