import { useState, useCallback } from 'react';
import api from '../api/axios';
import { useNavigate } from 'react-router-dom';

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend
} from 'recharts';

const Dashboard = () => {

  const [resumes, setResumes] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [file, setFile] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState('');
  const [uploadError, setUploadError] = useState('');

  const [showResults, setShowResults] = useState(false);

  const navigate = useNavigate();

  // Fetch Dashboard Data
  const fetchDashboardData = useCallback(async () => {

    try {

      const resumesResponse = await api.get(
        'resumes/'
      );

      const jobsResponse = await api.get(
        'recommend-jobs/'
      );

      setResumes(resumesResponse.data);

      setRecommendations(jobsResponse.data);

      setError('');

    } catch (err) {

      console.error(err);

      if (err.response?.status === 401) {

        navigate('/login');

      } else {

        setError(
          'Failed to load dashboard data.'
        );
      }
    }

  }, [navigate]);

  // File Selection
  const handleFileChange = (e) => {

    setFile(e.target.files[0]);
  };

  // Upload Resume
  const handleUpload = async (e) => {

    e.preventDefault();

    if (!file) return;

    const formData = new FormData();

    formData.append(
      'resume_file',
      file
    );

    try {

      setLoading(true);

      setUploadError('');

      // Hide old results
      setShowResults(false);

      await api.post(

        'resumes/upload/',

        formData,

        {
          headers: {
            'Content-Type':
            'multipart/form-data'
          }
        }
      );

      await fetchDashboardData();

      setShowResults(true);

    } catch (err) {

      console.error(err);

      setUploadError(

        err.response?.data?.detail ||

        'Failed to upload resume.'
      );

    } finally {

      setLoading(false);
    }
  };

  // Logout
  const handleLogout = () => {

    localStorage.removeItem(
      'access_token'
    );

    localStorage.removeItem(
      'refresh_token'
    );

    navigate('/login');
  };

  // Latest Resume
  const latestResume = resumes.length > 0
    ? resumes[0]
    : null;

  // ATS Score Data
  const atsScoreData = [

    {
      name: 'Score',
      value: latestResume?.resume_score || 0
    },

    {
      name: 'Remaining',
      value:
        100 -
        (latestResume?.resume_score || 0)
    }
  ];

  // Skills Radar Data
  const skillsRadarData = [

    {
      subject: 'Frontend',

      value:
        latestResume?.skills?.filter(
          skill =>

            [
              'React',
              'Javascript',
              'HTML',
              'CSS'
            ].includes(skill.name)
        ).length * 20 || 0
    },

    {
      subject: 'Backend',

      value:
        latestResume?.skills?.filter(
          skill =>

            [
              'Python',
              'Django',
              'Flask',
              'SQL'
            ].includes(skill.name)
        ).length * 20 || 0
    },

    {
      subject: 'Databases',

      value:
        latestResume?.skills?.filter(
          skill =>

            [
              'SQL',
              'MySQL',
              'Postgresql',
              'MongoDB'
            ].includes(skill.name)
        ).length * 20 || 0
    },

    {
      subject: 'DevOps',

      value:
        latestResume?.skills?.filter(
          skill =>

            [
              'Docker',
              'AWS',
              'Kubernetes'
            ].includes(skill.name)
        ).length * 20 || 0
    },

    {
      subject: 'AI/ML',

      value:
        latestResume?.skills?.filter(
          skill =>

            [
              'Machine Learning',
              'Tensorflow',
              'Pytorch',
              'Numpy',
              'Pandas'
            ].includes(skill.name)
        ).length * 20 || 0
    }
  ];

  // Job Match Bar Graph Data
  const jobMatchData = recommendations
    .slice(0, 5)
    .map(job => ({

      subject:
        job.title.length > 15

          ? job.title.substring(0, 15)

          : job.title,

      value: job.match_score
    }));

  const COLORS = [
    '#4CAF50',
    '#E0E0E0'
  ];

  return (

    <div className="dashboard-container">

      {/* Header */}
      <header className="dashboard-header">

        <h2>
          Your Career Dashboard
        </h2>

        <button
          onClick={handleLogout}
          className="btn-primary"
        >
          Logout
        </button>

      </header>

      {/* Dashboard Error */}
      {error && (

        <div className="error">
          {error}
        </div>

      )}

      <div className="dashboard-grid">

        {/* Upload Card */}
        <div className="card upload-card">

          <h3>
            Upload Resume (PDF)
          </h3>

          {/* Upload Error */}
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

            {/* Selected File */}
            {file && (

              <p
                className="text-muted"
                style={{
                  marginTop: "10px"
                }}
              >
                Selected File:
                {" "}
                {file.name}
              </p>

            )}

            {/* Upload Button */}
            <button
              type="submit"
              className="btn-primary"
              disabled={!file || loading}
            >

              {loading
                ? "Analyzing..."
                : "Upload & Analyze"}

            </button>

            {/* View Resume */}
            {showResults &&
             latestResume?.resume_file && (

              <div
                style={{
                  marginTop: "15px"
                }}
              >

                <a
                  href={latestResume.resume_file}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-primary"
                  style={{
                    display: "inline-block",
                    textDecoration: "none",
                    padding: "10px 15px"
                  }}
                >
                  View Uploaded Resume
                </a>

              </div>

            )}

          </form>

        </div>

        {/* Skills Card */}
        <div className="card skills-card">

          <h3>
            Your Extracted Skills
          </h3>

          {showResults &&
           latestResume &&
           latestResume.experience_level && (

            <div
              style={{
                marginBottom: "15px"
              }}
            >

              <strong
                style={{
                  color: "#4CAF50",
                  fontSize: "17px"
                }}
              >
                Experience Level:
                {" "}
                {latestResume.experience_level}
              </strong>

            </div>

          )}

          {showResults &&
           latestResume?.skills?.length > 0 ? (

            <div className="skills-tags">

              {latestResume.skills.map(
                (skill) => (

                  <span
                    key={skill.id}
                    className="skill-tag"
                  >
                    {skill.name}
                  </span>

                )
              )}

            </div>

          ) : (

            <p className="text-muted">

              Upload and analyze
              a resume to view skills.

            </p>

          )}

        </div>

      </div>

      {/* Resume Analysis */}
      {showResults && latestResume && (

        <div className="card recommendations-card">

          <h3>
            Resume Analysis
          </h3>

          {/* AI Suggestions */}
          {latestResume.ai_suggestions?.length > 0 && (

            <div
              style={{
                marginTop: "25px"
              }}
            >

              <h4
                style={{
                  color: "#2196F3"
                }}
              >
                AI Resume Suggestions
              </h4>

              <div
                style={{
                  display: "flex",
                  flexDirection: "column",
                  gap: "12px",
                  marginTop: "15px"
                }}
              >

                {latestResume.ai_suggestions.map(
                  (suggestion, index) => (

                    <div
                      key={index}
                      style={{

                        backgroundColor: "#f4f8ff",

                        borderLeft:
                          "5px solid #2196F3",

                        padding: "12px",

                        borderRadius: "8px",

                        color: "#333"
                      }}
                    >

                      {suggestion}

                    </div>

                  )
                )}

              </div>

            </div>

          )}

          {/* Career Paths */}
          {latestResume.career_paths?.length > 0 && (

            <div
              style={{
                marginTop: "30px"
              }}
            >

              <h4
                style={{
                  color: "#9C27B0"
                }}
              >
                Recommended Career Paths
              </h4>

              <div
                style={{
                  display: "flex",
                  flexWrap: "wrap",
                  gap: "15px",
                  marginTop: "15px"
                }}
              >

                {latestResume.career_paths.map(
                  (career, index) => (

                    <div
                      key={index}
                      style={{

                        background:
                          "linear-gradient(135deg, #9C27B0, #673AB7)",

                        color: "white",

                        padding: "15px 20px",

                        borderRadius: "12px",

                        fontWeight: "bold",

                        minWidth: "220px",

                        textAlign: "center"
                      }}
                    >

                      {career}

                    </div>

                  )
                )}

              </div>

            </div>

          )}

        </div>

      )}

      {/* Resume Analytics */}
      {showResults && latestResume && (

        <div className="card recommendations-card">

          <h3
            style={{
              marginBottom: "30px"
            }}
          >
            Resume Analytics
          </h3>

          <div
            style={{
              display: 'grid',

              gridTemplateColumns:
                'repeat(auto-fit, minmax(350px, 1fr))',

              gap: '40px'
            }}
          >

            {/* ATS ROUND GRAPH */}
            <div>

              <h4
                style={{
                  textAlign: 'center',
                  marginBottom: '20px'
                }}
              >
                ATS Resume Score
              </h4>

              <ResponsiveContainer
                width="100%"
                height={350}
              >

                <PieChart>

                  <Pie
                    data={atsScoreData}
                    dataKey="value"
                    innerRadius={90}
                    outerRadius={120}
                    paddingAngle={3}
                  >

                    {atsScoreData.map(
                      (entry, index) => (

                        <Cell
                          key={index}
                          fill={COLORS[index]}
                        />

                      )
                    )}

                  </Pie>

                  <Tooltip />

                </PieChart>

              </ResponsiveContainer>

              <h1
                style={{
                  textAlign: 'center',
                  color: '#4CAF50',
                  marginTop: '-40px'
                }}
              >
                {latestResume.resume_score}%
              </h1>

            </div>

            {/* SKILLS RADAR GRAPH */}
            <div>

              <h4
                style={{
                  textAlign: 'center',
                  marginBottom: '20px'
                }}
              >
                Skills Distribution
              </h4>

              <ResponsiveContainer
                width="100%"
                height={350}
              >

                <RadarChart
                  data={skillsRadarData}
                >

                  <PolarGrid />

                  <PolarAngleAxis
                    dataKey="subject"
                  />

                  <PolarRadiusAxis
                    angle={30}
                    domain={[0, 100]}
                  />

                  <Radar
                    name="Skills"
                    dataKey="value"
                    stroke="#2196F3"
                    fill="#2196F3"
                    fillOpacity={0.6}
                  />

                  <Legend />

                </RadarChart>

              </ResponsiveContainer>

            </div>

            {/* JOB MATCH BAR GRAPH */}
            <div>

              <h4
                style={{
                  textAlign: 'center',
                  marginBottom: '20px'
                }}
              >
                Job Match Scores
              </h4>

              <ResponsiveContainer
                width="100%"
                height={350}
              >

                <BarChart
                  data={jobMatchData}
                >

                  <CartesianGrid
                    strokeDasharray="3 3"
                  />

                  <XAxis dataKey="subject" />

                  <YAxis />

                  <Tooltip />

                  <Legend />

                  <Bar
                    dataKey="value"
                    fill="#9C27B0"
                    radius={[10, 10, 0, 0]}
                  />

                </BarChart>

              </ResponsiveContainer>

            </div>

          </div>

        </div>

      )}

      {/* Recommended Jobs */}
      <div className="card recommendations-card">

        <h3>
          Recommended Jobs For You
        </h3>

        {showResults &&
         recommendations.length > 0 ? (

          <div className="jobs-list">

            {recommendations.map(
              (job, index) => (

                <div
                  key={index}
                  className="job-item"
                >

                  <div className="job-header">

                    <h4>
                      {job.title}
                    </h4>

                    <span className="match-badge">

                      Match:
                      {" "}
                      {job.match_score}%

                    </span>

                  </div>

                  <p
                    style={{
                      color: "#4CAF50",
                      fontWeight: "bold"
                    }}
                  >
                    Level:
                    {" "}
                    {job.experience_level}
                  </p>

                  <p className="job-desc">
                    {job.description}
                  </p>

                </div>

              )
            )}

          </div>

        ) : (

          <p className="text-muted">

            Upload and analyze a resume
            to get recommendations.

          </p>

        )}

      </div>

    </div>
  );
};

export default Dashboard;