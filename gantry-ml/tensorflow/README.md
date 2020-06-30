# aiops

### 폴더 구조.   
```
├── README.md   
├── gantry_aiops   
│   ├── classify_data.py   
│   ├── cluster.csv    
│   ├── test_ml.py   
│   └── tf_logistic_regression.py   
├── metric_data     
│   ├── m_data.py   
│   ├── metric_data.csv   
│   └── test_m.py   
└── requirements.txt
```


## 환경 설정 
vritualenv 설치 
참조: https://www.tensorflow.org/install/pip?hl=ko#mac-os_1

## fast run
$ ./run.sh


## manual 실행 

### 메트릭 데이터 수집
```
cd metric_data
$ python m_data.py

count,  CPU_TIME,  MEMROY_TIME,  CPU_INSANCE,  MEMORY_INSTANCE,  CPU_VALUE,  MEMORY_VALUE 
0312 1592208728 1592208728 10.11.0.106:9100 10.11.0.106:9100 0.34213333333355567 0.7412692227895373
0313 1592208788 1592210408 10.11.0.106:9100 10.11.0.106:9100 0.3614545666666928 0.08976454454829286
...
1593 1592287088 1592190068 10.11.0.106:9100 10.11.0.73:9100 2.030833333333333 0.277358503932864
1594 1592287148 1592190128 10.11.0.106:9100 10.11.0.73:9100 1.998 0.2774374445897312
```
TIME 에서 0312까지는 동일한 시간대의 데이터를 수집하고 있지만, 그 이후 시간대가 다른 값이 추출됨 (확인필요)
 
 * m_data.py를 실행하면 동일 폴더에 metric_data.csv가 생성됨 
 * csv : cpu 값과 메모리 값만 추출. 

 ### 그룹 분류
 k mean 알고리즘을 이용하여 군집을 자동 분류함. 실행 후 cluster.csv 파일 생성되고 데이틀 확인하면 마지막 필드에 0, 1의 값으로 분류되어 있음. 
 ```
 $ cd gantry_aiops
 $ python classify_datay.py 
 ```

 ### logistic 모델 
 가설의 sigmoid로 추정하고 cost 학습은 경사하강법 적용 
 ```
 hypothesis = tf.sigmoid(tf.matmul(X, W) + b)
 train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
 ```
 ```
 $ cd gantry_aiops
 $ python tf_logistic_regression.py
 ```

