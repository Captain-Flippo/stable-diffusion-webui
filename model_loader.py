# This script downloads stable diffusion models from huggingface with git-lfs and loads them into the model directory.
# The models are preferably downloaded as savetensor

from pathlib import Path
import os
import subprocess
from dataclasses import dataclass

home = Path(__file__).parent
os.chdir(home)
os.mkdir("models")
os.chdir("models")

@dataclass
class Model:
    name: str
    url: str
    file: str

MODELS = [
    Model("f222", "https://huggingface.co/acheong08/f222", "f222.safetensors"),
    Model("Protogen_x5.8_Official_Release", "https://huggingface.co/darkstorm2150/Protogen_x5.8_Official_Release", "ProtoGen_X5.8.safetensors"),
]

for model in MODELS:
    #start subprocess to download model
    subprocess.run(["git", "clone", "--depth", "1", model.url])
    #copy model to models folder
    model_path = Path(home, model.name, model.file)
    subprocess.run(["cp", "-r", model_path, "../stable_diffusion-webui/models/Stable-diffusion/"])
    #remove model folder
    subprocess.run(["rm", "-rf", model.name])

os.chdir(home)