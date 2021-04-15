function demo1() {
	document.getElementById("demo1").innerHTML = Math.PI;
}

function demo2() {
	document.getElementById("demo2").innerHTML = Math.round(4.4);
}

function demo3() {
	document.getElementById("demo3").innerHTML = Math.pow(8, 2);
}

function demo4() {
	document.getElementById("demo4").innerHTML = Math.sqrt(64);
}

function demo5() {
	document.getElementById("demo5").innerHTML = Math.abs(-4.4);
}

function demo6() {
	// document.getElementById("demo6").innerHTML = Math.ceil(4.4);
	document.getElementById("demo6").innerHTML = Math.floor(4.4);
}

function demo7() {
	document.getElementById("demo7").innerHTML =
		"The sine value of 90 degrees is " + Math.sin(90 * Math.PI / 180);

	document.getElementById("demo7").innerHTML =
		"The cosine value of 0 degrees is " + Math.cos(0 * Math.PI / 180);
}

function demo8() {
	document.getElementById("demo8").innerHTML =
		Math.max(0, 150, 30, 20, -8, -200);

	document.getElementById("demo8").innerHTML =
		Math.min(0, 150, 30, 20, -8, -200);
}

function convert(degree) {
	var x;
	if (degree == "C") {
		x = document.getElementById("c").value * 9 / 5 + 32;
		document.getElementById("f").value = Math.round(x);
	} else {
		x = (document.getElementById("f").value - 32) * 5 / 9;
		document.getElementById("c").value = Math.round(x);
	}
}
