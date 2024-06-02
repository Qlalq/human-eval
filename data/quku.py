import json

# 读取文件
with open('MBPP_samples.jsonl', 'r') as file:
    lines = file.readlines()

# 处理每一行
for i in range(len(lines)):
    line = lines[i].strip()
    if line:  # 检查行是否为空
        try:
            data = json.loads(line)
            if 'completion' in data:
                # 删除第一次出现"def"前的所有字符
                data['completion'] = data['completion'].split('def', 1)[-1]
                # 重新添加"def"，因为split操作会删除它
                data['completion'] = 'def' + data['completion']
            lines[i] = json.dumps(data)
        except json.JSONDecodeError:
            print(f"Line {i+1} is not a valid JSON object.")

# 写回文件
with open('MBPP_samples.jsonl', 'w') as file:
    file.write('\n'.join(lines))