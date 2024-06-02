import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from human_eval.data import write_jsonl, read_problems
import requests
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
def generate_one_completion(prompt: str):
    torch.set_default_device("cuda")
    tokenizer = AutoTokenizer.from_pretrained("epfl-llm/meditron-70b")
    model = AutoModelForCausalLM.from_pretrained("epfl-llm/meditron-70b")
    
    inputs = tokenizer(prompt, return_tensors="pt", return_attention_mask=False)
    outputs = model.generate(**inputs, max_length=200, temperature=0.8, do_sample=True)
    completion = tokenizer.batch_decode(outputs)[0]
    
    return completion

problems = read_problems("data/human-eval-v2-20210705.jsonl")

num_samples_per_task = 200
samples = [
    dict(task_id=task_id, completion=generate_one_completion(problems[task_id]["prompt"]))
    for task_id in problems
    for _ in range(num_samples_per_task)
]
write_jsonl("samples.jsonl", samples)