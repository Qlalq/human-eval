#文件功能：将human-eval-v2-20210705.jsonl里的"prompt"和"test"根据"task_id"写入到samples_GPT4o_results.jsonl中（false_all.py再将错误用例汇总）
import json

# 读取human-eval-v2-20210705.jsonl文件（解压HumanEval.jsonl.gz得到）
with open('data/human-eval-v2-20210705.jsonl', 'r') as file:
    tasks = {json.loads(line)['task_id']: json.loads(line) for line in file}

# 读取samples_GPT4o_results.jsonl文件
with open('samples_GPT4o_results.jsonl', 'r') as file:
    samples = [json.loads(line) for line in file]

# 将"prompt"和"test"字段根据"task_id"对应到samples中
for sample in samples:
    task_id = sample['task_id']
    if task_id in tasks:
        sample['prompt'] = tasks[task_id]['prompt']
        sample['test'] = tasks[task_id]['test']

# 将结果写回samples_GPT4o_results.jsonl文件
with open('samples_GPT4o_results.jsonl', 'w') as file:
    for sample in samples:
        file.write(json.dumps(sample) + '\n')