<html>
<head>
    <title>xAI - register</title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />
    <link rel="StyleSheet" href="style/register.css" />

    <script>
        $(document).ready(function() {
            $('select').material_select();
        });
    </script>
</head>
<body>
    <a href="index.php"><img class="top_logo" id="top_logo" src="img/logo_light.png" /><a>
    <div id="title"><strong>Sign Up</strong></div>

    <div class="section"></div>

    <div class="container">
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
                    <select>
                        <option value="" disabled selected>Select your country</option>
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
                    <a class="waves-effect waves-light btn">
                        Sign up!
                        <i class="material-icons right">send</i>
                    </a>
                </div>
            </div>
        </form>
    </div>
</body>
</html>