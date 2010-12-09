
$(document).ready(function() { 
		
		if(typeof document.body.style.maxHeight === "undefined"){ 
			//You're using IE6
		}
		else {
			$('.disabled-default').show();
			$('#msg').hide();
			
			//Hide form stuff from non-JS bots
			$('#createcard').wrap('<form action="" method="POST"></form>');
			$('#createcard').append('<input type="image" src="/static/chrome/clear.gif" height="40" width="90" id="sendbutton">');

			//Live Preview Code
			
			function set_picture(selected){
				$('#picture').attr('src', $(selected).find('img').attr('rel'))
			}			
			
			$('#picture_field label').click( function() {
				set_picture(this);
			})
			
			// If there are fields selected when the form loads, show the preview of the selection
			$('input:radio:checked').click(); 		
				
			$('textarea').focus(); // Put the cursor in the text box
		}
});
