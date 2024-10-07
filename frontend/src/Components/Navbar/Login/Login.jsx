import React from 'react'
import './Login.css'
const videoSource = require('../../../assets/Cyber Security Opener (After Effects template).mp4');

const Main = () => {
  return (
    <div>
        <div className='Main'>
             <video autoPlay muted loop>
                <source src={videoSource} type="video/mp4" />
              </video>

            <div className="Main-text">
              <h1> Cyber Security  </h1>
              <p> </p>
           </div>
     
        </div>
      <div className="Content">
      <section>
          <h2>About Cyber Security</h2>
          <p>
            Cybersecurity refers to the practice of protecting systems, networks, and programs from digital attacks.
            These cyberattacks are usually aimed at accessing, changing, or destroying sensitive information; 
            extorting money from users; or interrupting normal business processes.
          </p>
        </section>

        <section>
          <h2>Features of Our Recon Tool</h2>
          <ul>
            <li>Vulnerability Scanning</li>
            <li>Network Mapping</li>
            <li>Information Gathering</li>
            <li>Automated Reporting</li>
          </ul>
        </section>

        <section>
          <h2>Get Started with Recon Tool</h2>
          <p>
            To begin using our tool, create an account or log in. Our tool provides insights and scans to ensure your systems are secure.
          </p>
          <button>Learn More</button>
        </section>
      </div>
      </div>
    
  )
}

export default Main
