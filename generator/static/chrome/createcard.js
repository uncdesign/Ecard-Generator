
$(document).ready(function() { 
		
		if(typeof document.body.style.maxHeight === "undefined"){ 
			//You're using IE6
		}
		else {
			$('.disabled-default').show();
			$('#msg').hide();
			$('#createcard').wrap('<form action="" method="POST"></form>');
			$('#rightcol').append('<input type="image" src="/static/chrome/send.png" id="sendbutton">');
			
			
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
				$('textarea').css('font-family', $(this).css('font-family'));
			})
			
			$('#picture_field label').click( function() {
				$('#picture').attr('src', $(this).find('img').attr('rel'))
			})
		
			$('#border_field label').click( function() {
				$('.bowpreviews').css('background-image', 'url(' + $(this).find('img').attr('rel') + ')' )
			})

		}
});
