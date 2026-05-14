import { Navigate } from 'react-router-dom';

const PrivateRoute = ({ children }) => {

  // Get token from localStorage
  const token = localStorage.getItem('access_token');

  // If token not found → redirect to login
  if (!token) {
    return <Navigate to="/login" replace />;
  }

  // If logged in → show dashboard
  return children;
};

export default PrivateRoute;