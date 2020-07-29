import requests
import json
import time

prom_query_range_url = 'http://13.124.167.81:32406/api/v1/query_range?query='
prom_query_url = 'http://13.124.167.81:32406/api/v1/query?query='

def call_data(url, query):
    r = requests.get(url + query)
    return r

def convert_range_time():
    start_time = '2020-06-22T00:00:00Z'
    end_time = '2020-06-28T11:59:59Z' 
    step = '5m'

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
    ###print("===== CPU RESULT =====")
    instance_list = []
    cpu_value_list = []
    time_list = []
    global cnt 
    cnt = 0
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
            cnt = cnt + 1
    ###print("======================")
    #print(instance_list)
    #print(cpu_value_list)
    return (cnt, time_list, instance_list, cpu_value_list)

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
    for item in memory_result['data']['result']:
        len_value = len(item['values'])
        for i in range(len_value):
            #print(item['metric']['instance'], i, item['values'][i])
            time_list.append(item['values'][i][0])
            instance_list.append(item['metric']['instance'])
            memory_value_list.append(item['values'][i][1])
    ###print("=========================")
    return (time_list, instance_list, memory_value_list)


def x_data():
    cnt, cpu_time, cpu_instance, cpu_value = cpu_data()
    memory_time, memory_instance, memory_value = memory_data()
    data = []
    
    #print("count, ", "CPU_TIME, ", "MEMROY_TIME, ", "CPU_INSANCE, ", "MEMORY_INSTANCE, ", "CPU_VALUE, ", "MEMORY_VALUE")
    header = "ds,y"
    f = open("prophet_data.csv", 'w')  # time, cpu
    f.write(header + "\n")
    for i in range(cnt):
        if cpu_instance[i] == '10.11.0.106:9100':   ## 특정노드 데이터 추출 하드코딩 변경 필요
            #print(str(i).zfill(4), cpu_time[i], memory_time[i], cpu_instance[i], memory_instance[i], cpu_value[i], memory_value[i])
            #date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(cpu_time[i])))
            date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(cpu_time[i])))
            #data = str(date_time) + "," + str(cpu_value[i]) + "," + str(memory_value[i])  +  "\n"
            time_data_cpu = str(date_time) + "," + str(cpu_value[i]) +  "\n"
            #print(data)
            f.write(time_data_cpu) 
    f.close()

if __name__=="__main__":
    #print(cpu_data())
    #print(memory_data())
    print(x_data())
