#!/bin/bash
CUDA_VISIBLE_DEVICES=0 python scripts/im_pipeline.py pipelines/im_pipeline.yaml 0_sampletrajs
CUDA_VISIBLE_DEVICES=0 python scripts/im_pipeline.py pipelines/im_pipeline.yaml 1_train
CUDA_VISIBLE_DEVICES=0 python scripts/im_pipeline.py pipelines/im_pipeline.yaml 2_eval
