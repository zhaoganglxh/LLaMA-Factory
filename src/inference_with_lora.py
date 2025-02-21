from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import os
import torch
from transformers import TextStreamer

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"  # 确保环境变量设置正确
base_model_name = "/media/zhaogang/4T2-2-LLM/HuggingFace/models/qwen/qwen-2.5-7b/"
#lora_model_path = "/media/zhaogang/4T2-2-LLM/sources_linux/LLaMA-Factory/saves/qwen-2.5-7b/lora/sft"
lora_model_path = "/media/zhaogang/4T2-2-LLM/sources_linux/LLaMA-Factory/saves/qwen-2.5-7b/lora/dpo"
#lora_model_path = "/media/zhaogang/4T2-2-LLM/sources_linux/LLaMA-Factory/saves/qwen-2.5-7b/lora/sft_cuda0"
device = "cuda"

# 加载基础模型和LoRA模型，并设置为float16以减少显存占用
base_model = AutoModelForCausalLM.from_pretrained(base_model_name, torch_dtype=torch.float16)
model = PeftModel.from_pretrained(base_model, lora_model_path)

# 将模型移动到GPU并启用多GPU并行计算
model = model.to(device)
model = torch.nn.DataParallel(model)

# 清理显存
torch.cuda.empty_cache()

tokenizer = AutoTokenizer.from_pretrained(base_model_name)

while True:
    input_text = input()

    if input_text == "exit" or input_text == "quit" or input_text == "bye":
        break
    inputs = tokenizer(input_text, return_tensors="pt").to(device)

    # 创建流式输出器
    streamer = TextStreamer(tokenizer)

    # 生成输出，使用流式输出器
    output = model.module.generate(**inputs, max_length=1000, num_return_sequences=1, streamer=streamer)

    # 打印到控制台
    while True:
        try:
            print(streamer.tokenizer.decode(streamer.tokens_seen), end="")
            streamer.flush()
        except BrokenPipeError:
            break