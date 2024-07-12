// 일치 연산자 ===를 제외한 비교 연산자의 피연산자에 undefined나 null이 오지 않도록 특별히 주의하시기 바랍니다.
// 또한, undefined나 null이 될 가능성이 있는 변수가 <, >, <=, >=의 피연산자가 되지 않도록 주의하시기 바랍니다. 
// 명확한 의도를 갖고 있지 않은 이상 말이죠. 
// 만약 변수가 undefined나 null이 될 가능성이 있다고 판단되면, 이를 따로 처리하는 코드를 추가하시기 바랍니다.


5 > 4                   // true
"apple" > "pineapple"   // false
"2" > "12"              // true
undefined == null       // true
undefined === null      // false
null == "\n0\n"         // false -> null은 오직 undefined와 같습니다.
null === +"\n0\n"       // false -> 형이 다르므로 false가 반환