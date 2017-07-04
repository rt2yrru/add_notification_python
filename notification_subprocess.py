import subprocess
def _update():
    _command="sudo apt update"
    get_info = subprocess.Popen(["/bin/bash", "-c", _command], stdout=subprocess.PIPE)
    return get_info
_msg=str(_update())   
subprocess.Popen(["/bin/bash", "-c", _msg]) 
