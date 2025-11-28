import os
import requests

AIP_KEY = os.getenv("AIPIPE_API_KEY")

def run_code(code: str):
    try:
        response = requests.post(
            "https://api.aipipe.ai/v1/run",
            json={"code": code},
            headers={"Authorization": f"Bearer {AIP_KEY}"}
        )
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}
