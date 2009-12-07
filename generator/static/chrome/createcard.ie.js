$(document).ready(function() { 
	//Fix IE label select bug
		$('#options li label').bind("click", function(){
		('input',this).click();
    });
});
