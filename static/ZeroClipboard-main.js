$(document).ready(function() {
ZeroClipboard.config({ swfPath: "../static/ZeroClipboard.swf" });
var client = new ZeroClipboard( document.getElementById("coupon-copy-button") );

client.on( "ready", function( readyEvent ) {
  // alert( "ZeroClipboard SWF is ready!" );

  client.on( "aftercopy", function( event ) {
    // `this` === `client`
    // `event.target` === the element that was clicked
   // event.target.style.display = "none";
    alert("Copied text to clipboard: " + event.data["text/plain"] );
  } );
} );

});