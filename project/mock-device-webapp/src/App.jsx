// TODO: Implement ESP32-CAM Device Simulator
import { useState, useEffect } from 'react'

const DeviceState = {
  OFF: 'off',
  BOOTING: 'booting',
  CAPTURING: 'capturing',
  CONNECTING_WIFI: 'connecting_wifi',
  SENDING: 'sending',
  IDLE: 'idle'
}

function App() {
  const [state, setState] = useState(DeviceState.OFF)
  const [eventLog, setEventLog] = useState([])
  const [photoCount, setPhotoCount] = useState(0)
  const [uptime, setUptime] = useState(0)
  const [duration, setDuration] = useState(60)
  const [wifiFailure, setWifiFailure] = useState(false)

  const activateAlarm = async () => {
    addLog('Power ON - Alarm activated')
    setState(DeviceState.BOOTING)
    // TODO: Implement full state machine
  }

  const stopAlarm = () => {
    addLog('Power OFF - Alarm stopped')
    setState(DeviceState.OFF)
    setPhotoCount(0)
    setUptime(0)
  }

  const addLog = (message) => {
    const timestamp = new Date().toLocaleTimeString()
    setEventLog(prev => [...prev, `[${timestamp}] ${message}`])
  }

  return (
    <div className="min-h-screen bg-[#1a1a2e] text-white p-6">
      <div className="max-w-2xl mx-auto">
        {/* Header */}
        <div className="bg-[#16213e] rounded-lg p-4 mb-6">
          <h1 className="text-xl font-bold flex items-center gap-2">
            🔌 MOCK ESP32-CAM DEVICE SIMULATOR
          </h1>
          <p className="text-gray-400">
            Device: SW-MOCK-001 | Status:{' '}
            <span className={state === DeviceState.OFF ? 'text-red-500' : 'text-green-500'}>
              {state === DeviceState.OFF ? '⚫ POWERED OFF' : '🟢 POWERED ON'}
            </span>
          </p>
        </div>

        {/* Device State */}
        <div className="bg-[#16213e] rounded-lg p-4 mb-6">
          <h2 className="text-lg font-semibold mb-4">DEVICE STATE</h2>
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div>Power: {state === DeviceState.OFF ? '⚫ OFF' : '🟢 ON'}</div>
            <div>State: {state.toUpperCase()}</div>
            <div>WiFi: {state === DeviceState.OFF ? 'Not connected' : 'Connected'}</div>
            <div>Photos: {photoCount} captured</div>
            <div>Uptime: {uptime}s</div>
          </div>
        </div>

        {/* Controls */}
        <div className="bg-[#16213e] rounded-lg p-4 mb-6">
          <h2 className="text-lg font-semibold mb-4">CONTROLS</h2>
          <div className="flex gap-4 mb-4">
            <button
              onClick={activateAlarm}
              disabled={state !== DeviceState.OFF}
              className="bg-red-600 hover:bg-red-700 disabled:bg-gray-600 px-4 py-2 rounded font-semibold"
            >
              🔔 ACTIVATE ALARM
            </button>
            <button
              onClick={stopAlarm}
              disabled={state === DeviceState.OFF}
              className="bg-gray-600 hover:bg-gray-700 disabled:bg-gray-800 px-4 py-2 rounded font-semibold"
            >
              ⏹️ STOP ALARM
            </button>
          </div>
          <div className="flex items-center gap-4 mb-4">
            <label>Duration:</label>
            <input
              type="number"
              value={duration}
              onChange={(e) => setDuration(Number(e.target.value))}
              className="bg-[#0f3460] px-3 py-1 rounded w-24 text-center"
            />
            <span>seconds</span>
          </div>
          <label className="flex items-center gap-2">
            <input
              type="checkbox"
              checked={wifiFailure}
              onChange={(e) => setWifiFailure(e.target.checked)}
              className="rounded"
            />
            Simulate WiFi failure (use backup)
          </label>
        </div>

        {/* Event Log */}
        <div className="bg-[#16213e] rounded-lg p-4 mb-6">
          <h2 className="text-lg font-semibold mb-4">EVENT LOG</h2>
          <div className="bg-[#0f3460] rounded p-3 h-48 overflow-y-auto font-mono text-sm">
            {eventLog.length === 0 ? (
              <p className="text-gray-500">No events yet...</p>
            ) : (
              eventLog.map((log, i) => <div key={i}>{log}</div>)
            )}
          </div>
        </div>

        {/* Camera Preview */}
        <div className="bg-[#16213e] rounded-lg p-4">
          <h2 className="text-lg font-semibold mb-4">CAMERA PREVIEW (Last Capture)</h2>
          <div className="bg-[#0f3460] rounded p-4 text-center text-gray-500">
            No photo captured yet
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
