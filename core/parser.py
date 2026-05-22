import ast
import os


def extract_python_functions(repo_path):

    parsed_data = []

    for root, _, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):

                file_path = os.path.join(root, file)

                try:

                    with open(file_path, "r", encoding="utf-8") as f:
                        source = f.read()

                    tree = ast.parse(source)

                    for node in ast.walk(tree):

                        # Extract functions
                        if isinstance(node, ast.FunctionDef):

                            parsed_data.append({
                                "type": "function",
                                "name": node.name,
                                "file": file_path,
                                "line": node.lineno,
                                "code": ast.get_source_segment(source, node)
                            })

                        # Extract classes
                        elif isinstance(node, ast.ClassDef):

                            parsed_data.append({
                                "type": "class",
                                "name": node.name,
                                "file": file_path,
                                "line": node.lineno,
                                "code": ast.get_source_segment(source, node)
                            })

                except Exception as e:

                    print(f"Error parsing {file_path}: {e}")

    return parsed_data