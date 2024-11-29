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
    file: str

MODELS = [
    # Model("Protogen", "huggingface", "https://huggingface.co/darkstorm2150/Protogen_x5.8_Official_Release", "ProtoGen_X5.8.safetensors"),
    # Model("Cyberrealistic", "huggingface", "https://huggingface.co/ckpt/CyberRealistic", "cyberrealistic_v13.safetensors"),
    # Model("Dreamlike-Photoreal", "huggingface", "https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0", "dreamlike-photoreal-2.0.saftensors"),
    # Model("Ghibli-Diffusion", "huggingface", "https://huggingface.co/nitrosocke/Ghibli-Diffusion", "ghibli-diffusion-v1.ckpt"),
    # Model("3D-Render-Style", "huggingface", "https://huggingface.co/goofyai/3d_render_style_xl", "3d_render_style_xl.safetensors"),
    # Model("Elden-Ring-Diffusion", "huggingface", "https://huggingface.co/nitrosocke/elden-ring-diffusion", "eldenRing-v3-pruned.ckpt"),
    # Model("QR-Code-Monster", "huggingface", "https://huggingface.co/monster-labs/control_v1p_sd15_qrcode_monster", "control_v1p_sd15_qrcode_monster.safetensors"),
    Model("BigASP", "civitai", "https://civitai.com/api/download/models/991916?type=Model&format=SafeTensor&size=pruned&fp=fp16", "BigASP.safetensors")
]

for model in MODELS:
    #start subprocess to download model
    if model.host == "huggingface":
        subprocess.run(["git", "clone", "--depth", "1", model.url])
    if model.host == "civitai":
        os.makedirs(model.name, exist_ok=True)
        subprocess.run(["wget", "-O", f"{model.name}/{model.file}", model.url])
    # Crawl for all models within the model/**/ folders and copy them into the target directory
    for root, dirs, files in os.walk(home + "/models"):
        for file in files:
            if file.endswith(".safetensors") or file.endswith(".ckpt"):
                source_path = Path(root, file)
                target_path = Path(home, "stable-diffusion-webui/models/Stable-diffusion", file)
                subprocess.run(["cp", source_path, target_path])
    if REMOVE_MODELS:
        #remove model folder
        subprocess.run(["rm", "-rf", model.name])

os.chdir(home)