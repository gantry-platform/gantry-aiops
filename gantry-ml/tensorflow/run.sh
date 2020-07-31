#!/bin/bash

python metric_data/m_data.py
cd gantry_aiops
python classify_data_without_graph.py
python tf_logistic_regression.py

