function chase()
{
	// passedTime variable represents a timelimit for user to get mouse pointer over image element
	while ( passedTime < 2000 )				
	{
		// go through all images and check if their visibility is hidden
		// if so, get onmouseover event from it
		var x = document.getElementById("imgBorderTop").style.visibility;
		if ( x === "hidden")
		{
			var mouseEvent = document.getElementById("imgBorderTop").onmouseover = function() { event };
		}
		else
		{
			var x = document.getElementById("imgBorderRight").style.visibility;
		}
		if ( x === "hidden")
		{
			var mouseEvent = document.getElementById("imgBorderRight").onmouseover = function() { event };
		}
		else
		{
			var x = document.getElementById("imgBorderBottom").style.visibility;
		}
		if ( x === "hidden")
		{
			var mouseEvent = document.getElementById("imgBorderLeft").onmouseover = function() { event };
		}
		else
		{
		var mouseEvent = false
		}
			
		chaseCounter++;
			
		endTime = new Date().getTime();
		passedTime = endTime - startTime;
	}
}