
$(document).ready(function() { 
		
				
		$('#message_field textarea').keyup( function() {
			$('#message').text($(this).val());
		});
		
		$('#fromname_field input').keyup( function() {
			$('#name').html($(this).val());
		});
		
		$('#fromemail_field input').keyup( function() {
			$('#email').html($(this).val());
		});
		
		
		$('#typeface_field label').click( function() {
			$('#message').css('font-family', $(this).css('font-family'));
		})
		
		$('#picture_field label').click( function() {
			$('#picture').attr('src', $(this).find('img').attr('rel'))
		})
	
		$('#border_field label').click( function() {
			$('#border').attr('src', $(this).find('img').attr('rel'))
		})

		
});
