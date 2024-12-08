import './App.css';
import Home from './pages/Home';
import {Routes, Route, BrowserRouter as Router} from "react-router-dom";
import ImageUploader from './pages/ImageUpload';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home/>}></Route>
        <Route path="/ImageUpload" element={<ImageUploader/>}></Route>
      </Routes>
    </Router>
  );
}

export default App;
