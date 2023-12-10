import React, {useState} from "react";
import {useNavigate} from 'react-router-dom';

import '../styles/InputPage.css';
import { Button, Select } from 'antd';

import axios from 'axios';


function DropAndSubmit() {
    const { Option } = Select;
    //사용자가 드롭다운바에서 선택한 숫자 상태 관리
    const [selectNum, setSelectNum] = useState(1);

    //QuizPage.js로 이동하기 위함
    const navigate = useNavigate();

    //사용자가 선택한 값을 화면에 띄우기
    const handleSelect = (value) => {
        setSelectNum(value);
    };

    //서버에 사용자가 선택한 값(num) 전달하며 퀴즈데이터 요청 보내기
    const handleSubmit = async(selectNum) => {
        try {
            // API엔드포인트의 URL, num 객체 전송
            const response = await axios.get('/create/quiz', { params: { number: selectNum }  } );
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
        <>
            <Select defaultValue={selectNum} onChange={handleSelect} style={{width : 120}} listHeight={150}>
                {Array.from ({length:13}, (_, i) => i + 1).map((num) => (
                    <Option key={num} value={num}> {num} </Option>
                ))}
            </Select>
            <Button type="primary" className="InputButton" onClick={() => handleSubmit(selectNum)}>Go!</Button>
        </>
    );
}


function InputPage() {
    return (
        <div className="Input">
            <div className="InputContentBox">
                <div className="InputTitle">다음과 같은 내용의 문제가 출제됩니다</div>
                <div className="InputContainer">
                    <div className="InputElement">Data Structure<br/>&amp; Algorithms</div>
                    <div className="InputElement">Basic &amp;<br/>Sorting/Searching</div>
                    <div className="InputElement">Definition, Synonym,<br/> Generalization,<br/> Time Complexity</div>
                </div>
                <div className="InputNumBox">
                    <div className="InputContent">출제할 문제 수 : </div>
                    <DropAndSubmit/>
                </div>
            </div>
        </div>
    );
}

export default InputPage;