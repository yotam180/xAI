<html>
    <head><title>login</title></head>
    <body>
        <?php
        require_once("include.php");
        $boolean = logIn($_GET["username"],$_GET["password"]);
        echo $boolean?"yes":"no";
        function logIn($username,$password)
        {
            $file = fopen("Users.txt","r+");
            $users = json_decode(fread($file,10000),true);
            $index = userIndex($username,$users);
            return($users[$index]["Password"]==$password);
        }
        ?>
    </body>
</html>