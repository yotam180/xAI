<?php
session_start();
/*if(!isset($_SESSION["username"])){
    header("Location:index.php");
    exit();
}*/
if($_SERVER["REQUEST_METHOD"]!="GET"){
    header("Location:index.php");
    exit();
}
echo("<div id='count' style='display:none'>".$_GET["count"]."</div>");

?><center>
<h1>Time left for picture:6</h1> 
<img src = '' id='image' height='200' width='130'>
<br/>
<input type='text' id='tag' placeholder='Enter what you see'>
<input type='submit' value='send' onclick='send()'>
</center>
<script type='text/javascript'>
    function send()
    {
        var tag = document.getElementById("tag").value;
        if(tag=="")
        {
            document.getElementById("tag").placeholder = "You must enter value";
            return;
        }
        var text = httpGet("backend.php?tag="+tag);
        loop();
    }
    var files;
    function httpGet(url)
    {
        var xml = new XMLHttpRequest();
        xml.open("GET",url,false);
        xml.send(null);
        return xml.responseText;
    }
    function clock()
    {
        var time = document.getElementsByTagName("h1")[0];
        var content = time.innerText.split(":");
        time.innerText = content[0]+":"+parseFloat(content[1]-0.1).toString().slice(0,3);
        if(parseFloat(content[1])-0.1<=0.1)
            loop();
    }
    var c = setInterval(clock,100);
    setTimeout(start,500);
    function start()
    {
        var cont = httpGet("getFiles.php?count="+document.getElementById("count").innerText);
        files = JSON.parse(cont);
        loop();
    }
    function loop()
    {
        //Initializes text box after submit
        var textbox = document.getElementById("tag");
        textbox.value = "";
        textbox.placeholder = "Enter what you see";

        if(files.length==0)
        {
           // clearInterval(h);
            clearInterval(c);
            document.getElementsByTagName("h1")[0].innerText = "Game Over";
            document.getElementById("image").style = "display:none";    
            return;
        }
        loadImage(files[0])
        files.splice(0,1);
    }
    function loadImage(name)
    {
        document.getElementById("image").src = "images"+String.fromCharCode(92)+name;

        //setting the clock back to 6 seconds
        var time = document.getElementsByTagName("h1")[0];
        var content = time.innerText.split(":");
        time.innerText = content[0]+":6"
    }
</script>