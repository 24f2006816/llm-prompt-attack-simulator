from ai_pipe import Client
import os
import tempfile
import subprocess

client = Client(api_key=os.getenv("AIPIPE_API_KEY"))

def run_code(code: str):
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as temp:
            temp.write(code)
            temp_path = temp.name

        result = subprocess.run(
            ["python", temp_path],
            capture_output=True,
            text=True
        )

        return {
            "success": True,
            "output": result.stdout + result.stderr
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
