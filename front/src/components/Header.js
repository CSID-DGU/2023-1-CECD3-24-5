import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Header.css';

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