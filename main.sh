# Start the server.py script and wait for it to initialize
python3 autoMoving/server.py &

# Get the process ID of the server
SERVER_PID=$!

# Wait for the server to start (you can adjust the sleep duration as needed)
sleep 5

# Start the navigation.py script
python3 autoMoving/navigation.py &

# Wait for all background processes to finish
wait