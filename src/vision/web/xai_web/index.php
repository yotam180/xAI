<html>
<head>
    <title>xAI</title>
    <?php require_once("include.php"); ?>

    <link rel="StyleSheet" type="text/css" href="style/index.css"></link>

    <script>

        jQuery.fn.extend({
            onscroll: function(el, callback) {
                $(this).addClass("scroll_show");
                $(this).attr("scroll-el", el);
                $(this).on("scrolled_to", callback);
            }
        });

        $(document).ready(function() {
            var newsbar = $(".newsbar");

            newsbar.hide();
            newsbar = newsbar.toArray();
            $(newsbar[0]).show();

            var newsid = 0;
            let nextnews = function() {
                $(newsbar[newsid++ % newsbar.length]).hide("slide", {direction: "left"}, 1500);
                $(newsbar[newsid % newsbar.length]).show("slide", {direction: "right"}, 1500, function() {
                    setTimeout(nextnews, 7000);
                });
            };
            nextnews();

            $("#vid_frame").on("load", function() {
                $(this).show();

                let hidestatic = function() {
                    $("#alt_back_brain").stop(true, true).fadeOut(3000, function() {
                        setTimeout(showstatic, 20000);
                    });
                };
                let showstatic = function() {
                    $("#alt_back_brain").stop(true, true).fadeIn(3000, function() {
                        setTimeout(hidestatic, 20000);
                    });
                };

                setTimeout(hidestatic, 3000);
            });

            $(document).scroll(function() {
                $("[class='scroll_show']").each(function(idx) {
                    if (window.scrollY > $($(this).attr("scroll-el")).offset().top - window.innerHeight / 2) {
                        $(this).trigger("scrolled_to");
                        $(this).removeClass("scroll_show");
                    }
                    /*else {
                        if ($(this).is(":visible"))
                            $(this).fadeOut();
                    }*/
                });
            });

            $("#sec2title").onscroll("#section2", function() {
                $(this).fadeIn(2000);
            });
            $("#sec2explanation").onscroll("#section2", function() {
                $(this).show("slide", {direction: "left"}, 2000);
            });
            $("#sec2img").onscroll("#section2", function() {
                $(this).show("slide", {direction: "right"}, 1500);
                let el = $(this);
                setTimeout(function() {
                    $({blur: 2}).animate({blur: 0}, {
                        duration: 2000,
                        easing: "swing",
                        step: function() {
                            el[0].style.filter = "blur(" + this.blur + "px)";
                        }
                    })
                }, 1500);
            });

            $("#sec3title").onscroll("#section3", function() {
                $(this).fadeIn(2000);
            });
            $("#sec3explanation").onscroll("#section3", function() {
                $(this).show("slide", {direction: "right"}, 2000);
            });
            $("#sec3img").onscroll("#section3", function() {
                $(this).show("slide", {direction: "left"}, 1500);
            });

            $("#sec4explanation").onscroll("#section3", function() {
                $(this).show("slide", {direction: "left"}, 2000);
            });
            $("#sec4img").onscroll("#section3", function() {
                $(this).show("slide", {direction: "right"}, 1500);
            });

            $("#sec5title").onscroll("#section5", function() {
                $(this).fadeIn(2000);
            });
            $("#sec5panel").onscroll("#section5", function() {
                $(this).show("slide", {direction: "up"}, 1500);
            });

            $("#sec6title").onscroll("#section6", function() {
                $(this).fadeIn(2000);
            });
            $("#sec6panel").onscroll("#section6", function() {
                $(this).show("slide", {direction: "up"}, 1500);
            });
        });
    </script>
</head>
<body>

<?php require("header.php"); ?>

<div id="section1" class="section">
    <div id="alt_back_brain">&nbsp;</div>
    <iframe id="vid_frame" src="https://www.youtube.com/embed/dAIQeTeMJ-I?autoplay=1&controls=0&showinfo=0&autohide=1&modestbranding=1&loop=1&playlist=dAIQeTeMJ-I" allowfullscreen>
    </iframe>
    <div id="main_title" class="newsbar shown">
        <h1 style="vertical-align: middle"><img id="main_logo" src="img/logo_light.png" /><i> A research project in the field of machine learning</i></h1>
        <span style="display: inline-block; width: 15vw;">&nbsp;</span><strong>xAI&trade;</strong> is a tool for developers that provides an easy interface for working with neural networks for image classification and manipulation. Read more...
    </div>
    <div id="main_title2" class="newsbar">
        <h1 style="vertical-align: middle"><img id="main_logo" src="img/github.png" /><i> xAI is Open Source!</i></h1>
        <span style="display: inline-block; width: 15vw;">&nbsp;</span><strong>xAI&trade;</strong> You can find our source code for the networks, dataset gathering system and web servers on our github <a href="https://github.com/yotam180/xAI/">here</a>
    </div>
</div>

<div id="section2" class="section white_gradient">
    <div id="sec2title" style="position: relative; left: 10vw; width: 75vw; top: 10vh; color: white; z-index: 10; background-color: #2884b7; padding: 20px; font-size: 4.5vh;"><strong>What's <img src="img/logo_light.png" style="display: inline; height: 1em;" />?</strong></div>
    <div id="sec2explanation" style="text-align: justify; text-justify: inter-word; padding: 5vh; float: left; position: relative; left: 10vw; width: 20vw; top: 5vh; height: 70vh; background-color: transparent;">
        xAI&trade; is a research project to demonstrate the usage of Neural Networks in the field of Machine Learning, and expresses Deep Learning technologies in the form of image recognition. 
        <br/><br/>
        The project is an API for developers for image classification and style transfer, creating &amp; gathering datasets and training new networks.
        <br/><br/>
        We provide a RESTful API using HTTP for developers from all languages.
    </div>
    <div id="sec2img" style="float: right; position: relative; left: -5vw; width: 60vw; top: 5vh; height: 70vh; background-color: transparent; background-image: url('img/img2.jpg'); background-size: 100% auto; background-repeat: repeat-x; filter: blur(2px);">&nbsp;</div>
</div>

<div id="section3" style="height: 200vh !important;" class="section white_gradient_m">
    <div id="sec3title" style="position: relative; left: 15vw; width: 75vw; top: 10vh; color: white; z-index: 10; background-color: #5c28b7; padding: 20px; font-size: 4.5vh;"><strong>Our Products</strong></div>
    <div id="sec3explanation" style="text-align: justify; text-justify: inter-word; padding: 5vh; float: right; position: relative; right: 10vw; width: 20vw; top: 5vh; height: 70vh; background-color: transparent;">
        <h2 style="color: turquoise; padding: 2vh;">Style Transfer</h2>
        <strong>TRANSFORM IMAGES INTO ART USING ARTIFICIAL INTELLIGENCE.</strong>
        <br/><br/>
        Re-style your images with ease! Select an image to process, and easily change its style using our simple-to-use REST API.
        <br/><br/>
        <a href="style.php">Read more...</a>
    </div>
    <div id="sec3img" style="float: left; position: relative; right: -5vw; width: 60vw; top: 5vh; height: 70vh; background-color: transparent; background-image: url('img/styles.jpg'); background-size: 100% auto; background-repeat: repeat-x;">&nbsp;</div>

    <div id="sec4explanation" style="text-align: justify; text-justify: inter-word; padding: 5vh; float: left; position: relative; left: 10vw; width: 20vw; top: 5vh; height: 70vh; background-color: transparent;">
        <h2 style="color: #cd5c5c; padding: 2vh;">Image Classification</h2>
        <strong>CREATE YOUR OWN TOOLS FOR TRANSFORMING IMAGES TO DATA.</strong>
        <br/><br/>
        Easily create datasets and train classifiers to identify images in objects using our easy to understand, easy to implement method we offer and our APIs.
        <br/><br/>
        <a href="classify.php">Read more...</a>
    </div>
    <div id="sec4img" style="float: right; position: relative; left: -5vw; width: 60vw; top: 5vh; height: 70vh; background-color: transparent; background-image: url('img/digits.png'); background-size: 100% auto; background-repeat: repeat-x;">&nbsp;</div>
</div>

<div id="section5" class="section white_gradient">
    <div id="sec5title" style="position: relative; left: 10vw; width: 75vw; top: 10vh; color: white; z-index: 10; background-color: #2dcc8f; padding: 20px; font-size: 4.5vh;"><strong>Live Demo</strong></div>
    <div id="sec5panel" style="position: relative; left: 15vw; top: 10vh; height: 55vh; width: 65vw; background-image: url('img/styles.jpg');"><br/><br/><br/><h1 style="text-align: center; background-color: rgba(0, 0, 128, 0.5); color: white;">Not yet "live"</h1></div>
</div>

<div id="section6" class="section red_gradient_m">
    <div id="sec6title" style="position: relative; left: 10vw; width: 75vw; top: 10vh; color: white; z-index: 10; background-color: #f20729; padding: 20px; font-size: 4.5vh;"><strong>Log in / Sign Up</strong></div>
    <div id="sec6panel" style="position: relative; left: 15vw; top: 10vh; height: 55vh; width: 65vw; background-image: url('img/styles.jpg');"><br/><br/><br/><h1 style="text-align: center; background-color: rgba(0, 0, 128, 0.5); color: white;">To be implemented</h1></div>
</div>

</body>
</html>