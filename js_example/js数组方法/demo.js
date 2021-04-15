function demo1() {
	var fruits = ["Banana", "Orange", "Apple", "Mango"];
	document.getElementById("demo1").innerHTML = fruits;
	fruits.push("Kiwi");
	document.getElementById("demo1").innerHTML = fruits;
}

function demo2() {
	var fruits = ["Banana", "Orange", "Apple", "Mango"];
	document.getElementById("demo2").innerHTML = fruits;
	fruits.pop();
	document.getElementById("demo3").innerHTML = fruits;
}

function demo3() {
	var fruits = ["Banana", "Orange", "Apple", "Mango"];
	document.getElementById("demo4").innerHTML = fruits.join(" * ");
}

function demo4() {
	var myGirls = ["Emma", "Isabella"];
	var myBoys = ["Jacob", "Michael", "Ethan"];
	var myChildren = myGirls.concat(myBoys);

	document.getElementById("demo5").innerHTML = myChildren;
}

function demo5() {
	var arr1 = ["Emma", "Isabella"];
	var arr2 = ["Jacob", "Michael", "Ethan"];
	var arr3 = ["Joshua", "Daniel"];

	var myChildren = arr1.concat(arr2, arr3);

	document.getElementById("demo6").innerHTML = myChildren;
}

function demo6() {
	var fruits = ["Banana", "Orange", "Apple", "Mango"];
	document.getElementById("demo7").innerHTML = "原数组：<br>" + fruits;
	fruits.splice(2, 0, "Lemon", "Kiwi");
	document.getElementById("demo8").innerHTML = "新数组：<br>" + fruits;
}

function demo7() {
	var fruits = ["Banana", "Orange", "Apple", "Mango"];
	document.getElementById("demo9").innerHTML = fruits;
	fruits.unshift("Lemon");
	document.getElementById("demo9").innerHTML = fruits;

}

function demo8(){
	var fruits = ["Banana", "Orange", "Apple", "Mango"];
	document.getElementById("demo10").innerHTML = fruits;
	fruits.shift();
	document.getElementById("demo11").innerHTML = fruits;
}