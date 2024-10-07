import React, { useState } from 'react'
import './Navbar.css'
import logo from '../../assets/logo2.png'
import { Link } from 'react-router-dom'
const Navbar = () => {
  return (
    <nav className=' dark-nav '>
      <img src={logo} alt="" className="logo" />
      <ul>
        <li><Link to='' smooth={true} offset={0} duration={500}></Link></li>
        <li><Link to='Login' smooth={true} offset={0} duration={500}>Home</Link></li>
        <li><Link to='Programs' smooth={true} offset={-260} duration={500}>Test</Link></li>
        <li><Link to='Test' smooth={true} offset={-260} duration={500}>Info</Link></li>
        <li><Link to='About' smooth={true} offset={-260} duration={500}>Contact us</Link></li>
        

      </ul>
    </nav>
  )
}

export default Navbar
