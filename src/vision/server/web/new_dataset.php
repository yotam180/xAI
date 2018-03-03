<html>
<head>
    <title>xAI | New Dataset</title>

    <?php require("include.php"); ?>

    <link rel="StyleSheet" href="style/master.css" />

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

            $(".chips").material_chip({
                placeholder: "Enter a keyword"
            });
            $(".chips").find(".input")
                       .css({color: "#039be5"});
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
        </form>
    </div>
</body>
</html>