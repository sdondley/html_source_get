import subprocess

# Get the article html
def get_the_html(url=None):
    if url:
        script_path = '../applescripts/fetch_html.osa'
        result = subprocess.run([script_path, url], capture_output=True, text=True)
    else:
        script_path = '../applescripts/safari_grab_source.osa'
        result = subprocess.run([script_path], capture_output=True, text=True)

    return result.stdout
