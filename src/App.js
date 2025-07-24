import React, { useState } from 'react';
import Login from './components/Login/Login';
import ItemList from './components/ItemList/ItemList';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <div className="App">
      {loggedIn ? <ItemList /> : <Login onSuccess={() => setLoggedIn(true)} />}
    </div>
  );
}

export default App;
