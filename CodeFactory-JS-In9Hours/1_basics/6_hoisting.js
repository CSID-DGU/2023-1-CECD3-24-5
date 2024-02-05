/**
 * Hoisting
 */

console.log('Hello');
console.log('World');

/**
 * Hoisting은 무엇인가?
 * 
 * 모든 변수 선언문이 코드 최상단으로 이동되는 것처럼 느껴지는 현상
 */

console.log(name);
var name = '옹헤';
console.log(name);

console.log(yuJin);
//let yuJin = '안유진';

/**
 * let과 const에서도 hoisting이 발생한다
 * 근데 에러메세지 출력해서 보여준다
 * var은 그걸 못막아주니까...그래서 let과 const만 사용하라는 것!
 */