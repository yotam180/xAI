<html>
<head>
    <title>xAI - register</title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />
    <link rel="StyleSheet" href="style/register.css" />

    <script>
        $(document).ready(function() {
            $.ajax({
                url: "/profile",
                success: function(e) {
                    var j = JSON.parse(e);
                    $("#name_span").text(j.first_name + " " + j.last_name);
                },
                error: function(a, b, c) {
                    if (a.status == 403) {
                        location.href = "/login.php";
                    }
                }
            });
        });
    </script>
</head>
<body>
    <a href="console.php"><img class="top_logo" id="top_logo" src="img/logo_light.png" /></a>
    <div id="title"><strong>Welcome to xAI, <span id="name_span">[...]</span>.</strong></div>
</body>
</html>