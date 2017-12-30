<html>
<head>
    <title>register</title>
</head>
<body>
    <?php
    $GLOBALS["path"]="";
    require_once($path."include.php");
    echo register($_GET["username"],$_GET["password"],$_GET["email"]);
    function register($username,$password,$email)
    {
        $file = fopen($GLOBALS["path"]."Users.txt","a+");
        $users = json_decode(fread($file,10000),true);
        if(userIndex($username,$users)!=-1)
        {
            fclose($file);
            return -1;
        }
        $index = sizeof($users);
        $users[$index]["Username"] = $username;
        $users[$index]["Password"] = $password;
        $users[$index]["Email"] = $email;
        $temp = fopen($GLOBALS["path"]."Users.txt","w+");
        fclose($temp);
        fwrite($file,json_encode($users));
        fclose($file);
        return 0;
    }
    ?>
</body>
</html>