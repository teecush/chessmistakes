#!/bin/bash

# Navigate to the stockfish_viewer directory
cd "$(dirname "$0")"

echo "🚀 Starting Stockfish Analysis Viewer Server..."
echo "This will start a local server to properly load the CSV data"
echo ""

# Start the Python HTTP server
python3 -m http.server 8080 &
SERVER_PID=$!

# Wait a moment for server to start
sleep 2

# Open the browser
open http://localhost:8080/stockfish_analysis_viewer.html

echo ""
echo "✅ Server started successfully!"
echo "🌐 Viewer opened in your browser"
echo ""
echo "To stop the server, run: kill $SERVER_PID"
echo "Or simply close this terminal window"
echo ""
echo "Manual access: http://localhost:8080/stockfish_analysis_viewer.html" 