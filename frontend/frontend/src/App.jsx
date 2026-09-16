import { useState,useEffect } from 'react'
import './App.css'

function App() {
  const [backendStatus, setBackendStatus] = useState("");
  
  async function health(){
    const response = await fetch('http://127.0.0.1:8000/health')
    return response.json();
  }

  useEffect(()=>{
    health().then(data=>{
      setBackendStatus(data.status)
    })
  },[]);

  return (
    <>
      <title>Planner V1</title>
      <h1>Frontend is running</h1>
      <p>{`Backend : ${backendStatus}`}</p>
    </>
  )
}

export default App
