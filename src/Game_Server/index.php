<?php
session_start();
function main()
{
    if($_SERVER["REQUEST_METHOD"]=="POST"){
        $_SESSION["username"] = $_POST["username"];
        return;
    }
    else if(isset($_SESSION["username"]))
        header("Location:logOut.php");
}
?>
<html>
    <head>
        <title>log in</title>
    </head>
    <body>
        <center><table><form action='' method='post' id='form1'>
            <tr><td>Username</td><td ><input type='text' name='username'></td></tr>
            <tr><td>Password</td><td ><input type='password' name='password'></td></tr>
            <tr><td><input type='button' onclick='send()' value='Send'></td><td>
            <input type='button' value='Register' onclick ='register()'></td></tr>

        </form></table></center>

        <script>
            function send()
            {
                var form = document.getElementById("form1");
                form.submit();
            }
        </script>

    </body>

</html>