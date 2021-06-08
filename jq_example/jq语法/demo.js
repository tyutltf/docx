$(document).ready(function() {
	$("button.1").click(function() {
		$(this).hide();
	});
});

$(document).ready(function() {
	$("button.2").click(function() {
		$("p.2").hide();
	});
});

$(document).ready(function() {
	$("button.3").click(function() {
		$("#div1").fadeOut();
		$("#div2").fadeOut("slow");
		$("#div3").fadeOut(3000);
	});
});

$(document).ready(function() {
	$("p.3").click(function() {
		$(this).hide();
	});
});

$(document).ready(function() {
	$(".ex .hide").click(function() {
		$(this).parents(".ex").hide("slow");
	});
});

$(document).ready(function() {
	$(".flip").click(function() {
		$(".panel").slideToggle("slow");
	});
});


$(document).ready(function() {
	$("button").click(function() {
		var div = $(".div1");
		div.animate({
			height: '300px',
			opacity: '0.4'
		}, "slow");
		div.animate({
			width: '300px',
			opacity: '0.8'
		}, "slow");
		div.animate({
			height: '100px',
			opacity: '0.4'
		}, "slow");
		div.animate({
			width: '100px',
			opacity: '0.8'
		}, "slow");
	});
});
