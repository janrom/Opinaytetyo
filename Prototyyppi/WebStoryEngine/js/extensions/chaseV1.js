(function (engine)
{
    "use strict";
 
    // A command is given the XML element that triggered the command
    // and a reference to the interpreter object:
    engine.commands.chase = function (command, interpreter)
    {
		var randVal = Math.floor((Math.random() * 3) + 1);
		
		function show_image(src) 
		{
			var img = document.createElement("img");
			img.src = src;			
			
			// This next line will just add it to the <body> tag
			document.body.appendChild(img);
		}
		
		randVal = 1;
		if ( randVal == 1)
		{
			show_image( "assets/images/borders/left2.png" );			
			show_image( "assets/images/borders/bottom2.png" );			
			show_image( "assets/images/borders/right2.png" );			
			show_image( "assets/images/borders/invisibleHorizontal.png" );			
		}
	
	
		/*
        // The UI tools offer equivalents to the browser's alert(), prompt() 
        // and confirm() functions that don't block further 
        // execution of JavaScript.
        engine.tools.ui.alert(
            interpreter,
            {
                title: "Hello extension says:",
                message: "Hello World!",
                doNext: true, // trigger next command after user clicked "ok"
                pause: true // prevent the game from running in the background
            }
        );
 
        // return an object with a "doNext" property that tells 
        // the interpreter to stop after executing this command:
        return {
            doNext: false
        };
		*/
    };
}(WSE));