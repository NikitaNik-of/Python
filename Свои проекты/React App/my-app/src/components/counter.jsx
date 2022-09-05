import React from 'react';
import { useState } from 'react';

const Counter = function () {
    const [count, setCount] = useState(69)
    
    function increment() {
        setCount(count + 1)
    }
  
    function decrement(){
        setCount(count - 1)
    }
    

    return(
        <div>
            <h1>{count}</h1>
            <button onClick={increment}>+1</button>
            <button onClick={decrement}>-1</button>
        </div>
    )
}

export default Counter;