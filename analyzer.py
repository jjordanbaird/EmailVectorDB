import ast
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PythonCodeAnalyzer:
    def __init__(self, directory=None, output_path=None):
        self.directory = directory or os.getcwd()
        self.output_path = output_path or "output.txt"

    def get_arg_data_type(self, arg):
        if arg.annotation:
            return ast.unparse(arg.annotation)
        else:
            return ""

    def get_classes_and_methods(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            file_contents = f.read()

        module = ast.parse(file_contents)
        classes_and_methods = {}

        for node in module.body:
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                bases = [ast.unparse(base) for base in node.bases]
                class_docstring = ast.get_docstring(node)

                method_data = {}
                for n in node.body:
                    if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        method_name = n.name
                        args = [(arg.arg, self.get_arg_data_type(arg)) for arg in n.args.args]
                        return_data_type = ast.unparse(n.returns) if n.returns else "Unknown"
                        method_docstring = ast.get_docstring(n)

                        method_data[method_name] = {
                            "args": args,
                            "return_data_type": return_data_type,
                            "docstring": method_docstring
                        }

                classes_and_methods[class_name] = {
                    "bases": bases,
                    "docstring": class_docstring,
                    "methods": method_data
                }

        return classes_and_methods



    def analyze_directory(self):
        python_files = []
        for root, dirnames, files in os.walk(self.directory):
            for file in files:
                if file.endswith(".py"):
                    python_files.append(os.path.join(root, file))

        logger.debug(f"Python files found: {python_files}")

        result = {}
        for file_path in python_files:
            try:
                classes_and_methods = self.get_classes_and_methods(file_path)
                if classes_and_methods:
                    result[file_path] = classes_and_methods
            except Exception as e:
                logger.error(f"Error analyzing file {file_path}: {e}")

        return result

    def save_results(self, results):
        with open(self.output_path, 'w', encoding='utf-8') as f:
            for file_path, classes_and_methods in results.items():
                f.write(f"File: {os.path.relpath(file_path, os.path.dirname(os.getcwd()))}\n")
                for class_name, class_data in classes_and_methods.items():
                    f.write(f"  Class: {class_name}\n")
                    f.write(f"    Inherits from: {', '.join(class_data['bases'])}\n")
                    f.write(f"    Docstring: {class_data['docstring']}\n")
                    for method_name, method_data in class_data['methods'].items():
                        f.write(f"    Method: {method_name}\n")
                        for arg_name, arg_data_type in method_data['args']:
                            if arg_data_type:
                                f.write(f"      Arg: {arg_name} ({arg_data_type})\n")
                            else:
                                f.write(f"      Arg: {arg_name}\n")
                        f.write(f"      Returns: {method_data['return_data_type']}\n")
                        f.write(f"      Docstring: {method_data['docstring']}\n")


    def analyze_and_save(self):
        results = self.analyze_directory()
        logger.debug(f"Analysis results: {results}")
        self.save_results(results)

# Usage example
analyzer = PythonCodeAnalyzer(output_path="output.txt")
analyzer.analyze_and_save()
