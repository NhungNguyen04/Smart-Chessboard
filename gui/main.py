import subprocess
import time

# Run socket server
subprocess.Popen(['python', 'socket_server.py'])

# Wait for a moment to ensure the socket server is running
time.sleep(2)

# Run GUI
subprocess.Popen(['python', 'gui.py'])

