import { Link } from 'react-router-dom';
import { 
  FaRobot, FaFileAlt, FaChartLine, FaLock, 
  FaUpload, FaCheckCircle, FaUserTie, FaLinkedin, FaTwitter, FaGithub, FaArrowRight 
} from 'react-icons/fa';
import { BsStars } from 'react-icons/bs';
import './Home.css';

const Home = () => {
  return (
    <div className="home-container">
      {/* Background Elements */}
      <div className="bg-orb orb-1"></div>
      <div className="bg-orb orb-2"></div>
      <div className="bg-orb orb-3"></div>

      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-content">
          <div className="hero-badge">
            <BsStars className="badge-icon" />
            <span>Next-Generation Career AI</span>
          </div>
          <h1>
            AI-Powered Resume Analysis <br />
            <span className="gradient-text">& Smart Job Matching</span>
          </h1>
          <p className="hero-subtitle">
            Upload your resume, extract skills automatically, and discover personalized job recommendations powered by advanced AI.
          </p>
          <div className="hero-cta-group">
            <Link to="/register" className="btn-primary-glow">
              Get Started <FaArrowRight />
            </Link>
            <a href="#features" className="btn-secondary-glow">
              Explore Features
            </a>
          </div>
        </div>
        <div className="hero-visual">
          <div className="glass-panel main-panel">
            <div className="panel-header">
              <span className="dot dot-red"></span>
              <span className="dot dot-yellow"></span>
              <span className="dot dot-green"></span>
            </div>
            <div className="panel-body">
              <div className="scan-line"></div>
              <FaFileAlt className="visual-icon resume-icon pulse" />
              <div className="visual-line line-1"></div>
              <div className="visual-line line-2"></div>
              <div className="visual-line line-3"></div>
              <div className="ai-node">
                <FaRobot />
              </div>
            </div>
          </div>
          {/* Floating elements */}
          <div className="floating-card float-1">
             <FaChartLine className="text-blue" />
             <span>95% Match Rate</span>
          </div>
          <div className="floating-card float-2">
             <FaCheckCircle className="text-green" />
             <span>Skills Extracted</span>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="features-section">
        <div className="section-header">
          <h2>Powerful <span className="gradient-text">Features</span></h2>
          <p>Everything you need to accelerate your job search.</p>
        </div>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon-wrapper"><FaFileAlt /></div>
            <h3>Resume Analysis</h3>
            <p>Deep parsing of your resume to understand your complete professional profile and experience.</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon-wrapper"><BsStars /></div>
            <h3>Skill Extraction</h3>
            <p>Advanced NLP identifies core competencies and technical skills hidden in your text.</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon-wrapper"><FaChartLine /></div>
            <h3>AI Job Matching</h3>
            <p>Our algorithms find the perfect roles for you based on your unique extracted skill set.</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon-wrapper"><FaLock /></div>
            <h3>Secure Authentication</h3>
            <p>Bank-level JWT security ensures your personal career data remains strictly confidential.</p>
          </div>
        </div>
      </section>

      {/* Statistics Section */}
      <section className="stats-section">
        <div className="stats-grid glass-card">
          <div className="stat-item">
            <h3>1000+</h3>
            <p>Resumes Analyzed</p>
          </div>
          <div className="stat-item">
            <h3>500+</h3>
            <p>Job Matches</p>
          </div>
          <div className="stat-item">
            <h3>95%</h3>
            <p>Match Accuracy</p>
          </div>
          <div className="stat-item">
            <h3>100%</h3>
            <p>Secure System</p>
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section className="how-it-works-section">
        <div className="section-header">
          <h2>How It <span className="gradient-text">Works</span></h2>
          <p>Four simple steps to your dream job.</p>
        </div>
        <div className="timeline">
          <div className="timeline-item">
            <div className="step-number">1</div>
            <div className="timeline-content glass-card">
              <FaUserTie className="step-icon" />
              <h3>Register / Login</h3>
              <p>Create your secure account to access our AI tools.</p>
            </div>
          </div>
          <div className="timeline-item">
            <div className="step-number">2</div>
            <div className="timeline-content glass-card">
              <FaUpload className="step-icon" />
              <h3>Upload Resume</h3>
              <p>Upload your latest CV in PDF format securely.</p>
            </div>
          </div>
          <div className="timeline-item">
            <div className="step-number">3</div>
            <div className="timeline-content glass-card">
              <FaRobot className="step-icon" />
              <h3>AI Extracts Skills</h3>
              <p>Our engine reads and categorizes your abilities.</p>
            </div>
          </div>
          <div className="timeline-item">
            <div className="step-number">4</div>
            <div className="timeline-content glass-card">
              <FaChartLine className="step-icon" />
              <h3>Get Recommendations</h3>
              <p>Receive smart, tailored job matches instantly.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="testimonials-section">
        <div className="section-header">
          <h2>Success <span className="gradient-text">Stories</span></h2>
          <p>See what our users have achieved.</p>
        </div>
        <div className="testimonials-grid">
          <div className="testimonial-card glass-card">
            <div className="quote">"JobFit Analyzer completely changed how I look for roles. The AI found jobs I wouldn't have considered but were perfect for my skills."</div>
            <div className="author">
              <div className="avatar bg-gradient-1">SJ</div>
              <div className="author-info">
                <h4>Sarah Jenkins</h4>
                <p>Software Engineer</p>
              </div>
            </div>
          </div>
          <div className="testimonial-card glass-card">
            <div className="quote">"The skill extraction is scarily accurate. It helped me realize I was underselling myself on my resume. Highly recommended!"</div>
            <div className="author">
              <div className="avatar bg-gradient-2">MD</div>
              <div className="author-info">
                <h4>Marcus Doe</h4>
                <p>Data Analyst</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="home-footer glass-card">
        <div className="footer-content">
          <div className="footer-brand">
            <h3>JobFit Analyzer</h3>
            <p>Empowering your career through Artificial Intelligence.</p>
          </div>
          <div className="footer-links">
            <h4>Quick Links</h4>
            <Link to="/">Home</Link>
            <a href="#features">Features</a>
            <Link to="/dashboard">Dashboard</Link>
          </div>
          <div className="footer-social">
            <h4>Connect</h4>
            <div className="social-icons">
              <a href="#!"><FaLinkedin /></a>
              <a href="#!"><FaTwitter /></a>
              <a href="#!"><FaGithub /></a>
            </div>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; {new Date().getFullYear()} JobFit Analyzer. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default Home;
