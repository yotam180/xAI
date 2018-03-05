<html>
<head>
    <title>xAI - register</title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />
    <link rel="StyleSheet" href="style/register.css" />

    <script src="https://rawgit.com/ruimarinho/google-libphonenumber/master/dist/libphonenumber.js"></script>

    <script>
        $(document).ready(function() {
            $('select').material_select();

            var phoneUtil = libphonenumber.PhoneNumberUtil.getInstance();
            var PNF = libphonenumber.PhoneNumberFormat;
            var EMAIL = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

            $("#txt_username").focusout(function() {
                if ($(this).val().length < 6) {
                    err(this, "Too short? Must be at least 6 chars long.");
                }
                else if ($(this).val().length > 30) {
                    err(this, "Too long? Must be at most 30 chars long.");
                }
                else if (!$(this).val().match(/^[A-Za-z0-9\_\.]+$/i)) {
                    err(this, "Just English letters, numbers, dots and underscores please :)");
                }
                else {
                    ok(this);
                }
            });

            $("#txt_password").focusout(function() {
                if ($(this).val().length < 6) {
                    err(this, "Too short? Must be at least 6 chars long.");
                }
                else if ($(this).val().length > 30) {
                    err(this, "Too long? Must be at most 30 chars long.");
                }
                else if ($(this).val().toUpperCase() == $(this).val()) {
                    err(this, "Must contain at least one lower-case character.");
                }
                else if ($(this).val().toLowerCase() == $(this).val()) {
                    err(this, "Must contain at least one upper-case character.");
                }
                else {
                    ok(this);
                }
            });

            $("#txt_firstname").focusout(function() {
                if ($(this).val().length < 2) {
                    err(this, "You must fill a valid name.");
                }
                else {
                    ok(this);
                }
            });
            $("#txt_lastname").focusout(function() {
                if ($(this).val().length < 2) {
                    err(this, "You must fill a valid name.");
                }
                else {
                    ok(this);
                }
            });

            $("#txt_phonenum").focusout(function() {
                var num = $(this).val();
                if (!num.startsWith("+"))
                    num = "+" + num;
                try {
                    var phoneNumber = phoneUtil.parseAndKeepRawInput(num);
                    //$(this).val(phoneUtil.format(num, PNF.INTERNTIONAL));
                    ok(this, phoneUtil.format(phoneNumber, PNF.INTERNATIONAL));
                }
                catch (er) {
                    err(this, "Have you forgotten the country code?");
                }
            });

            $("#txt_confirmpassword").focusout(function() {
                if ($(this).val() != $("#txt_password").val()) {
                    err(this, "Hmm... The confirmation and the password don't match");
                }
                else {
                    ok(this);
                }
            });

            $("#txt_email").focusout(function() {
                if ($(this).val().match(EMAIL)) {
                    ok(this);
                }
                else {
                    err(this, "The email you provided is in an incorrect format!");
                }
            });

            $("#txt_confirmemail").focusout(function() {
                if ($(this).val() != $("#txt_email").val()) {
                    err(this, "Hmm... The confirmation and the email don't match");
                }
                else {
                    ok(this);
                }
            });

            $("#select_country").change(function() {
                if ($(this).val().length == 2) {
                    ok($(".select-wrapper"));
                }
                else {
                    err($(".select-wrapper"), "You must select a country");
                }
            })

            $("#btn_signup").click(function() {

                if (!$("#check_terms").is(":checked")) {
                    Materialize.toast("You must agree to the terms of service", 5000);
                    return;
                }

                let $me = $(this);
                $me.attr("disabled", true);
                $.ajax({
                    url: "/register",
                    type: "POST",
                    data: JSON.stringify({
                        "username": $("#txt_username").val(),
                        "password": $("#txt_password").val(),
                        "confirmation": $("#txt_confirmpassword").val(),
                        "first_name": $("#txt_firstname").val(),
                        "last_name": $("#txt_lastname").val(),
                        "email": $("#txt_email").val(),
                        "country": $("#select_country").val(),
                        "phone": $("#txt_phonenum").val()
                    }),
                    success: function(e) {
                        var j = JSON.parse(e);
                        if (j.error) {
                            Materialize.toast(j.error, 5000);
                        }
                        else if (j.message) {
                            Materialize.toast(j.message, 2000);
                            setTimeout(function() {
                                window.location = "/";
                            }, 2000);
                        }
                        else {
                            Materialize.toast(e, 5000);
                        }
                        $me.attr("disabled", false);
                    },
                    error: function(a, b, c) {
                        Materialize.toast("An error occured while trying to register you.", 5000);
                        $me.attr("disabled", false);
                    }
                });
            });


        });

        function err(el, text) {
            $("label[for=" + $(el).attr("id") + "]").attr("data-error", text);
            $(el).removeClass("valid");
            $(el).addClass("invalid");
        }

        function ok(el, text) {
            $("label[for=" + $(el).attr("id") + "]").attr("data-success", text);
            $(el).removeClass("invalid");
            $(el).addClass("valid");
        }

    </script>
</head>
<body>
    <a href="index.php"><img class="top_logo" id="top_logo" src="img/logo_light.png" /></a>
    <div id="title"><strong>Sign Up</strong></div>

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
                <div class="input-field col s3">
                    <input id="txt_firstname" type="text" />
                    <label for="txt_firstname">First Name</label>
                </div>
                <div class="input-field col s3">
                    <input id="txt_lastname" type="text" />
                    <label for="txt_lastname">Last Name</label>
                </div>
            </div>

            <div class="row">
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <input id="txt_phonenum" type="text" />
                    <label for="txt_phonenum">Phone Number</label>
                </div>
            </div>

            <div class="row">
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <select id="select_country">
                        <option value="" selected>Select your country</option>
                        <?php
                            $json = json_decode(file_get_contents("static/country_codes.json"));
                            foreach ($json as $c) {
                                $code = $c->code;
                                $name = $c->name;
                                echo("<option value='$code'>$name</option>\n");
                            }
                        ?>
                    </select>
                    <label>Country</label>
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
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <input id="txt_confirmpassword" type="password" />
                    <label for="txt_confirmpassword">Retype password</label>
                </div>
            </div>

            <div class="row">
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <input id="txt_email" type="email" />
                    <label for="txt_email">Email</label>
                </div>
            </div>

            <div class="row">
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <input id="txt_confirmemail" type="email" />
                    <label for="txt_confirmemail">Retype email</label>
                </div>
            </div>

            <div class="row">
                <div class="col s3"></div>
                <div class="switch col s6">
                    <label>
                    I do not agree
                    <input id="check_terms" type="checkbox" />
                    <span class="lever"></span>
                    I agree to the
                    </label>  <a href="terms.php" target="_blank">terms of service</a>
                </div>
            </div>

            <div class="row">
                <div class="col s4"></div>
                <div class="col s6">
                    <a class="waves-effect waves-light btn" id="btn_signup">
                        Sign up!
                        <i class="material-icons right">send</i>
                    </a>
                </div>
            </div>
        </form>
    </div>
</body>
</html>