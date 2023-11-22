import React from "react";
import { useNavigate } from 'react-router-dom';
import '../styles/EnterPage.css';
import {Button} from 'antd';
import Bottom from '../components/Bottom'

function EnterPage() {
    const navigate = useNavigate(); //hook은 함수 컴포넌트의 최상위 레벨에서 호출되어야 함.

    const handleStart = () => {
        navigate('/InputPage');
      };

    return (
        <div className="Enter">
            <div className="EnterContentBox">
                <div className="EnterTitle">Automatic Quiz Generalization</div>
                <div className="EnterContent">당신의 지식을 테스트해보세요!</div>
                <Button type="primary" className='EnterButton' onClick={handleStart}>Start</Button>
                {/* <button className='EnterButton' onClick={handleStart}>Start</button> */}
            </div>
            <Bottom />
        </div>
    );
}


export default EnterPage;
