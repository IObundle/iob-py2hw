import os
import importlib

def run_unit_tests():
    # Get a list of all Python files in the current directory
    files = [file for file in os.listdir('.') if file.endswith('.py')]

    for file in files:
        # Exclude the current file (iob_tests.py) from being imported
        if file != 'iob_tests.py':
            module_name = file[:-3]  # Remove the '.py' extension to get the module name
            module = importlib.import_module(module_name)
            
            # Check if the module has a 'unit_test' function and call it if present
            if hasattr(module, 'unit_test') and callable(module.unit_test):
                print(f"Running unit tests for {module_name}")
                module.unit_test()
                print()

if __name__ == "__main__":
    run_unit_tests()

