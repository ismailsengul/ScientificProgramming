import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function getMessage() {
  axios.get('http://localhost:8000/hello') 
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.error(error);
    });
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>

        <button onClick={getMessage}>Click me</button>
      </header>
    </div>
  );
}

export default App;
