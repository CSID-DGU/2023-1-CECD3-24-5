import React, {useEffect, useState} from "react";
import { Navigate, useNavigate} from 'react-router-dom';
import '../styles/InputPage.css';
import Bottom from '../components/Bottom'

import axios from 'axios';


function DropAndSubmit() {
    //사용자가 드롭다운바에서 선택한 숫자 상태 관리
    const [selectNum, setSelectNum] = useState(1);

    //QuizPage.js로 이동하기 위함
    const navigate = useNavigate();

    //사용자가 선택한 값을 화면에 띄우기
    const handleSelect = (e) => {
        setSelectNum(e.target.value);
    };

    //서버에 사용자가 선택한 값(num) 전달하며 퀴즈데이터 요청 보내기
    const handleSubmit = async(selectNum) => {
        try {
            // API엔드포인트의 URL, num 객체 전송
            const response = await axios.get('http://127.0.0.1:5000/create/quiz', { params: { number: selectNum }  } );
            console.log(response.data);
        
            //서버에서 받아온 Response 객체는 json 형식으로 자동 파싱됨.
            //QuizPage 경로의 컴포넌트에 quizData 전송 -> useLocation 사용, location.state.quizData으로 접근
            if (response.data) {
                navigate('/QuizPage', { state: response.data });
              } else {
                console.error("Data is missing");
                navigate('/QuizPage', { 
                    state: {
                        id: 1,
                        problem : 'What is the time complexity of Bubble Sort in the worst-case scenario?',
                        select : ['O(n^2)', 'O(n log n)', 'O(n)', 'O(1)'],
                        answer : 2
                    },
                });
              }
              
        } catch (error) {
            console.error("There was an error sending the data!", error);
        }
    };

    return (
        <div>
            <select value={selectNum} onChange={handleSelect} >
                {Array.from ({length:30}, (_, i) => i + 1).map((num) => (
                    <option key={num} value={num}> {num} </option>
                ))}
            </select>
            <button onClick={() => handleSubmit(selectNum)}>Go!</button>
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
                    <div className="InputContent">출제할 문제 수 : </div>
                    <DropAndSubmit/>
                </div>
            </div>
            <Bottom />
        </div>
    );
}

export default InputPage;