// go to new round if event happened and counter is not reached
if ( mouseEvent === true && chaseCounter < 5)
{
	document.createElement("<goto scene="chase" />");
}
// go to successful scene 
else if (  mouseEvent === true && chaseCounter > 5)
{
	document.createElement("<goto scene="chaseSuccessForestPeople" />");
}
// go to failure scene
else
{
	document.createElement("<goto scene="chaseFailureForestPeople" />");
}					