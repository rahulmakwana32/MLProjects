import os
import getpass
from huggingface_hub import HfApi, login

def main():
    print("🚀 Hugging Face Upload Assistant")
    print("--------------------------------")
    
    # 1. Login
    try:
        # Check if already logged in by trying to get user info (skip if we want to force explicit token usually, but let's try)
        # Actually easier to just ask for token if not found or just ask always for this script
        print("Please enter your Hugging Face Access Token (Write permission required).")
        print("You can find it here: https://huggingface.co/settings/tokens")
        token = getpass.getpass("Token: ").strip()
        if not token:
            print("Token is required!")
            return
        
        login(token=token)
        api = HfApi()
        user_info = api.whoami(token=token)
        username = user_info['name']
        print(f"✅ Logged in as: {username}")
        
    except Exception as e:
        print(f"❌ Login failed: {e}")
        return

    # 2. Repo Details
    default_repo_name = "service-now-incident-risk-prediction"
    repo_name = input(f"Enter new repository name (default: {default_repo_name}): ").strip() or default_repo_name
    repo_id = f"{username}/{repo_name}"
    
    # 3. Create Repo
    try:
        print(f"Creating repository: {repo_id}...")
        api.create_repo(repo_id=repo_id, repo_type="model", exist_ok=True)
        print("✅ Repository ready.")
    except Exception as e:
        print(f"❌ Failed to create repo: {e}")
        return

    # 4. Prepare Files (Update README with metadata)
    readme_path = "README.md"
    metadata = f"""---
license: mit
library_name: sklearn
tags:
- linear-regression
- tabular-classification
- service-now
- risk-prediction
---
"""
    # Check if metadata already exists
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith("---"):
        print("Adding YAML metadata to README.md...")
        new_content = metadata + content
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    # 5. Upload
    print(f"Uploading files to {repo_id}...")
    try:
        api.upload_folder(
            folder_path=".",
            repo_id=repo_id,
            repo_type="model",
            ignore_patterns=["*.py", "__pycache__", ".ipynb_checkpoints", ".DS_Store"], # Upload everything except scripts and junk
            commit_message="Upload model and notebook"
        )
        print(f"✅ Upload Complete! View your model here: https://huggingface.co/{repo_id}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    main()
