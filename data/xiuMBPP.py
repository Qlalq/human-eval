import json

def process_file():
    data_list = []
    with open('MBPP.jsonl', 'r') as file:
        for line in file:
            data = json.loads(line)
            prompt = data['prompt']
            code = data['code']
            function_name = code.split(':')[0].strip()
            updated_prompt = f"{prompt} The beginning of the generated content is as follows: {function_name}"
            data['prompt'] = updated_prompt
            data_list.append(data)

    with open('MBPP.jsonl', 'w') as file:
        for data in data_list:
            file.write(json.dumps(data) + '\n')

process_file()