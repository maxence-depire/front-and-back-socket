import React, { useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import { io } from "socket.io-client"

function App() {
  
  useEffect(() => {
    const socket = io("localhost:5000", {
      transports: ["websocket"],
      cors: {
        origin: "http://localhost:3000/"
      }
    })

    socket.on("connect", (data) => {
      console.log(data)
    })

  })

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        
        <button>Submit.</button>
      </header>
    </div>
  );
}

export default App;
