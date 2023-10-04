import React, {useEffect, useState} from "react";
import { useNavigate } from 'react-router-dom';
import '../styles/EnterPage.scss';
import InputPage from './InputPage';

function EnterPage() {
    return (
        <div className="enterContent">
            <div className="innerText">Automatic Quiz Generalization</div>
        </div>
        <Bottom />
    );
}

export default EnterPage;
