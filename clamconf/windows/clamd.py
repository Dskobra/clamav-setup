oldFile = "C:\\ClamAV\\conf_examples\\clamd.conf.sample"
newFile = "C:\\ClamAV\\clamd.conf"
def config_edit_example_text():
    # Erase the Example text placeholder
    # in order for clamav to read the file. Otherwise
    # complains about config not being edited.
    # Minor issue doing this erases the word Example
    # from the "## Example" line at the top of the config
    # file. config_fix_example adds it back in for cosmetic
    # reasons.
    # Read in the file
    with open(oldFile, 'r') as file:
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('Example', '')

    # Write the file out again
    with open(newFile, 'w') as file:
      file.write(filedata)

def config_fix_example():
    # config_edit_example_text unfortunately
    # also erases the word Example from the comment in the conf file.
    # this adds it back in.
    # Read in the file
    with open(newFile, 'r') as file:
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('##  config file for the Clam AV daemon', '## Example config file for the Clam AV daemon')

    # Write the file out again
    with open(newFile, 'w') as file:
      file.write(filedata)
config_edit_example_text()
config_fix_example()
