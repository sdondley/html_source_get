import subprocess
import os
import sys

# Get the article html
def get_html(url=None):
    script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "applescripts")

    if url:
        script_file = 'fetch_html.osa'
        script_path = os.path.join(script_dir, script_file)
        result = subprocess.run([script_path, url], capture_output=True, text=True)
    else:
        script_file = 'safari_grab_source.osa'
        script_path = os.path.join(script_dir, script_file)
        result = subprocess.run([script_path], capture_output=True, text=True)

    return result.stdout
