// https://ko.javascript.info/logical-operators

let admin = prompt("Who's there?", "");
if(admin === "Admin"){
    let password = prompt("Password?", "");
    if (password === "TheMaster") {
        alert("환영합니다!");
    } else if (password === "") {
        alert("취소되었습니다.");
    } else {
        alert("인증에 실패했습니다.")
    }
} else if (admin === "") {
    alert("Canceled")
} else {
    alert("I don't know you")
}