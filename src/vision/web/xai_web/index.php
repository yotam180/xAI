<html>
<head>
    <title>xAI</title>
    <?php require_once("include.php"); ?>

    <link rel="StyleSheet" type="text/css" href="style/index.css"></link>

    <script>
        $(document).ready(function() {
            var newsbar = $(".newsbar");

            newsbar.hide();
            newsbar = newsbar.toArray();
            $(newsbar[0]).show();

            var newsid = 0;
            setInterval(function() {
                $(newsbar[newsid++ % newsbar.length]).hide("slide", {direction: "left"}, 1500);
                $(newsbar[newsid % newsbar.length]).show("slide", {direction: "right"}, 1500);
            }, 10000);

            $("#vid_frame").on("load", function() {
                $(this).show();

                let hidestatic = function() {
                    $("#alt_back_brain").fadeOut(3000);
                    setTimeout(showstatic, 20000);
                };
                let showstatic = function() {
                    $("#alt_back_brain").fadeIn(3000);
                    setTimeout(hidestatic, 20000);
                };
                
                setTimeout(hidestatic, 3000);
            });
        });
    </script>
</head>
<body>

<?php require("header.php"); ?>

<div class="section">
    <div id="alt_back_brain">&nbsp;</div>
    <iframe id="vid_frame" src="https://www.youtube.com/embed/dAIQeTeMJ-I?autoplay=1&controls=0&showinfo=0&autohide=1&modestbranding=1&loop=1&playlist=dAIQeTeMJ-I" allowfullscreen>
    </iframe>
    <div id="main_title" class="newsbar shown">
        <h1 style="vertical-align: middle"><img id="main_logo" src="img/logo_light.png" /><i> A research project in the field of machine learning</i></h1>
        <span style="display: inline-block; width: 15vw;">&nbsp;</span><strong>xAI&trade;</strong> is a tool for developers that provides an easy interface for working with neural networks for image classification and manipulation. Read more...
    </div>
    <div id="main_title2" class="newsbar">
        <h1 style="vertical-align: middle"><img id="main_logo" src="img/logo.png" /><i> 2 A research project in the field of machine learning</i></h1>
        <span style="display: inline-block; width: 15vw;">&nbsp;</span><strong>xAI&trade;</strong> is a tool for developers that provides an easy interface for working with neural networks for image classification and manipulation. Read more...
    </div>
</div>

<div class="section">

</div>

</body>
</html>