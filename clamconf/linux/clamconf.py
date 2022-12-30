import clamd
import freshclam

print("This will setup the configuration files for clamav as needed.")
print("Please note this was designed for my Windows use, but should work on Linux after editing global variables. Make no guarantee.")
print("1. Open clamd and freshclam. sample configuration files")
print("2. Searches the files for the 'Example' text and remove it (otherwise clamav thinks its not setup and refuses to run).")
print("3. Resaves the sample files under the main directory with the conf file type as clamav expects.")
