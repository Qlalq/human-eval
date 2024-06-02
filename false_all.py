import json

with open('samples_GPT4o_results.jsonl', 'r') as file:
    lines = file.readlines()

false_samples = [json.loads(line) for line in lines if json.loads(line)['passed'] == False]
#HE_false（手标）.txt里有我手动标注的错误原因，所以下面生成的文件名是Humaneval_false.txt，不要覆盖
with open('Humaneval_false.txt', 'w') as file:
    for sample in false_samples:
        # 将\\n替换为\n
        sample = json.dumps(sample).replace("\\n", "\n")
        file.write(sample + '\n'+"-----------------------------------------------------------"+'\n')