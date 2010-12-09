$(document).ready(function() { 
	//Fix IE label select bug
		$('#picture_field li label').bind("click", function(){
		('input',this).click();
    });
});
