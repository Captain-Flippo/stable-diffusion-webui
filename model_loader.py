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
    url: str
    file: str

MODELS = [
#    Model("Protogen", "https://huggingface.co/darkstorm2150/Protogen_x5.8_Official_Release", "ProtoGen_X5.8.safetensors"),
    Model("Cyberrealistic", "https://huggingface.co/ckpt/CyberRealistic", "cyberrealistic_v13.safetensors"),
#    Model("Dreamlike-Photoreal", "https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0", "dreamlike-photoreal-2.0.saftensors"),
#    Model("Ghibli-Diffusion", "https://huggingface.co/nitrosocke/Ghibli-Diffusion", "ghibli-diffusion-v1.ckpt"),
#    Model("3D-Render-Style", "https://huggingface.co/goofyai/3d_render_style_xl", "3d_render_style_xl.safetensors"),
#    Model("Elden-Ring-Diffusion", "https://huggingface.co/nitrosocke/elden-ring-diffusion", "eldenRing-v3-pruned.ckpt"),
#    Model("QR-Code-Monster", "https://huggingface.co/monster-labs/control_v1p_sd15_qrcode_monster", "control_v1p_sd15_qrcode_monster.safetensors"),
#    Model("Realistic-Vision", "https://huggingface.co/SG161222/Realistic_Vision_V5.1_noVAE", ""),
]

for model in MODELS:
    #start subprocess to download model
    subprocess.run(["git", "clone", "--depth", "1", model.url])
    #copy model to models folder
    model_path = Path(home , "models", model.url.split("/")[-1], model.file)
    subprocess.run(["cp", model_path, home+"/stable_diffusion-webui/models/Stable-diffusion/"+model.file])
    if REMOVE_MODELS:
        #remove model folder
        subprocess.run(["rm", "-rf", model.name])

os.chdir(home)