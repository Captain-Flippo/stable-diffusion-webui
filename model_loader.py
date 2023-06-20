# This script downloads stable diffusion models from huggingface with git-lfs and loads them into the model directory.
# The models are preferably downloaded as savetensor

from pathlib import Path
import os
import subprocess
from dataclasses import dataclass

home = Path(__file__).parent.parent
REMOVE_MODELS = False

os.chdir(home)
if "models" not in os.listdir():
    os.mkdir("models")
os.chdir("models")

@dataclass
class Model:
    name: str
    url: str
    file: str

MODELS = [
    Model("f222", "https://huggingface.co/acheong08/f222", "f222.safetensors"),
    Model("Protogen", "https://huggingface.co/darkstorm2150/Protogen_x5.8_Official_Release", "ProtoGen_X5.8.safetensors"),
]

for model in MODELS:
    #start subprocess to download model
    subprocess.run(["git", "clone", "--depth", "1", model.url])
    #copy model to models folder
    model_path = Path(home , "models", model.url.split("/")[-1], model.file)
    subprocess.run(["cp", model_path, "stable_diffusion-webui/models/Stable-diffusion/"])
    if REMOVE_MODELS:
        #remove model folder
        subprocess.run(["rm", "-rf", model.name])

os.chdir(home)