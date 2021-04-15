function demo1() {
	var x = 123;

	document.getElementById("demo1").innerHTML =
		x.valueOf() + "<br>" +
		(123).valueOf() + "<br>" +
		(100 + 23).valueOf();
}

function demo2() {
	var x = 9.656;
	document.getElementById("demo2").innerHTML =
		x.toExponential() + "<br>" +
		x.toExponential(2) + "<br>" +
		x.toExponential(4) + "<br>" +
		x.toExponential(6);
}

function demo3() {
	var x = 9.656;
	document.getElementById("demo3").innerHTML =
		x.toFixed(0) + "<br>" +
		x.toFixed(2) + "<br>" +
		x.toFixed(4) + "<br>" +
		x.toFixed(6);
}

function demo4() {
	var x = 9.656;
	document.getElementById("demo4").innerHTML =
		x.toPrecision() + "<br>" +
		x.toPrecision(2) + "<br>" +
		x.toPrecision(4) + "<br>" +
		x.toPrecision(6);
}

function demo5() {
	document.getElementById("demo5").innerHTML =
		Number(true) + "<br>" +
		Number(false) + "<br>" +
		Number("10") + "<br>" +
		Number("  10") + "<br>" +
		Number("10  ") + "<br>" +
		Number(" 10  ") + "<br>" +
		Number("10.33") + "<br>" +
		Number("10,33") + "<br>" +
		Number("10 33") + "<br>" +
		Number("John");
}

function demo6() {
	document.getElementById("demo6").innerHTML =
		parseInt("10") + "<br>" +
		parseInt("10.33") + "<br>" +
		parseInt("10 6") + "<br>" +
		parseInt("10 years") + "<br>" +
		parseInt("years 10");
}
