from huggingface_hub import snapshot_download
from huggingface_hub import login

login()

# Replace 'facebookresearch/sam3' with the correct repo ID if different
model_path = snapshot_download(repo_id="facebookresearch/sam3")
print(f"SAM 3 model weights downloaded to: {model_path}")