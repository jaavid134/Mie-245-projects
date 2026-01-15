import os
import importlib.util
import io
import contextlib
import pandas as pd


def test_case_1(module):
    # ground truth
    ground_truth = [2, 1]

    # build instance
    candidate_list = module.LinkedList()
    candidate_list.insert_start(1)
    candidate_list.insert_start(2)

    # get candidate
    candidate_order = get_candidate_order(candidate_list)

    if (candidate_order == ground_truth) and candidate_list.tail.value == ground_truth[len(ground_truth)-1] and candidate_list.head.value == ground_truth[0]:
        return 1
    return 0


def get_candidate_order(linked_list):
    current = linked_list.head
    candidate_order = []
    while current:
        candidate_order.append(int(current.value))
        current = current.next
    return candidate_order


def main():
    path = "submissions" 
    files = list(os.listdir(path))

    all_grades = []
    for file in files:
        if 'MIE245_Lab_1_' in file:
            utorid = file[:-3].split("_")[-1]
            test_case_grades = [utorid]

            module_name = file.split("/")[-1].split(".")[0]
            module_path = path + "." + module_name

            try:
                module = importlib.import_module(module_path)
                test_case_grades.append(test_case_1(module))
                if test_case_grades[-1] != 1:
                    print(utorid, test_case_grades[-1])
            except Exception as e:
                test_case_grades.append(0)
                print(utorid, 0, "except", f"utorid: {utorid}", e)

            all_grades.append(test_case_grades)
        else:
            print('Skipping file: ', file)

    path_csv = "grades.csv"
    pd.DataFrame(all_grades).to_csv(path_csv, header = False, index = False)

if __name__ == '__main__':
    main()

