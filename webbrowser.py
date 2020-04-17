import subproccess
url = input("enter url:")
list_files = subprocess.run(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "",  url ])
print("The exit code was: %d" % list_files.returncode)
#upload to target machine 
#access shell on target machine 
#run the exploit or payload on target machine in the shell
