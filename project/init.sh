#!/bin/bash
# Smart Witness Development Environment Setup

echo "🚀 Starting Smart Witness Development Environment..."
echo ""

# Kill any existing processes on our ports
echo "⏹️  Stopping any existing services..."
pkill -f "uvicorn" 2>/dev/null || true
pkill -f "vite" 2>/dev/null || true
sleep 2

# Start Backend
echo "🔧 Starting Backend (FastAPI)..."
cd backend
pip install -r requirements.txt --quiet
uvicorn main:app --reload --port 8000 &
cd ..
sleep 3

# Start Mock Device Webapp
echo "📱 Starting Mock Device Simulator..."
cd mock-device-webapp
npm install --silent
npm run dev &
cd ..
sleep 2

# Start Mock Telegram Webapp
echo "💬 Starting Mock Telegram Simulator..."
cd mock-telegram-webapp
npm install --silent
npm run dev &
cd ..
sleep 2

# Start Dashboard
echo "📊 Starting Dashboard..."
cd dashboard
npm install --silent
npm run dev &
cd ..
sleep 2

echo ""
echo "✅ Smart Witness Development Environment Ready!"
echo ""
echo "📍 URLs:"
echo "   Dashboard:           http://localhost:3000"
echo "   Mock Device:         http://localhost:3001"
echo "   Mock Telegram:       http://localhost:3002"
echo "   Backend API:         http://localhost:8000"
echo "   API Docs:            http://localhost:8000/docs"
echo ""
echo "🛑 To stop: pkill -f 'uvicorn|vite'"
