
import React, { useState } from 'react';

function App() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    setResponse('');
    try {
      const res = await fetch('http://localhost:5000/prompt', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });
      const data = await res.json();
      setResponse(data.prompt_response || data.error);
    } catch (err) {
      setResponse('Error: ' + err.message);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: 20, fontFamily: 'Arial' }}>
      <h2>Ask Titan About anything you Need</h2>
      <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter a prompt"
        style={{ padding: 8, width: '60%' }}
      />
      <button onClick={handleSubmit} style={{ marginLeft: 10, padding: 8 }}>
        Ask Titan
      </button>
      <div style={{ marginTop: 20 }}>
        {loading ? 'Thinking...' : <strong>{response}</strong>}
      </div>
    </div>
  );
}

export default App;
