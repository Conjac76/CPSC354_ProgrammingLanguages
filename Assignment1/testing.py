import os
import subprocess

def load_tests(file_path):
    tests = []
    with open(file_path, 'r') as file:
        for line in file:
            name, input, expected_output = line.strip().split(', ')
            tests.append((name, input, expected_output))
    return tests

def run_test(program, input):
    result = subprocess.run(['python3', program, input], capture_output=True, text=True)
    return result.stdout.strip()

def main():
    script_dir = os.path.dirname(__file__)
    tests_path = os.path.join(script_dir, "testing-data.txt")
    tests = load_tests(tests_path)
    for program in os.listdir(os.path.dirname(__file__)):
        for (name, input, expected_output) in tests:
            if program.endswith(f"{name}.py"):
                output = run_test(program, input)
                print(f"{output == expected_output} | {name} | Input: {input} | Expected: {expected_output} | Output: {output}")

if __name__ == "__main__":
    main()
