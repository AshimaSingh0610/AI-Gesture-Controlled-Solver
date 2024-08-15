import os

# Define the project structure
project_structure = {
    "Interactive-Gesture-Controlled-AI-Solver": {
        "src": {
            "model.py": None,
            "training.py": None,
            "inference.py": None,
            "gesture_control": {
                "detector.py": None,
                "processor.py": None,
                "actions.py": None
            }
        },
        "data": {
            "raw": None,
            "processed": None
        },
        "models": {
            "model.h5": None
        },
        "notebooks": {
            "experiments.ipynb": None
        },
        "utils": {
            "helper.py": None
        },
        "config": {
            "config.yaml": None
        },
        "tests": {
            "test_model.py": None
        },
        ".gitignore": None,
        "README.md": None,
        "requirements.txt": None
    }
}

def create_structure(base_path, structure):
    for key, value in structure.items():
        path = os.path.join(base_path, key)
        if isinstance(value, dict):
            # Create directory
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Created directory: {path}")
            # Recursively create files and directories inside
            create_structure(path, value)
        else:
            # Create file
            with open(path, 'w') as f:
                print(f"Created file: {path}")

# Base path for the project
base_path = os.path.join(os.getcwd(), "Interactive-Gesture-Controlled-AI-Solver")

# Create the project structure
create_structure(base_path, project_structure)

print("Project structure created successfully.")
