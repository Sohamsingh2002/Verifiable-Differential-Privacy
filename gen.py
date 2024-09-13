import yaml

# Define the requirements
requirements = {
    'python': '>=3.7',
    'libraries': {
        'numpy': '==1.20.3',
        'sqlparse': '==0.4.2',
        'matplotlib': '==3.4.2',
        'pandas': '==1.2.4',
        'scipy': '==1.6.3',
        'hashlib': None,
        'os': None,
        're': None
    }
}

# Write the requirements to a YAML file
with open('requirements.yml', 'w') as file:
    yaml.dump(requirements, file, default_flow_style=False)

print("YAML file generated successfully: requirements.yml")
