function demo1() {
	var carName1 = "Porsche 911"; // 双引号
	var carName2 = 'Porsche 911'; // 单引号

	document.getElementById("demo1").innerHTML =
		carName1 + " " + carName2;
}

function demo2() {
	var answer1 = "It's good to see you again!";
	var answer2 = "He is called 'Bill'";
	var answer3 = 'He is called "Bill"';

	document.getElementById("demo2").innerHTML =
		answer1 + "<br>" + answer2 + "<br>" + answer3;

}

function demo3() {
	var txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	document.getElementById("demo3").innerHTML = txt.length;
}
