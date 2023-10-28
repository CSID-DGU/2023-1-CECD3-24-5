import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Header.css';
import useLocalStorage from '../hooks/useLocalStorage';

function Header() {
    const navigate = useNavigate();
    const handleEnter = () => {
        localStorage.clear();
        navigate(`/`);
    };

    return (
        <div className='HeaderBox'>
            <button className='HeaderContent' onClick={handleEnter}>Twenty4</button>
        </div>
    );
}

export default Header;