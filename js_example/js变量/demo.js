function demo1() {
	var price1 = 7;
	var price2 = 8;
	var price3 = 12;
	var total = price1 + price2 + price3;
	document.getElementById("demo1").innerHTML = "总计：" + total;
}

function demo2() {
	var pi = 3.14;
	var person = "Bill Gates";
	var answer = 'How are you!';

	document.getElementById("demo2").innerHTML =
		pi + "<br>" + person + "<br>" + answer;
}

function demo3() {
	var person = "Bill Gates",
		carName = "porsche",
		price = 150000;
	document.getElementById("demo3").innerHTML = carName;
}

function demo4() {
	var carName;
	document.getElementById("demo4").innerHTML = carName;
}

function demo5() {
	x = "8" + 3 + 5;
	document.getElementById("demo5").innerHTML = x;
}

function demo6() {
	var x = 3 + 5 + "8"
	document.getElementById("demo6").innerHTML = x;
}
