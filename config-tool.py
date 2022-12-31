def get_user_input():
    global oldFile
    global newFile
    userInput= input("Please enter your OS (Windows or Linux): ")
    osName = userInput.lower()
    if osName == "linux":
        # set the log to the default linux location
        # this uses the upstream location in /usr/local/etc/

        # Create the freshclam.conf file from the sample file
        oldFile = "//usr//local//etc//freshclam.conf.sample"
        newFile = "//usr//local/etc//freshclam.conf"
        create_config()

        # Create the clamd.conf file from the sample file
        oldFile = "//usr//local//etc//clamd.conf.sample"
        newFile = "//usr//local//etc/clamd.conf"
        create_config()
    elif osName == "windows":
        # Due to permission issues in progam files
        # in windows I assume the install location
        # C:\ClamAV (despite the installer using
        # program files as the default location weirdly)

        # Create the freshclam.conf file from the sample file
        oldFile = "C:\\ClamAV\\conf_examples\\freshclam.conf.sample"
        newFile = "C:\\ClamAV\\freshclam.conf"
        create_config()

        # Create the clamd.conf file from the sample file
        oldFile = "C:\\ClamAV\\conf_examples\\clamd.conf.sample"
        newFile = "C:\\ClamAV\\clamd.conf"
        create_config()
    else:
        print("Unkown OS: ", userInput)
        print("Supported options are only Windows and Linux")
    

def create_config():
    # Erase the Example text placeholder
    # in order for clamav to parse the
    # config files (else complains).
    
    # Read in the file
    with open(oldFile, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('# Comment or remove the line below.\nExample', '# Comment or remove the line below. \n# Example')

    # Write the file out again
    with open(newFile, 'w') as file:
      file.write(filedata)

oldFile = ""
newFile = ""
print("This script edits the clamd and freshclam sample files otherwise clamav complains about unable to parse them.")
print("Only supports Windows/Linux. Linux users please use sudo as this assumes files are under /usr/local/etc")
get_user_input()
