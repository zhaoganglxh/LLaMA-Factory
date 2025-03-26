#!/bin/bash
# DO NOT use GPTQ/AWQ model in FSDP+QLoRA

CUDA_VISIBLE_DEVICES=0,1 accelerate launch \
    --config_file examples/accelerate/fsdp_config.yaml \
    src/train.py examples/extras/fsdp_qlora/qwen2.5/qwen2.5_lora_sft.yaml
