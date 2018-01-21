<?php

require_once("config.php");

if ($_SERVER["REQUEST_METHOD"] != "POST") {
    die("{\"message\": \"post required\"}");
}

session_start();
$session = isset($_SESSION["api_session"]) ? $_SESSION["api_session"] : null;

$op = array(
    "http" => array(
        "method" => "POST",
        "header" => "Content-type: application/x-www-form-urlencoded\r\n" . ($session ? "Authentication: Session " + base64_encode($session) : "") . "\r\n",
        "content" => json_encode($_POST)
    )
);

$ctx = stream_context_create($op);
$res = file_get_contents($API . "register", false, $ctx);

echo $res;

?>