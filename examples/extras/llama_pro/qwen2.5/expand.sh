#!/bin/bash

python scripts/llama_pro.py \
    --model_name_or_path /home/zhaogang/sources_linux/models/qwen-2.5-7b \
    --output_dir models/qwen2.5-7b-pro \
    --num_expand 7
