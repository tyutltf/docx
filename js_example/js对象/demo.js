function demo1() {
	// 创建对象：
	var car = {
		type: "porsche",
		model: "911",
		color: "white"
	};

	// 显示对象中的数据：
	document.getElementById("demo1").innerHTML = car.type;
}

function demo2() {
	// 创建对象：
	var person = {
		firstName: "Bill",
		lastName: "Gates",
		id: 12345
	};

	// 显示对象中的数据：
	document.getElementById("demo2").innerHTML =
		person.firstName + " " + person.lastName;
}

function demo3() {
	// 创建对象：
	var person = {
		firstName: "Bill",
		lastName: "Gates",
		id: 12345
	};

	// 显示对象中的数据：
	document.getElementById("demo3").innerHTML =
		person["firstName"] + " " + person["lastName"];
}

function demo4() {
	// 创建对象：
	var person = {
		firstName: "Bill",
		lastName: "Gates",
		id: 12345,
		fullName: function() {
			return this.firstName + " " + this.lastName;
		}
	};

	// 显示对象中的数据：
	document.getElementById("demo4").innerHTML = person.fullName();
}

function demo5() {
	// 创建对象：
	var person = {
		firstName: "Bill",
		lastName: "Gates",
		id: 12345,
		fullName: function() {
			return this.firstName + " " + this.lastName;
		}
	};

	// 显示对象中的数据：
	document.getElementById("demo5").innerHTML = person.fullName;
}
