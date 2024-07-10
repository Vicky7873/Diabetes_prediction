import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src",
    os.path.join(".github", "workflows")
]

for dirs_ in dirs:
    os.makedirs(dirs_, exist_ok=True)
    with open(os.path.join(dirs_, ".gitkeep"), "w") as f:
        pass

files = [
    os.path.join("src", "__init__.py"),
    "params.yaml",
    "dvc.yaml",
    ".gitignore"
]

for files_ in files:
    with open (files_, "w") as f:
        pass