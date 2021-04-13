function demo1() {
	document.getElementById("demo1").innerHTML = "Hello World!";
}

function demo2(name, job) {
	document.getElementById("demo2").innerHTML = "Welcome " + name + ", the " + job + ".";
}

function demo3(txt) {
	document.getElementById("demo3").innerHTML = txt
}

function demo4(a, b) {
	return a * b;
}

function toCelsius(f) {
	return (5 / 9) * (f - 32);
}
