//Example of a custom action:
//Shakes the game container from left to right multiple times.
//The given option lets us determine how broad the shaking should be.
//Example usage: <<screenshake 10>>
var executeScreenshakeAction = function(action)
{
  //Actions can have an impact on any element of the page and any variable in the code. Do wild stuff.
  //Remember, great power, great responsibility (...I mean it's easy to break stuff too).
  var element = $("#container");

  //Parse the first option as an integer
  var strength = parseInt(action.options[0]);

  //Multiple jQuery animations will be (b r u t a l l y) queued.
  element.animate({
    "left":strength+"px"
  }, 50);
  element.animate({
    "left":-strength+"px"
  }, 100);
  element.animate({
    "left":strength+"px"
  }, 100);
  element.animate({
    "left":-strength+"px"
  }, 100);
  element.animate({
    "left":strength+"px"
  }, 100);
  element.animate({
    "left":-strength+"px"
  }, 100);
  element.animate({
    "left":"0px"
  }, 50);
}

//Custom action for tension-based shaking
//Applies escalating shake animations based on intensity level
//Usage: <<shake light>> <<shake medium>> <<shake heavy>>
var executeShakeAction = function(action)
{
  var intensity = action.options[0];
  if(!intensity)
  {
    console.error("Shake action requires an intensity parameter: light, medium, or heavy");
    return;
  }

  intensity = intensity.toLowerCase();
  var validIntensities = ["light", "medium", "heavy"];
  if(validIntensities.indexOf(intensity) === -1)
  {
    console.error("Invalid shake intensity: "+intensity+". Use: light, medium, or heavy");
    return;
  }

  var className = "shake-" + intensity;
  var element = $("#container");

  //Remove any existing shake animation
  element.removeClass("shake-light shake-medium shake-heavy");

  //Apply the new animation
  element.addClass(className);

  //Determine animation duration and remove class after it completes
  var duration = 0;
  switch(intensity)
  {
    case "light":
      duration = 400;
      break;
    case "medium":
      duration = 600;
      break;
    case "heavy":
      duration = 800;
      break;
  }

  //Remove the animation class after it completes so it can be triggered again
  setTimeout(function()
  {
    element.removeClass(className);
  }, duration);
};

//Add functions to execute your custom actions here!
/*
var myCustomAction = function(action)
{ 
  //Do something here?
}
*/

var myCustomAction = function(action)
{ 
  //Do something here?
}

//A dictionary of all the known custom actions, and the function they call when they're executed.
//Don't forget to add your own "name":function pairs here, too!
var customActions = {
  "screenshake":executeScreenshakeAction,
  "shake":executeShakeAction,
  /* "custom":myCustomAction, */
}