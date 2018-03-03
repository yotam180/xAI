<html>
<head>
    <title>xAI | New Dataset</title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />
    <style>
        .chips ::placeholder {
            color: #9e9e9e;
        }
    </style>
    <script>
        $(document).ready(function() {
            $("#txt_subject").on("input", function() {
                $("#txt_identifier").val(PROFILE.username + "_" + ($(this).val().match(/\w+/g) || []).map(x => x.toLowerCase()).join("_"));
                Materialize.updateTextFields();
            });

            $.ajax({
                url: "/profile",
                success: function(e) {
                    window.PROFILE = JSON.parse(e);
                }
            })

            $("#txt_positives").material_chip();
            $("#txt_positives").find(".input").attr("placeholder", "Trigger Keywords");
            $("#txt_negatives").material_chip()
            $("#txt_negatives").find(".input").attr("placeholder", "Negative Keywords");
        
            $(".chips").find(".input").css({color: "#039be5"});

            $("#btn_create").click(function() {
                $.ajax({
                    url: "/create_dataset",
                    type: "POST",
                    data: JSON.stringify({
                        subject: $("#txt_subject").val(),
                        identifier: $("#txt_identifier").val(),
                        description: $("#txt_description").val(),
                        positive: $("#txt_positives").material_chip("data").map(x => x.tag),
                        negative: $("#txt_negatives").material_chip("data").map(x => x.tag)
                    }),
                    success: function(e) {
                        Materialize.toast("Creating Dataset...");
                    },
                    error: function(a, b, c) {
                        try {
                            j = JSON.parse(a.responseText);
                            Materialize.toast("Error " + a.status + ": " + j.message);
                        }
                        catch (e) {
                            Materialize.toast("Error " + a.status);
                        }
                    }
                });
            });
        });
    </script>
</head>
<body class="white-text">
    <a href="console.php"><i class="medium material-icons">arrow_back</i></a>
    <div id="title"><strong>New Dataset</strong></div>
    <div class="section"></div>
    <div class="container" style="color: #039be5;">
        <form id="dataset_details" class="col s12">
            <div class="row">
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <input id="txt_subject" type="text" />
                    <label for="txt_subject">Subject (What is your dataset about?) - Example: Dog, Cat, Airplane, Man</label>
                </div>
            </div>
            <div class="row">
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <input id="txt_identifier" type="text" />
                    <label for="txt_identifier">Dataset identifier</label>
                </div>
            </div>
            <div class="row">
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <input id="txt_description" type="text" />
                    <label for="txt_description">Description (What is your subject about?)</label>
                </div>
            </div>
            <div class="row">
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <div class="chips white-text" id="txt_positives"></div>
                </div>
            </div>
            <div class="row">
                <div class="col s3"></div>
                <div class="input-field col s6">
                    <div class="chips white-text" id="txt_negatives"></div>
                </div>
            </div>
            <div class="row">
                <div class="col s4"></div>
                <div class="col s6">
                    <a class="waves-effect waves-light btn" id="btn_create">
                        Create Dataset
                        <i class="material-icons right">add</i>
                    </a>
                </div>
            </div>
        </form>
    </div>
</body>
</html>