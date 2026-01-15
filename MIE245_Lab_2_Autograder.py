import os
import importlib.util
import pandas as pd
import random

def test_case_insertion(module):
    """ Tests the insertion_sort function inside Sorter class """
    try:
        # 1. Ground truth
        input_data = [64, 34, 25, 12, 22, 11, 90]
        ground_truth = sorted(input_data.copy())

        # 2. Instantiate Student Class
        sorter = module.Sorter()

        # 3. Get candidate result
        # Passing a copy to ensure the student function doesn't modify original for comparison
        candidate_result = sorter.insertion_sort(input_data.copy())

        # 4. Compare
        if candidate_result == ground_truth:
            return 1
        return 0
    except Exception as e:
        # print(f"Debug - Insertion Sort Error: {e}") # Uncomment for debugging
        return 0

def test_case_merge(module):
    """ Tests the merge_sort function inside Sorter class """
    try:
        # 1. Ground truth
        input_data = [38, 27, 43, 3, 9, 82, 10]
        ground_truth = sorted(input_data.copy())

        # 2. Instantiate Student Class
        sorter = module.Sorter()

        # 3. Get candidate result
        candidate_result = sorter.merge_sort(input_data.copy())

        # 4. Compare
        if candidate_result == ground_truth:
            return 1
        return 0
    except Exception as e:
        # print(f"Debug - Merge Sort Error: {e}") # Uncomment for debugging
        return 0

def main():
    path = "submissions" 
    # Ensure the submissions directory exists
    if not os.path.exists(path):
        print(f"Error: '{path}' directory not found.")
        return

    files = list(os.listdir(path))

    all_grades = []
    for file in files:
        if 'MIE245_Lab_2_' in file:
            utorid = file[:-3].split("_")[-1]
            # Grade list: [utorid, insertion_score, merge_score]
            student_grades = [utorid]

            module_name = file.split("/")[-1].split(".")[0]
            module_path = os.path.join(path, file)

            try:
                # Dynamic import
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Run Tests
                student_grades.append(test_case_insertion(module))
                student_grades.append(test_case_merge(module))

                # Console output for feedback
                if student_grades[1] != 1 or student_grades[2] != 1:
                    print(f"Fail: {utorid} -> Insertion: {student_grades[1]}, Merge: {student_grades[2]}")

            except Exception as e:
                student_grades.extend([0, 0])
                print(utorid, 0, "except", f"utorid: {utorid}", e)

            all_grades.append(student_grades)
        else:
            if file != ".DS_Store": 
                print('Skipping file: ', file)

    path_csv = "grades.csv"
    pd.DataFrame(all_grades).to_csv(path_csv, header=False, index=False)
    print("Grading complete. Results saved to grades.csv")

if __name__ == '__main__':
    main()
