let answer = prompt("자바스크립트의 '공식' 이름은 무엇일까요?", "");
if (answer === "ECMAScript") {
    alert("정답입니다!");
} else {
    alert("모르셨나요? 정답은 ECMAScript입니다!");
}

let number = prompt("숫자 하나를 입력하세요", 0);
if (answer > 0) {
    alert(1);
} else if (answer < 0) {
    alert(-1);
} else {
    alert(0)
}


// let result;
// if (a + b < 4) {
//   result = '미만';
// } else {
//   result = '이상';
// }

let result = (a + b < 4) ? '미만': '이상';


// let message;
// if (login == '직원') {
//   message = '안녕하세요.';
// } else if (login == '임원') {
//   message = '환영합니다.';
// } else if (login == '') {
//   message = '로그인이 필요합니다.';
// } else {
//   message = '';
// }

let message = (login == "직원") ? "안녕하세요." : 
    (login == "임원") ? "환영합니다." : 
    (login == "") ? "로그인이 필요합니다." : 
    "";