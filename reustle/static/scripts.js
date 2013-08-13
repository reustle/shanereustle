$(function(){

	$('.howdy_link').hover(function(){
		$('.avatar').addClass('cowboy');
	}, function(){
		$('.avatar').removeClass('cowboy');
	}).click(function(){
		// Prevents # from being added to url
		return false;
	});
	
});

