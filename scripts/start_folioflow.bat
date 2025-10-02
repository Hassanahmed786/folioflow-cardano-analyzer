@echo off
echo Starting FolioFlow Masumi Agent...
echo.

echo Starting Flask backend...
start "FolioFlow Backend" /MIN python backend\masumi_agent.py

echo Waiting for backend to start...
timeout /t 5

echo Starting frontend server...
cd frontend
start "FolioFlow Frontend" /MIN python -m http.server 8000
cd ..

echo.
echo ✅ FolioFlow is now running!
echo 🌐 Frontend: http://localhost:8000
echo 🤖 Agent API: http://localhost:5000/agent/capabilities
echo 🔍 Health Check: http://localhost:5000/health
echo.
echo Press any key to open the application in your browser...
pause > nul

start http://localhost:8000

echo.
echo Press any key to stop all services...
pause > nul

taskkill /f /im python.exe /t > nul 2>&1
echo Services stopped.
pause