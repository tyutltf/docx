function demo1() {
	var d = new Date();
	document.getElementById("demo1").innerHTML = d;
}

function demo2() {
	var d = new Date();
	document.getElementById("demo2").innerHTML = d.getFullYear();
}

function demo3() {
	var d = new Date();
	document.getElementById("demo3").innerHTML = d.getTime();
}

function demo4() {
	var d = new Date();
	d.setFullYear(2020);
	document.getElementById("demo4").innerHTML = d;
}

function demo5() {
	var d = new Date();
	document.getElementById("demo5").innerHTML = d.toUTCString();
}

function demo6() {
	var d = new Date();
	document.getElementById("demo6").innerHTML = d.getDay();
}

function demo7() {
	var d = new Date();
	var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
	document.getElementById("demo7").innerHTML = days[d.getDay()];
}
