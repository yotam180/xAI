<html>
<head>
    <title>xAI - register</title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />
    <link rel="StyleSheet" href="style/register.css" />

    <script src="https://rawgit.com/ruimarinho/google-libphonenumber/master/dist/libphonenumber.js"></script>

    <script>window.SERV = "http://localhost:9090";</script>

    <script>
        $(document).ready(function() {
            $("#btn_login").click(function() {
                $.ajax({
                    url: window.SERV + "/login",
                    type: "POST",
                    data: JSON.stringify({
                        username: $("#txt_username").val(),
                        password: $("#txt_password").val()
                    }),
                    success: function(a) {
                        var j = JSON.parse(a);
                        if (j.login) {
                            Materialize.toast("Successful. Redirecting...");
                        }
                        else {
                            Materialize.toast(j.message);
                        }
                    },
                    error: function() {
                        Materialize.toast("Error while logging in to xAI servers.");
                    }
                });
            });
        });
    </script>

</head>
<body>
<a href="index.php"><img class="top_logo" id="top_logo" src="img/logo_light.png" /></a>
<div id="title"><strong>Login</strong></div>

<div class="section"></div>
<div class="container" style="color: #039be5;">
    <form id="register_details" class="col s12">
        <div class="row">
            <div class="col s3"></div>
            <div class="input-field col s6">
                <input id="txt_username" type="text" />
                <label for="txt_username">Username</label>
            </div>
        </div>
        <div class="row">
            <div class="col s3"></div>
            <div class="input-field col s6">
                <input id="txt_password" type="password" />
                <label for="txt_password">Password</label>
            </div>
        </div>
        <div class="row">
            <div class="col s4"></div>
            <div class="col s6">
                <a class="waves-effect waves-light btn" id="btn_login">
                    Login
                    <i class="material-icons right">send</i>
                </a>
            </div>
        </div>
    </form>
</div>

</body>
</html>