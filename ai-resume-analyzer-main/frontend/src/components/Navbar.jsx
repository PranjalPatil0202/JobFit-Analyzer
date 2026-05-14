import { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { BsStars } from 'react-icons/bs';

const Navbar = () => {
  const [scrolled, setScrolled] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();

  // Get token to check authentication status
  const token = localStorage.getItem('access_token');

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);

    window.addEventListener('scroll', handleScroll);

    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    navigate('/login');
  };

  return (
    <nav className={`modern-navbar ${scrolled ? 'scrolled' : ''}`}>

      {/* Logo */}
      <div className="nav-brand">
        <Link to="/">
          <BsStars className="brand-icon" />
          <span>JobFit Analyzer</span>
        </Link>
      </div>

      {/* Navigation Links */}
      <div className="nav-menu">

        <Link
          to="/"
          className={location.pathname === '/' ? 'active' : ''}
        >
          Home
        </Link>

        <a href="/#features">
          Features
        </a>

        {/* Dashboard Link Logic */}
        <Link
          to="/dashboard"
          className={location.pathname === '/dashboard' ? 'active' : ''}
        >
          Dashboard
        </Link>

      </div>

      {/* Action Buttons */}
      <div className="nav-actions">

        {token ? (
          <button onClick={handleLogout} className="btn-ghost" style={{ border: 'none', cursor: 'pointer', fontFamily: 'inherit', fontSize: '0.95rem' }}>
            Logout
          </button>
        ) : (
          <>
            <Link to="/login" className="btn-ghost">
              Login
            </Link>

            <Link to="/register" className="btn-primary-glow small">
              Register
            </Link>
          </>
        )}

      </div>
    </nav>
  );
};

export default Navbar;