function demo1() {
	document.getElementById("demo1").innerHTML = Math.random();
}

function demo2() {
	document.getElementById("demo2").innerHTML =
		Math.floor(Math.random() * 10);
}

function demo3() {
	document.getElementById("demo3").innerHTML =
		Math.floor(Math.random() * 10) + 1;
}

function demo4(min,max) {
	var res = Math.floor(Math.random() * (max - min + 1)) + min;
	document.getElementById('demo4').innerHTML = res
}
