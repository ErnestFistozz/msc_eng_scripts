import os, csv


def repo_tests_pair_file(app : str, filename = 'test_case_numbers_per_project') -> None:
    csv_file_name = filename + ".csv"
    with open(csv_file_name, "w") as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(["project name", "number of tests"])
        for row in app:
                csv_writer.writerow(row)

class TestCases:
    def __init__(self, parent_dir : str) -> None:
        self.main_dir = parent_dir

    def is_test_file(self, file_name : str) -> bool:
        if file_name.endswith('.java') and file_name.lower().__contains__('test'):
            return True
        return False

    def is_test_directory(self, dir : str) -> bool:
        if os.path.abspath(dir).lower().__contains__('test'):
            return True
        return False

    def file_test_cases(self, test_file : str) -> int:
        with open(test_file, 'r') as f:
            test_count = [line.rstrip() for line in f if line.lower().__contains__('@test')]
        return len(test_count)
    
    def total_number_of_test_cases(self) -> int:
        total_tests = 0
        for subdir, dirs, files in os.walk(self.main_dir):
            for file in files:
                if self.is_test_file(file):
                    total_tests += self.file_test_cases(file)
        return total_tests


if __name__ == '__main__':
    jmeter_tests = TestCases('')
    jmeter_tests.total_number_of_test_cases()