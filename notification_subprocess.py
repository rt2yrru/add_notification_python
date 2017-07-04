import subprocess
def update:
    _comamnd="sudo apt update"
    get_info = subprocess.Popen(["/bin/bash", "-c", _command], stdout=subprocess.PIPE)
    return get_info
 _msg=str(update)   
subprocess.Popen(["/bin/bash", "-c", _msg])
