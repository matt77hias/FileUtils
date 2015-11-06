import subprocess

def call(cmd, wait):
    if wait:
        call_and_wait(cmd)
    else:
        call_and_continue(cmd)
      
def call_and_continue(cmd):
    print_execution(cmd)
    subprocess.call(cmd, shell=True)
    
def call_and_wait(cmd):
    print_execution(cmd)
    subprocess.check_call(cmd, shell=True)
    
def print_execution(cmd):
   print('Executing:\n' + cmd + '\n') 