<script type="text/javascript">

    let scroll = function(anchorid) {
        $("html,body").animate({scrollTop: $(anchorid).offset().top}, "slow");
    }

    $(document).ready(function() {
        let folded = false;

        $(".menu_btn").mouseenter(function() {
            $(".menu_btn")
                .stop(true, true)
                .animate({backgroundColor: "transparent"}, "fast");

            $(this)
                .stop(true, true)
                .animate({backgroundColor: $(this).attr("oc")}, "fast");

            $(".header,.header_folded")
                .stop(true, true)
                .animate({backgroundColor: $(this).attr("ec")}, "slow");
            
                setTimeout(function() {
                    $(".top_logo,.top_logo_folded").attr("src", "img/logo.png");
                }, 500);
        });

        $(".header,.header_folded").mouseleave(function() {
            $(".menu_btn")
                .stop(true, true)
                .animate({backgroundColor: "transparent"}, "fast");

            $(".header,.header_folded")
                .stop(true, true)
                .animate({backgroundColor: "transparent"}, "slow");
                
            setTimeout(function() {
                $(".top_logo,.top_logo_folded").attr("src", "img/logo_light.png");
            }, 500);
        });

        $(window).scroll(function() {
            if (folded && window.scrollY == 0) {
                $("#header").removeClass("header_folded").addClass("header");
                $("#top_logo").removeClass("top_logo_folded").addClass("top_logo");
                folded = false;
            }
            if (!folded && window.scrollY > 0) {
                $("#header").removeClass("header").addClass("header_folded");
                $("#top_logo").removeClass("top_logo").addClass("top_logo_folded");
                folded = true;
            }
        });

        $("#about_btn").click(function() {
            scroll("#section2");
        });

        $("#products_btn").click(function() {
            scroll("#section3");
        });

        $("#demo_btn").click(function() {
            scroll("#section5");
        });

        $("#account_btn").click(function() {
            window.location = "login.php";
        });

        $("#top_logo").click(function() {
            scroll("#section1");
        })
    });
</script>
<div class="header" id="header">
    <img class="top_logo" id="top_logo" src="img/logo_light.png" />
    <table id="header_text" border="0">
        <tr>
            <td id="about_btn" class="menu_btn" oc="#2884b7" ec="#52a9d9">About</td>
            <td id="products_btn" class="menu_btn" oc="#5c28b7" ec="#8352d9">Products</td>
            <td id="demo_btn" class="menu_btn" oc="#2dcc8f" ec="#68dece">Demo</td>
            <td id="account_btn" class="menu_btn" oc="#f20729" ec="#fa647a">Login/Signup</td>
        </tr>
    </table>
</div>