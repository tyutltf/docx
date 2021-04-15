function demo1() {
	var cars = [
		"Audi",
		"BMW",
		"porsche"
	];
	document.getElementById("demo1").innerHTML = cars;
}

function demo2() {
	var cars = ["Audi", "BMW", "porsche"];
	document.getElementById("demo2").innerHTML = cars[0];
}

function demo3() {
	var cars = ["Audi", "BMW", "porsche"];
	cars[0] = "Volvo";
	document.getElementById("demo3").innerHTML = cars;
}

function demo4() {
	var fruits, text, fLen, i;
	fruits = ["Banana", "Orange", "Apple", "Mango"];
	fLen = fruits.length;

	text = "<ul>";
	for (i = 0; i < fLen; i++) {
		text += "<li>" + fruits[i] + "</li>";
	}
	text += "</ul>";
	console.log(text)
	document.getElementById("demo4").innerHTML = text;
}

function demo5() {
	var fruits, text, fLen, i;
	fruits = ["Banana", "Orange", "Apple", "Mango"];
	fruits[6] = "Lemon";

	fLen = fruits.length;
	text = "";
	for (i = 0; i < fLen; i++) {
		text += fruits[i] + "<br>";
	}
	document.getElementById("demo5").innerHTML = text;
}
