// alert
// 메시지를 보여줍니다.

// prompt
// 사용자에게 텍스트를 입력하라는 메시지를 띄워줌과 동시에, 입력 필드를 함께 제공합니다. 
// 확인을 누르면 prompt 함수는 사용자가 입력한 문자열을 반환하고, 취소 또는 Esc를 누르면 null을 반환합니다.

// confirm
// 사용자가 확인 또는 취소 버튼을 누를 때까지 메시지가 창에 보여집니다. 
// 사용자가 확인 버튼을 누르면 true를, 취소 버튼이나 Esc를 누르면 false를 반환합니다.

// [ 간단한 페이지 만들기 ]
// 사용자에게 이름을 물어보고, 입력받은 이름을 그대로 출력해주는 페이지를 만들어보세요.
let userName = prompt("이름을 입력해주세요!", "");
alert(`당신의 이름은 ${userName}입니다!`);