
$(document).ready(function() { 
		
		if(typeof document.body.style.maxHeight === "undefined"){ 
			//You're using IE6
		}
		else {
			$('.disabled-default').show();
			$('#msg').hide();
			$('#createcard').wrap('<form action="" method="POST"></form>');
			$('#rightcol').append('<input type="image" src="/static/chrome/send.png" id="sendbutton">');
	
	
			function set_typeface(selected){
				$('textarea').css('font-family', $(selected).css('font-family'));
			}
			
			function set_picture(selected){
				$('#picture').attr('src', $(selected).find('img').attr('rel'))
			}
			
			function set_border(selected){
				$('.bowpreviews').css('background-image', 'url(' + $(selected).find('img').attr('rel') + ')' )
			}
			

			
			$('#typeface_field label').click( function() {
				set_typeface(this);
			})
			
			$('#picture_field label').click( function() {
				set_picture(this);
			})
		
			$('#border_field label').click( function() {
				set_border(this);
			})
			
			
			
			/* $('#border_field input:radio').filter(':checked').ready( function() {
				set_border(this);
			}) */
		
		}
});
