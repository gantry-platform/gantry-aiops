{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Prometheus에서 Data 수집 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "메트릭 데이터를 개발 캔트리(Dev Gangry)에서 수집. 수집 메트릭 데이터는 CPU, Memory."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import json\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "prom_query_range_url = 'http://13.125.42.163:30915/api/v1/query_range?query='\n",
    "prom_query_url = 'http://13.125.42.163:30915/api/v1/query?query='"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def call_data(url, query):\n",
    "    r = requests.get(url + query)\n",
    "    return r"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def convert_range_time():\n",
    "    start_time = '2020-08-01T00:00:00Z'\n",
    "    #end_time = '2020-07-10T11:59:59Z' \n",
    "    \n",
    "    now = time.localtime()\n",
    "    current_date = \"%04d-%02d-%02d\" % (now.tm_year, now.tm_mon, now.tm_mday)\n",
    "    current_time = \"%02d:%02d:%02d\" % (now.tm_hour, now.tm_min, now.tm_sec)\n",
    "    current_d_t = current_d_t = current_date + 'T' + current_time + 'Z'\n",
    "    \n",
    "    step = '10m'\n",
    "    \n",
    "    c_start_time = time.strftime(\"%Y-%m-%dT%H:%M:%SZ\", time.gmtime(time.mktime(time.strptime(start_time, \"%Y-%m-%dT%H:%M:%SZ\"))))\n",
    "    #c_end_time = time.strftime(\"%Y-%m-%dT%H:%M:%SZ\", time.gmtime(time.mktime(time.strptime(end_time, \"%Y-%m-%dT%H:%M:%SZ\"))))\n",
    "    #start_end_step = '&start=' + c_start_time + '&end=' + c_end_time + '&step=' + step\n",
    "    start_end_step = '&start=' + c_start_time + '&end=' + current_d_t + '&step=' + step\n",
    "    return start_end_step"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "&start=2020-08-01T00:00:00Z&end=2020-08-19T05:26:37Z&step=10m\n"
     ]
    }
   ],
   "source": [
    "# 날짜 테스트 현재 시간, 현재 시스템 시간 확인 \n",
    "print(convert_range_time())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"\\ncpu_query = 'instance:node_cpu:rate:sum'\\nquery_range = '&start=2020-06-01T00:00:00Z&end=2020-07-04T05:56:48Z&step=10m'\\nquery_structure = cpu_query + query_range\\nprint(prom_query_range_url + query_structure)\\n\\nrr = call_data(prom_query_range_url, query_structure)\\nprint(rr)\\n\""
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# web cur code for test\n",
    "'''\n",
    "cpu_query = 'instance:node_cpu:rate:sum'\n",
    "query_range = '&start=2020-06-01T00:00:00Z&end=2020-07-04T05:56:48Z&step=10m'\n",
    "query_structure = cpu_query + query_range\n",
    "print(prom_query_range_url + query_structure)\n",
    "\n",
    "rr = call_data(prom_query_range_url, query_structure)\n",
    "print(rr)\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# CPU\n",
    "def cpu_data():\n",
    "    cpu_query = 'instance:node_cpu:rate:sum'\n",
    "    query_range = str(convert_range_time())\n",
    "    query_structure = cpu_query + query_range\n",
    "    cpu_r = call_data(prom_query_range_url, query_structure)\n",
    "    cpu_result = json.loads(cpu_r.text)\n",
    "    #print('result size=', len(cpu_result['data']['result'])) \n",
    "    ###print(\"===== CPU RESULT =====\")\n",
    "    instance_list = []\n",
    "    cpu_value_list = []\n",
    "    time_list = []\n",
    "    global cnt \n",
    "    cnt = 0\n",
    "    for item in cpu_result['data']['result']:\n",
    "        #print(item['metric']['instance'], item['values'])\n",
    "        #print('value size=', len(item['values']))\n",
    "        len_value = len(item['values'])\n",
    "        #for item2 in item['values']:\n",
    "        #    print('item2=', item2)\n",
    "        for i in range(len_value):\n",
    "            #print(item['metric']['instance'], i, item['values'][i])\n",
    "            time_list.append(item['values'][i][0])\n",
    "            instance_list.append(item['metric']['instance'])\n",
    "            cpu_value_list.append(item['values'][i][1])\n",
    "            cnt = cnt + 1\n",
    "    ###print(\"======================\")\n",
    "    #print(instance_list)\n",
    "    #print(cpu_value_list)\n",
    "    return (cnt, time_list, instance_list, cpu_value_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Memory\n",
    "def memory_data():\n",
    "    memory_query = 'instance:node_memory_utilisation:ratio'\n",
    "    query_range = str(convert_range_time())\n",
    "    query_structure = memory_query + query_range\n",
    "    memory_r = call_data(prom_query_range_url, query_structure)\n",
    "    memory_result = json.loads(memory_r.text)\n",
    "    #print('result size=', len(cpu_result['data']['result'])) \n",
    "    ###print(\"===== MEMORY RESULT =====\")\n",
    "    instance_list = []\n",
    "    memory_value_list = []\n",
    "    time_list = []\n",
    "    for item in memory_result['data']['result']:\n",
    "        len_value = len(item['values'])\n",
    "        for i in range(len_value):\n",
    "            #print(item['metric']['instance'], i, item['values'][i])\n",
    "            time_list.append(item['values'][i][0])\n",
    "            instance_list.append(item['metric']['instance'])\n",
    "            memory_value_list.append(item['values'][i][1])\n",
    "    ###print(\"=========================\")\n",
    "    return (time_list, instance_list, memory_value_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merge Data\n",
    "def merge_metric_data():\n",
    "    cnt, cpu_time, cpu_instance, cpu_value = cpu_data()\n",
    "    memory_time, memory_instance, memory_value = memory_data()\n",
    "    data = []\n",
    "    \n",
    "    #print(\"count, \", \"CPU_TIME, \", \"MEMROY_TIME, \", \"CPU_INSANCE, \", \"MEMORY_INSTANCE, \", \"CPU_VALUE, \", \"MEMORY_VALUE\")\n",
    "    header = \"date,time,cpu,memory\"\n",
    "    f = open(\"../csv_data/m_data_fromNow.csv\", 'w')  # time, cpu\n",
    "    f.write(header + \"\\n\")\n",
    "    for i in range(cnt):\n",
    "        if cpu_instance[i] == '10.11.1.80:9091':   ## 특정노드 데이터 추출 하드코딩 변경 필요\n",
    "            #print(str(i).zfill(4), cpu_time[i], memory_time[i], cpu_instance[i], memory_instance[i], cpu_value[i], memory_value[i])\n",
    "            #date_time = time.strftime(\"%Y-%m-%d %H:%M:%S\", time.localtime(int(cpu_time[i])))\n",
    "            date_time = time.strftime(\"%Y-%m-%d,%H:%M:%S\", time.localtime(int(cpu_time[i])))\n",
    "            m_data = str(date_time) + \",\" + str(cpu_value[i]) + \",\" + str(memory_value[i]) + '\\n'\n",
    "            #data = str(date_time) + \",\" + str(cpu_value[i]) + \",\" + str(memory_value[i])  +  \"\\n\"\n",
    "            f.write(m_data) \n",
    "    f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "if __name__==\"__main__\":\n",
    "    #print(cpu_data())\n",
    "    #print(memory_data())\n",
    "    print(merge_metric_data())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
