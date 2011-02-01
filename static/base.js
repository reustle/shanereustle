$("#email_btn").attr("href","#/").click(function(){
	$("#wrapper").animate({
		marginTop: "6%"
	},1000)
	
	$("#details").fadeOut("slow")
	$("#links").fadeOut("slow", function(){
		$("#email_form").fadeIn("fast")
	})
})

$("#send_email").click(function(){
	// Show user that something is happening
	
	$.post("/email/", {"name":$("#name").val(), "email":$("#email").val(), "phone":$("#phone").val(), "message":$("#message").val()}, function(response){
		if(response == "1"){
			alert("Email sent!")
			hide_form()
		}else{
			alert("Email failed!")
		}
	})
})

function hide_form(){
	$("#wrapper").animate({
		marginTop: "12%"
	},1000)
	
	$("#email_form").fadeOut("slow", function(){
		$("#details").fadeIn("fast")
		$("#links").fadeIn("fast")
	})
}

$("#cancel_btn").click(hide_form)

// Clear form field text on focus
$("#email_form input, #email_form textarea").focus(function(){
	if($(this).val() == $(this)[0].defaultValue && ($(this).attr("type") == "text" || $(this).attr("type") == "textarea") ){
		$(this).val("")
	}
})

