import { useState, useEffect, useCallback } from 'react';
import api from '../api/axios';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
  const [resumes, setResumes] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [uploadError, setUploadError] = useState('');

  const navigate = useNavigate();

  // Fetch dashboard data
  const fetchDashboardData = useCallback(async () => {
    try {
      setLoading(true);

      const [resumesRes, jobsRes] = await Promise.all([
        api.get('resumes/'),
        api.get('recommend-jobs/')
      ]);

      setResumes(resumesRes.data);
      setRecommendations(jobsRes.data);
      setError('');

    } catch (err) {

      if (err.response?.status === 401) {
        navigate('/login');
      } else {
        setError('Failed to load dashboard data. Please check your connection.');
      }

      console.error(err);

    } finally {
      setLoading(false);
    }
  }, [navigate]);

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    fetchDashboardData();
  }, [fetchDashboardData]);

  // Handle file selection
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Upload resume
  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) return;

    const formData = new FormData();
    formData.append('resume_file', file);

    try {

      setLoading(true);
      setUploadError('');

      await api.post('resumes/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      setFile(null);

      // Refresh dashboard data
      fetchDashboardData();

    } catch (err) {

      setUploadError(
        err.response?.data?.detail ||
        err.response?.data?.resume_file?.[0] ||
        'Failed to upload and analyze the resume.'
      );

      console.error("Upload failed", err);

    } finally {
      setLoading(false);
    }
  };

  // Logout function
  const handleLogout = () => {

    // Remove tokens
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');

    // Redirect user to login page
    navigate('/login');
  };

  // Loading screen
  if (loading) {
    return <div className="loading">Loading Dashboard...</div>;
  }

  const latestResume = resumes.length > 0 ? resumes[0] : null;

  return (
    <div className="dashboard-container">

      {/* Header */}
      <header className="dashboard-header">
        <h2>Your Career Dashboard</h2>

        <button
          onClick={handleLogout}
          className="btn-primary"
        >
          Logout
        </button>
      </header>

      {/* Error Message */}
      {error && <div className="error">{error}</div>}

      <div className="dashboard-grid">

        {/* Upload Resume Card */}
        <div className="card upload-card">
          <h3>Upload Resume (PDF)</h3>

          {uploadError && (
            <div className="error">
              {uploadError}
            </div>
          )}

          <form onSubmit={handleUpload}>
            <input
              type="file"
              accept=".pdf"
              onChange={handleFileChange}
            />

            <button
              type="submit"
              className="btn-primary"
              disabled={!file || loading}
            >
              {loading ? "Uploading..." : "Upload & Analyze"}
            </button>
          </form>
        </div>

        {/* Skills Card */}
        <div className="card skills-card">
          <h3>Your Extracted Skills</h3>

          {latestResume ? (

            latestResume.skills && latestResume.skills.length > 0 ? (

              <div className="skills-tags">
                {latestResume.skills.map((skill) => (
                  <span
                    key={skill.id}
                    className="skill-tag"
                  >
                    {skill.name}
                  </span>
                ))}
              </div>

            ) : (
              <p className="text-muted">
                No skills found. Try uploading a different resume.
              </p>
            )

          ) : (
            <p className="text-muted">
              Upload a resume to see your skills.
            </p>
          )}
        </div>
      </div>

      {/* Recommendations */}
      <div className="card recommendations-card">
        <h3>Recommended Jobs for You</h3>

        {recommendations.length > 0 ? (

          <div className="jobs-list">

            {recommendations.map((job) => (

              <div
                key={job.id}
                className="job-item"
              >

                <div className="job-header">
                  <h4>{job.title}</h4>

                  <span className="match-badge">
                    Match: {job.match_score}%
                  </span>
                </div>

                <p className="job-desc">
                  {job.description}
                </p>

                <div className="job-skills">
                  <strong>Required: </strong>
                  {job.required_skills}
                </div>

              </div>

            ))}

          </div>

        ) : (
          <p className="text-muted">
            No job recommendations available at the moment.
          </p>
        )}
      </div>

    </div>
  );
};

export default Dashboard;