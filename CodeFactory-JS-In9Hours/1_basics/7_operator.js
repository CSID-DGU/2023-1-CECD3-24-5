/**
 * Operators
 * 연산자
 */

/**
 * 산술 연산자
 * 
 * 1)덧셈
 * 2)뺄셈
 * 3)곱셈
 * 4)나눗셈 : /
 * 5)나머지 : %
 */

let number=1;
number++;
number--;

/** 
 * 연산자의 위치
 * 
 * 후위 연산자 (변수 뒤에 ++, --)의 경우
 * 앞의 연산자가 먼저 실행되고 이후에 후위연산자 실행함
 */
let result = 1;
console.log(result);

//= 연산자가 앞에 있으므로 먼저 저장됨
//이후에 ++ 연산자 실행됨
result = number ++;
console.log(result, number);

/**
 * 숫자 타입이 아닌 타입에 +, - 사용하면 어떻게 될까?
 */
//+ 붙이면 number 타입으로 바뀜
let sample = '99';
console.log(typeof +sample);
//근데 원본은 안바뀜. 여전히 string.
console.log(sample);
console.log(typeof sample);

/** 
 * 단축평가 (short circuit evaluation)
 * 
 * &&는 둘다 true여야 true 반환
 * &&를 사용했을 때 왼쪽이 true면 오른쪽 값 반환
 * &&를 사용했을 때 왼쪽이 false면 왼쪽 값 반환
 * 
 * ||는 하나만 true여도 true 반환
 * ||를 사용했을 때 왼쪽이 true면 왼쪽 값 반환
 * ||를 사용했을 때 왼쪽이 false면 오른쪽 값 반환
 */
