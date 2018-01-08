<script type="text/javascript">
    $(document).ready(function() {
        $(".menu_btn").mouseenter(function() {
            $(".menu_btn")
                .stop(true, true)
                .animate({backgroundColor: "transparent"}, "fast");

            $(this)
                .stop(true, true)
                .animate({backgroundColor: $(this).attr("oc")}, "fast");

            $("#header")
                .stop(true, true)
                .animate({backgroundColor: $(this).attr("ec")}, "slow");
            
            // $("#freezer")
            //     .stop(true, true)
            //     .fadeIn()
            //     .css({backgroundColor: $(this).attr("ec")});
        });
        $("#header").mouseleave(function() {
            $(".menu_btn")
                .stop(true, true)
                .animate({backgroundColor: "transparent"}, "fast");

            $("#header")
                .stop(true, true)
                .animate({backgroundColor: "transparent"}, "slow");

            // $("#freezer")
            //     .stop(true, true)
            //     .fadeOut();
        });
    });
</script>
<div id="header">
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