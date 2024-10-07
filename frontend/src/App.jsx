import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Navbar from './Components/Navbar/Navbar'
import Main from './Components/Navbar/Main/Main'
import Programs from './Components/Navbar/Programs/Program'
import Title from './Components/Navbar/Title/Title'
import About from './Components/Navbar/About/About'
import Test from './Components/Navbar/Test/Test'
import Footer from './Components/Footer/Footer'
import Login from './Components/Navbar/Login/Login'

const App = () => {
  return (
    <Router>
      <div>
       <Navbar/>
      <Routes>
        
          <Route path="/Main" element={<Main/>}/>
          <Route path="/Login" element={<Login/>}/>
         
          <Route path="/Programs" element={<Programs />} />
          <Route path="/About" element={<About />} />
          <Route path="/Test" element={<Test />} />q
          <Route path="/Footer" element={<Footer />} />

      </Routes>
      
     

      
  </div>

    </Router>
  
  )
}

export default App
