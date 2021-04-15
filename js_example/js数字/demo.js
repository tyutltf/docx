function demo1() {
	var x = 123e5;
	var y = 123e-5;
	document.getElementById("demo1").innerHTML = x + "<br>" + y;
}

function demo2() {
	var x = 999999999999999;
	var y = 9999999999999999;
	document.getElementById("demo2").innerHTML = x + "<br>" + y;
}

function demo3() {
	var x = 0.2 + 0.1;
	document.getElementById("demo3").innerHTML = "0.2 + 0.1 = " + x;
}

function demo4() {
	var x = 0.2 + 0.1;
	document.getElementById("demo4").innerHTML = "0.2 + 0.1 = " + x;
	var y = (0.2 * 10 + 0.1 * 10) / 10;
	document.getElementById("demo5").innerHTML = "0.2 + 0.1 = " + y;
}

function demo5() {
	var myNumber = 2;
	var txt = "";
	while (myNumber != Infinity) {
		myNumber = myNumber * myNumber;
		txt = txt + myNumber + "<br>";
	}
	document.getElementById("demo6").innerHTML = txt;
}

function demo6() {
	var x = 0xFF;
	document.getElementById("demo7").innerHTML = "0xFF = " + x;
}

function demo7() {
	var myNumber = 32;
	document.getElementById("demo8").innerHTML =
		"32 = " + "<br>" +
		" Decimal " + myNumber.toString(10) + "<br>" +
		" Hexadecimal " + myNumber.toString(16) + "<br>" +
		" Octal " + myNumber.toString(4) + "<br>" +
		" Binary " + myNumber.toString(2);
}
