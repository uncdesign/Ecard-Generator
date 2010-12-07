function rand(l,u) // lower bound and upper bound
{
	return Math.floor((Math.random() * (u-l+1))+l);
}

$(document).ready(function() { 

	$("#id_message").change( function() {
		var swears = new Array("Shit","Piss","Fuck","Cunt","Cocksucker","Motherfucker","Tits");
		var replacements = new Array("****", "!!!!","!@*^%$","bells","chimney","eggnog","frosty","jolly","snow","elves","cranberry sauce","mistletoe","North Pole","sled","snowflake","tinsel","wrapping paper");
		var messagetxt = $(this).val();
		for(i=0;i<swears.length;i++){	
			swearsearch = new RegExp(swears[i],"gi")
			messagetxt = messagetxt.replace(swearsearch,replacements[rand(0,replacements.length-1)])
		}
		$(this).val(messagetxt);
	});

});
