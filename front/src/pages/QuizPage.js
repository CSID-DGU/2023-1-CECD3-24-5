import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import '../styles/QuizPage.css';

import useLocalStorage from '../hooks/useLocalStorage';

import { Button, Radio } from 'antd';
import Tree from 'react-d3-tree';

function createTreeDataForType1(problemString) {
    const regex = /([a-z])="([^"]+)"/g;

    let nodeValues = {}; // Declare nodeValues here to make it accessible throughout the function

    const matches = problemString.match(regex);
    if (!matches) {
        console.error("No matches found in the problem string.");
    } else {
        nodeValues = matches.reduce((acc, pair) => {
            const [key, value] = pair.split('=').map(s => s.replace(/["]/g, '').trim());
            acc[key] = value;
            return acc;
        }, {});
    }
  
    const treeData = {
      name: nodeValues['a'], // root node
      children: [
        {
          name: nodeValues['b'],
          children: [
            {
              name: nodeValues['d'],
            },
            {
              name: nodeValues['e']
            }
          ]
        },
        {
          name: nodeValues['c'],
          children: [
            {
              name: nodeValues['f']
            },
            {
              name: nodeValues['g']
            }
          ]
        }
      ]
    };
    return treeData;
}

const MyTreeComponentType1 = ({ problem }) => {
    const [treeData, setTreeData] = useState(null);
  
    useEffect(() => {
      const data = createTreeDataForType1(problem);
      setTreeData([data]); // react-d3-tree는 배열 형태의 데이터를 기대합니다.
    }, [problem]);
    const scaleExtent = { min: 0.1, max: 1 };
    const translate = { x: 50, y: 200 };
    const separation = { siblings: 0.5, nonSiblings: 0.5 };
    return (
      <div id="treeWrapper" style={{ width: '50em', height: '20em' }}>
        {treeData && (
          <Tree
            data={treeData}
            scaleExtent={scaleExtent}
            translate={translate}
            separation={separation}
          />
        )}
      </div>
    );
  };


function createTreeDataForType2(problemString) {
  const nodeValues = problemString.match(/([a-z])=(-?\d+)/g).reduce((acc, pair) => {
    const [key, value] = pair.split('=');
    acc[key] = value;
    return acc;
  }, {});

  const treeData = {
    name: nodeValues['a'], // root node
    children: [
      {
        name: nodeValues['b'],
        children: [
          {
            name: nodeValues['d'],
            children: [
              {
                name: nodeValues['h']
              },
              {
                name: nodeValues['i']
              }
            ]
          },
          {
            name: nodeValues['e']
          }
        ]
      },
      {
        name: nodeValues['c'],
        children: [
          {
            name: nodeValues['f']
          },
          {
            name: nodeValues['g']
          }
        ]
      }
    ]
  };
  return treeData;
}

const MyTreeComponentType2 = ({ problem }) => {
  const [treeData, setTreeData] = useState(null);

  useEffect(() => {
    const data = createTreeDataForType2(problem);
    setTreeData([data]); // react-d3-tree는 배열 형태의 데이터를 기대합니다.
  }, [problem]);
  const scaleExtent = { min: 0.1, max: 1 };
  const translate = { x: 50, y: 200 };
  const separation = { siblings: 0.5, nonSiblings: 0.5 };
  return (
    <div id="treeWrapper" style={{ width: '50em', height: '20em' }}>
      {treeData && (
        <Tree
          data={treeData}
          scaleExtent={scaleExtent}
          translate={translate}
          separation={separation}
        />
      )}
    </div>
  );
};


function ShowQuiz() {
    //InputPage로 다시 이동하기 위함
    const navigate = useNavigate();

    const location = useLocation();
    const quizData = location.state || [];

    //테스트할 임시 데이터
    // const quizData = [
    //     {
    //         id: 1,
    //         problem : 'What is the time complexity of Bubble Sort in the worst-case scenario?',
    //         select : ['O(n^2)', 'O(n log n)', 'O(n)', 'O(1)'],
    //         answer : 2
    //     },
    //     {
    //         id: 2,
    //         problem: 'Which of the following sorting algorithms is NOT stable?',
    //         select : ['quick sort', 'insertion sort', 'merge sort', 'bubble sort'],
    //         answer : 2
    //     },
    //     {
    //         id: 3,
    //         problem : 'What is the time complexity of Bubble Sort in the worst-case scenario?',
    //         select : ['O(n^2)', 'O(n log n)', 'O(n)', 'O(1)'],
    //         answer : 2
    //     },
    //     {
    //         id: 4,
    //         problem : 'What is the time complexity of Bubble Sort in the worst-case scenario?',
    //         select : ['O(n^2)', 'O(n log n)', 'O(n)', 'O(1)'],
    //         answer : 2
    //     },
    //     {
    //         id: 5,
    //         problem: 'Which of the following sorting algorithms is NOT stable?',
    //         select : ['quick sort', 'insertion sort', 'merge sort', 'bubble sort'],
    //         answer : 2
    //     },
    //     {
    //         id: 6,
    //         problem : 'What is the time complexity of Bubble Sort in the worst-case scenario?',
    //         select : ['O(n^2)', 'O(n log n)', 'O(n)', 'O(1)'],
    //         answer : 2
    //     }
    // ];



    //사용자의 답 관리. selectopt = { 문제번호 : 선택지의 인덱스 }
    const [selectOpt, setSelectOpt] = useLocalStorage('selectOpt', {});
    //사용자의 틀린 답 관리. wrongAnswers = bool형
    const [wrongAnswers, setWrongAnswers] = useLocalStorage('wrongAnswers', {});
    //사용자의 맞은 문제 수를 저장하는 상태
    const [correctCnt, setCorrectCnt] = useLocalStorage('correctCnt', 0);
    //정답 확인하기 버튼을 눌렀는지 확인하는 상태
    //사용자가 답을 체크한 후, 상태를 localStorage에 저장 -> 새로고침 해도 checkedAnswer == true인 상태를 로드
    const [checkedAnswer, setCheckedAnswer] = useLocalStorage('checkedAnswer', false);


    const handleSelect = (quizId, optionIndex) => {
        setSelectOpt(prevState => ({ ...prevState, [quizId] : optionIndex}));
    }

    const handleAnswer = () => {
        let correct = 0;
        const wrongs = {};

        quizData.forEach(quiz => {
            //사용자가 해당 문제에 대해 선택한 답이 있다면 -> 사용자가 모두 답을 선택해야만 버튼 누를수 있게 바꾸기
            if (selectOpt[quiz.number] !== undefined) {
                //선택한 답과 정답이 일치한다면
                if (selectOpt[quiz.number] === quiz.answer) {
                    correct++;
                }
                else { //일치하지 않는다면
                    wrongs[quiz.number] = true;
                }
            }
            else {
                wrongs[quiz.number] = true;
            }
        })

        setCorrectCnt(correct);
        setWrongAnswers(wrongs);
        setCheckedAnswer(true);
    };

    const handleRestart = () => {
        // 로컬 스토리지의 모든 항목 초기화
        localStorage.clear();
        navigate('/InputPage');
    };

    return (
        <div className="OuterBox">
            {checkedAnswer && 
                <h1 className="answerText"> <span className="quizAnswer">{quizData.length} 문제</span> 중 <span>{correctCnt} 문제</span> 맞았습니다! </h1>
            }
            <div className="quizBox">
                {quizData.map((quiz) => (
                    <div className= "quizContainer" key={quiz.number}>
                        <h3 className="problemText" style={wrongAnswers[quiz.number] ? {color: 'red'} : {}}>{quiz.number}. {quiz.problem}</h3>
                        {quiz.type === 1 && (
                            <MyTreeComponentType1 problem={quiz.problem} />
                        )}
                        {quiz.type === 2 && (
                            <MyTreeComponentType2 problem={quiz.problem} />
                        )}
                        {quiz.select.map((option, index) => (
                                <label key={index} className="quizOption" style={wrongAnswers[quiz.number] && index === quiz.answer ? {color: 'red'} : {}}>
                                    <Radio
                                        name={`quiz-${quiz.number}`}
                                        value={index}
                                        onChange={() => handleSelect(quiz.number, index)}
                                        disabled={checkedAnswer}
                                        checked={selectOpt[quiz.number] === index}
                                        style={{
                                            marginRight: "15px",
                                            // ...(wrongAnswers[quiz.number] && index === quiz.answer ? { backgroundColor: 'red' } : {})
                                          }}
                                    />
                                    {option}
                                </label>
                        ))}
                    </div>
                ))}
            </div>
            <div>
                {checkedAnswer ? ( //사용자가 정답 확인하기 버튼을 누르면 -> 다시 출제하기 버튼 보이기
                    <Button type="primary" className="answerBtn" onClick={handleRestart}>다시 출제하기</Button>
                ) : (
                    <Button type="primary" className="answerBtn" onClick={handleAnswer}>정답 확인하기</Button>
                )}
            </div>
        </div>
    );
}




function QuizPage() {
    return (
        <>
            {<ShowQuiz />}
        </>
    );
}

export default QuizPage;

