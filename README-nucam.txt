3/8/2025
Project nucam... status and findings:
== util_functions.py can run as a standalone flask app, useful for testing. 
it's easy to add a decorator to invoke a function in a route
e.g., http://mc24b.local:5003/cpu_temp
      http://mc24b.local:5003/hello/CatFeeder
      http://mc24b.local:5003/jsontests/dict
==
<LI> - buttons: "Take Picture", "start stream", "kill stream", "movie"
<LI> - button to display temperature and CPU utilization
<LI> - class camstream with methods start, kill, take picture, movie
<LI> - vid 640x480.  pic 1024x768 (.7M), max 1920x1080 (1.6M)
<LI> - vid stream capture is choppy on mc24b. Maybe because pi3? Slow card?
<LI> - factor out dup header code ("jinja template inheritance")
<LI> o put this onto github
<LI> o use picamera2 for bookworm(12)
<LI> o monitor temperature in a thread/timer (planetA?)

== for button to act like <a>, use `<button type="button" onClick=...` Or use img or text.

== Put static/getHeat.js inline, then ctrl-R refreshes the script w/o clearing the cache. 
No script tag inside src'ed js file.  
Ctrl-shift-del to get to the settings page where I can clear browsing data/cached images and files... which include the js file I'm working on. 

nucam... errors that were weird, and that led me down a stupid path.

I wanted to avoid repeating the JS "status" function... 
so template inheritance...
BUT the simple nav buttons on nucam.html didn't work.
... <button onClick='javascript:window.location.href="/refresh"'> page refresh </button>
Took a while to find out I needed "type='button'"

I thought I had to split the js into a separate file, so I did.
That led to more debugging, but it was not a solution. 

I still haven't figured out the server error, where "answer" was 
being called with no data. 

Now I have the js split as a dangling open design question. Do I want it?
... getHeat.js has the 2 JS functions I was using for testing.
Ctrl-R doesn't reload the static js file.  With inline js, ctrl-R 
refreshes the "cached" static.  It was something to be learned...
but in a small app like this, decoupling doesn't simplfy development.

More important -- 
  call the mc24b dev to a close.  yes. call it nrcam for now.
    Then, do some renaming so that nucam IS the project name.
    dev-nucam? Nucam-dev? 
  Take some pictures of the nunias...
    put nrcam on a legacy camera bullseye(11) with a battery. (zd)
    python picamera_stream.py  streams to port 8000.  Test it.
    use the GoPro.
  Repo the stuff on github; get used to that.
  Use vscode not vi. 
    On pi400 or pi500, mod the code to use mc24b as a camera feed. 
  Make a bookworm(12) microsd card and get picamera2 demo working.
    I can get a start on a pizero or mc24b -- both have a camera.
    If I don't have another pi3, swap out the sd card.
    Don't mess with zc.  I'll still want that for our trip.

