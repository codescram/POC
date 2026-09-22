import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [counter, setCount] = useState(0)
  let [ msg, setMsg ] = useState("");
  function addValue() {
    if(counter >= 20) {
      setMsg("You reached the maximum limit");
      return;
    }
    setMsg("");
    setCount(counter + 1);
  }
  function subValue() {
    if(counter <= 0) {
      setMsg("You reached the minimum limit");
      return;
    }
    setMsg("");
    setCount(counter - 1);
  }


  return (
    <>
      <h1>Don't Give Up</h1>
      <h3>Counter : {counter}
      <br />
      <span style={{color: "red",fontSize:"12px", height:"12px", display:"block"}}>{msg}</span>
      </h3>
      
      <button onClick={addValue}>
        Add Value
      </button>
      
      <button onClick={subValue} style={{marginLeft:"10px"}}>Remove Value</button>
      <br />
      <br />
      <br />
      <br />
      <button onClick={() => setCount(0)}>Resets</button>
    </>
  )
}

export default App
