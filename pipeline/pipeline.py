import boto3
from os import getenv
from sys import argv
from tqdm import tqdm
from omegaconf import OmegaConf
from pathlib import Path

cwd = Path(__file__).parent
conf = OmegaConf.load(Path(cwd, "config.yaml"))

# Create a cloudformation client
client = boto3.client('cloudformation')

# Create a stack
response = client.create_stack(TemplateBody=str(Path(cwd, "cloudformation", conf.cloudformation.template)), StackName=conf.cloudformation.stack_name)
print(response)