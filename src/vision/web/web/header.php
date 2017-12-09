<?php
$menu = array("Sign In,login.php", "Sign Up,signup.php", "About,about.php");
$html = "";
foreach ($menu as $val) {
    $vals = explode(",", $val);
    $html .= "<li";
    if (strcmp("/" . $vals[1], $_SERVER["PHP_SELF"]) == 0) {
        $html .= " class=\"active\"";
    }
    $html .= "><a href=\"" . $vals[1] . "\">" . $vals[0] . "</a></li>";
}
?>

<nav>
    <div class="nav-wrapper">
        <a href="/" class="brand-logo">&nbsp;xAI</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
        <?php echo $html; ?>
        </ul>
    </div>
</nav>
