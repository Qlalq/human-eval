#调用API生成samples
from human_eval.data import write_jsonl, read_problems
import openai
from datetime import datetime

openai.api_base = "https://openkey.cloud/v1" # 换成代理，一定要加v1
openai.api_key = "sk-J1AjZiqLWeOQ9MEkA293Be557d8a4021B7A55e7e25F3305e"

#注意：大模型输出会带上def以及函数名，这不影响评测结果
def generate_one_completion(prompt,task_id):
    print(datetime.now().strftime("%H:%M:%S"), "task_id:",task_id) #终端显示当前时间和task_id
    resp= openai.ChatCompletion.create(
                                        model=model_name, 
                                        messages=[
                                        {"role": "system", "content": "Output function code only,without main function and code blocks(like ```python) and any explanation at the outset so that I can call your generated functions directly\n"},
                                        {"role": "user", "content": prompt}
                                        ])
    res = resp.choices[0].message.content
    print(res)
    return res


if __name__ == '__main__':
    # problems = read_problems("D:\computer_programming_language\VScode\VS code file\python\human-eval\data\MBPP.jsonl")
    problems = read_problems()#无参默认读取Humaneval的164条数据
    model_name = "gpt-3.5-turbo" # 模型名称，正式评测建议用gpt-4o
    num_samples_per_task = 1 # 循环生成答案 Pass@1 对应为1
    samples = [
        dict(task_id=task_id, completion=generate_one_completion(problems[task_id]["prompt"],task_id))
        for task_id in problems
        for _ in range(num_samples_per_task)
    ]
    write_jsonl(f"{model_name}_samples.jsonl", samples)#调整了命名顺序，使其不会覆盖我提供的结果文件