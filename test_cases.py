import os

def test_files(file_extension : str, directory: str, search_word : str) -> list:
    '''
    function to calculate  store all test files. files are found using key word test
    @param: file_extension - specifies file extension e.g java
    @param: directory -  specifies the search directory
    @param: search_word - word that identifies file to search for, e.g any file that contains word "test"
    '''
    test_files = []
    for root, subdirectories, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                #current_file = os.path.join(subdirectory, file)
                file_path = str(os.path.abspath(file))
                if search_word in file_path.lower():
                    test_files.append(file_path.lower())
    return test_files


def test_cases(files: list, search_word : str) -> int:
    '''
    function to calculate the number of test cases, test cases are identified by the key word @Test
    @param: files - list of all files contain  tests found through the method -> test_files
    @param: search_word -  specifies the search word for determining a test case e.g @Test
    '''
    no_of_test_cases = 0
    for file in files:
        with open(file, encoding='utf-8') as f:
            for line in f:
                if search_word.lower() in line.lower():
                    no_of_test_cases += 1
        f.close()
    return no_of_test_cases 

if __name__ == '__main__':
    file_ext = ".java"
    test_search_word = "test"
    test_case_search_word = "@Test"
    search_dir = input('Enter Directory to search: ')
    test_source_files = test_files(file_ext, search_dir , test_search_word)
    source_test_cases = test_cases(test_source_files, test_case_search_word)
    print(f'Total Test Cases: {source_test_cases}')
