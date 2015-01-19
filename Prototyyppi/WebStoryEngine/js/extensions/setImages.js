function setImages()
{
	// random value between 1 and 4
	var randVal = Math.floor((Math.random() * 4) + 1);
			
	// set image element hidden depending on random value
	if ( randVal === 1 )
	{
		document.getElementById("imgBorderTop").style.visibility = "hidden";
	}
	else if ( randVal === 2 )
	{
		document.getElementById("imgBorderRight").style.visibility = "hidden";
	}
	if ( randVal === 3 )
	{
		document.getElementById("imgBorderBottom").style.visibility = "hidden";
	}
	if ( randVal === 4 )
	{
		document.getElementById("imgBorderLeft").style.visibility = "hidden";
	}
}