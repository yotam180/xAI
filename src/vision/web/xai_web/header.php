<script type="text/javascript">
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
            console.log(folded, window.scrollY);
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
    });
</script>
<div class="header" id="header">
    <img class="top_logo" id="top_logo" src="img/logo_light.png" />
    <table id="header_text" border="0">
        <tr>
            <td class="menu_btn" oc="#2884b7" ec="#52a9d9">About</td>
            <td class="menu_btn" oc="#5c28b7" ec="#8352d9">Products</td>
            <td class="menu_btn" oc="#2dcc8f" ec="#68dece">Demo</td>
            <td class="menu_btn" oc="#f20729" ec="#fa647a">Account</td>
        </tr>
    </table>
</div>

<div id="freezer">
&nbsp;
</div>