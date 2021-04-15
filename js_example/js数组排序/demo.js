function demo1() {
	var fruits = ["Banana", "Orange", "Apple", "Mango"];
	document.getElementById("demo1").innerHTML = fruits;
	// fruits.sort();
	fruits.reverse();
	document.getElementById("demo1").innerHTML = fruits;

}

function demo2() {
	var points = [40, 100, 1, 5, 25, 10];
	document.getElementById("demo2").innerHTML = points;
	points.sort(function(a, b) {
		return a - b
	});
	document.getElementById("demo2").innerHTML = points;
}
