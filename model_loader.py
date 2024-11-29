# This script downloads stable diffusion models from huggingface with git-lfs and loads them into the model directory.
# The models are preferably downloaded as savetensor

from pathlib import Path
import os
import subprocess
from dataclasses import dataclass

home = "/home/ubuntu"
REMOVE_MODELS = False

os.chdir(home)
if "models" not in os.listdir():
    os.mkdir("models")
os.chdir("models")

@dataclass
class Model:
    name: str
    host: str
    url: str

MODELS = [
    # Model("Protogen", "huggingface", "https://huggingface.co/darkstorm2150/Protogen_x5.8_Official_Release"),
    Model("Cyberrealistic", "huggingface", "https://huggingface.co/ckpt/CyberRealistic"),
    # Model("Dreamlike-Photoreal", "huggingface", "https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0"),
    # Model("Ghibli-Diffusion", "huggingface", "https://huggingface.co/nitrosocke/Ghibli-Diffusion"),
    # Model("3D-Render-Style", "huggingface", "https://huggingface.co/goofyai/3d_render_style_xl"),
    # Model("Elden-Ring-Diffusion", "huggingface", "https://huggingface.co/nitrosocke/elden-ring-diffusion"),
    # Model("QR-Code-Monster", "huggingface", "https://huggingface.co/monster-labs/control_v1p_sd15_qrcode_monster"),
    # Model("Realistic-Vision", "huggingface", "https://huggingface.co/SG161222/Realistic_Vision_V5.1_noVAE", ""),
    Model("BigASP", "civitai", "https://civitai.com/api/download/models/991916?type=Model&format=SafeTensor&size=pruned&fp=fp16")
]

for model in MODELS:
    #start subprocess to download model
    if model.host == "huggingface":
        subprocess.run(["git", "clone", "--depth", "1", model.url])
    if model.host == "civitai":
        os.makedirs(model.name, exist_ok=True)
        subprocess.run(["wget", "-O", f"{model.name}/{model.name}.safetensors", model.url])
    #copy model to models folder
    model_path = Path(home , "models", model.url.split("/")[-1], model.file)
    subprocess.run(["cp", model_path, home+"/stable_diffusion-webui/models/Stable-diffusion/"+model.file])
    if REMOVE_MODELS:
        #remove model folder
        subprocess.run(["rm", "-rf", model.name])

os.chdir(home)