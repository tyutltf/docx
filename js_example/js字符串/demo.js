function demo1() {
	var carName1 = "Porsche 911"; // 双引号
	var carName2 = 'Porsche 911'; // 单引号

	document.getElementById("demo1").innerHTML =
		carName1 + " " + carName2;
}

function demo2() {
	var answer1 = "It's good to see you again!";
	var answer2 = "He is called 'Bill'";
	var answer3 = 'He is called "Bill"';

	document.getElementById("demo2").innerHTML =
		answer1 + "<br>" + answer2 + "<br>" + answer3;

}

function demo3() {
	var txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	document.getElementById("demo3").innerHTML = txt.length;
}

function demo4() {
	var str = "The full name of China is the People's Republic of China.";
	var pos = str.indexOf("China");
	document.getElementById("demo4").innerHTML = pos;
}

function demo5() {
	var str = "The rain in SPAIN stays mainly in the plain";
	var res = str.match(/ain/g);
	document.getElementById("demo5").innerHTML = res;
}

function demo6() {
	var str = document.getElementById("demo6").innerHTML;
	var txt = str.replace("Microsoft", "W3School");
	document.getElementById("demo6").innerHTML = txt;
}

function demo7() {
	var text = document.getElementById("demo7").innerHTML;
	document.getElementById("demo7").innerHTML = text.toUpperCase();
}

function demo8() {
	var text = document.getElementById("demo8").innerHTML;
	document.getElementById("demo8").innerHTML = text.toLowerCase();
}

function demo9() {
	var str = "a,b,c,d,e,f";
	var arr = str.split(",");
	document.getElementById("demo9").innerHTML = arr[0];
}
