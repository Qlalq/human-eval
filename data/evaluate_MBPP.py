import json
import re
import math
# import Counter
# import remove_dirty_chars
# import check
# import defaultdict
# import recursive_list_sum
# import get_equal
# import ct
# import eulerian_num
# import itemgetter
import collections
from typing import List, Dict

def evaluate_samples(sample_file: str, problem_file: str, result_file: str) -> bool:
    # 从jsonl文件中读取样本和问题
    with open(sample_file, 'r') as f:
        samples = [json.loads(line) for line in f]
    with open(problem_file, 'r') as f:
        problems = [json.loads(line) for line in f]

    # 将问题按照task_id进行索引
    problems_dict = {problem['task_id']: problem for problem in problems}

    results = []
    all_passed = True
    for sample in samples:
        task_id = sample['task_id']
        completion = sample['completion']
        problem = problems_dict[task_id]
        tests = problem['test_list']

        # 对每个样本进行测试
        passed = True
        error_message = ''
        for test in tests:
            try:
                exec(completion)
                exec(test)
            except Exception as e:
                passed = False
                error_message = str(e)
                all_passed = False
                break

        # 将结果存储到结果列表中
        result = {
            'task_id': task_id,
            'passed': passed,
            'error_message': error_message
        }
        results.append(result)

    # 将结果写入到jsonl文件中
    with open(result_file, 'w') as f:
        for result in results:
            f.write(json.dumps(result) + '\n')

    return all_passed

evaluate_samples('MBPP_samples.jsonl', 'MBPP.jsonl', 'MBPP_results.jsonl')