// [ 변수 가지고 놀기 ]
// - admin과 name이라는 변수를 선언하세요.
// - name에 값으로 "John"을 할당해 보세요.
// - name의 값을 admin에 복사해 보세요.
// - admin의 값을 alert 창에 띄워보세요. "John"이 출력되어야 합니다.

let admin, name;
name = "John";
admin = name;
alert(admin);

// [ 올바른 이름 선택하기 ]
// 현재 우리가 살고있는 행성(planet)의 이름을 값으로 가진 변수를 만들어보세요. 변수 이름은 어떻게 지어야 할까요?
// 웹사이트를 개발 중이라고 가정하고, 현재 접속 중인 사용자(user)의 이름(name)을 저장하는 변수를 만들어보세요. 변수 이름은 어떻게 지어야 할까요?

const ourPlanetName = "Earth";
let currentUserName = "John";

// [ 대문자 상수 올바로 사용하기 ]
// 대문자 상수는 하드 코딩한 값의 별칭을 만들 때 주로 사용한다.
// 실행 전에 이미 값을 알고 있고, 코드에서 직접 그 값을 쓰는 경우에 사용한다.
const BIRTHDAY = '18.04.1982';
const age = someCode(BIRTHDAY);

