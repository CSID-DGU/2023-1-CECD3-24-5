import React, {useEffect, useState} from "react";
import { Navigate, useNavigate } from 'react-router-dom';
import '../styles/InputPage.css';
import Bottom from '../components/Bottom'

import axios from 'axios';

function InputNum() {
    const [num, setNum] = useState("");

    // 입력 값 변경 핸들러
    const handleChange = (e) => {
        setNum(e.target.value);
    };

    const handleSubmit = async (e) => {
      e.preventDefault();
  
      try {
        // API엔드포인트의 URL, num 객체(string -> ㅑㅜㅅ로) 전송
        const response = await axios.post('https://your-server-endpoint.com/data', { num });
        console.log(response.data);
      } catch (error) {
        console.error("There was an error sending the data!", error);
      }
    };

    return (
        <div>
            <input 
                type="text" 
                value={num} 
                onChange={handleChange} 
            />
            <span>문제</span>
            <br/>
            <button onClick={handleSubmit}>문제 생성</button>
        </div>
    );
}


function InputPage() {
    return (
        <div className="Input">
            <div className="InputContentBox">
                <div className="InputTitle">다음과 같은 내용의 문제가 출제됩니다</div>
                <div className="InputContainer">
                    <div className="InputElement1">Data Structure\n& Algorithms</div>
                    <div className="InputElement2">Basic\n& Sorting/Searching</div>
                    <div className="InputElement3">Definition, Synonym,\n Generalization,\n Time Complexity</div>
                </div>
                <div className="InputNumBox">
                    <div className="InputContent">출제할 문제 수: </div>
                    <InputNum />
                </div>
            </div>
            <Bottom />
        </div>
    );
}

export default InputPage;