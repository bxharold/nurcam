// getHeat.js

// Put static/getHeat.js inline so ctrl-R reloads the script w/o needing to clear the cache
// OR -- use cmd-shift-R
// No script tag inside src'ed js file.  

    function getAnswer(){
       $.ajax({
         type: "POST",
         headers: {
            'Content-Type': 'application/json' //Important: Send JSON data
         },
         url: "http://mc24b.local:5000/answer", 
         data: JSON.stringify({
            'a': $('#a').val(),
            'b': $('#b').val()
         }),
         success: (function (data) {
           console.log("getAnswer success:",data);
           $("#c").val(data["c"]  +1  );
         }), 
         error: (function (error) {
           alert("error", error) 
           console.log(error);
         })
       });
    };

    function getHeat(){
       $.ajax({
         type: "POST",
         url: "http://mc24b.local:5000/heat",
         contentType: 'application/json'
       }).done(function (data) {
         console.log(data);
         $("#timestamp").val(data["timestamp"]);
         $("#util").val(data["util"]);
         $("#temp").val(data["temp"]);
         $("#throttle").val(data["throttle"]);
         $("#ip").val(data["ip"]);
         $("#hostname").val(data["hostname"]);
       }).fail(function (error) {
         console.log(error);
       });
    }

