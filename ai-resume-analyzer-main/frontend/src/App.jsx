import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import Home from './pages/Home';
import Navbar from './components/Navbar';
import PrivateRoute from './components/PrivateRoute';
import './index.css'; 

const App = () => {
  return (
    <Router>
      <div className="app-container">
        <Navbar />
        
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/dashboard" element={
              <PrivateRoute>
                <div className="page-wrapper">
                  <Dashboard />
                </div>
              </PrivateRoute>
            } />
            <Route path="/login" element={<div className="page-wrapper"><Login /></div>} />
            <Route path="/register" element={<div className="page-wrapper"><Register /></div>} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;
