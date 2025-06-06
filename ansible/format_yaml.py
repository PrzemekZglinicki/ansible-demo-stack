# format_yaml.py
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO
import glob

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True
yaml.width = 80
yaml.explicit_start = True

def force_block_style(data):
    """
    Recursively convert nested dicts inside lists to block style.
    """
    if isinstance(data, list):
        for item in data:
            force_block_style(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                value.fa.set_block_style()
                force_block_style(value)
            elif isinstance(value, list):
                force_block_style(value)

for path in glob.glob("**/*.yml", recursive=True):
    print(f"Formatting {path}")
    with open(path, "r") as f:
        data = yaml.load(f)

    # Apply block style to inner mappings
    force_block_style(data)

    with open(path, "w") as f:
        yaml.dump(data, f)
