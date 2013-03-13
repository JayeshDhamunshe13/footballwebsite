<!DOCTYPE html>

<html lang="en">

<head>
<title>Football ${self.title()}</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

## CSS links
<link href="../static/css/football.css" type="text/css" rel="stylesheet">
<link href="../static/css/bootstrap.css" type="text/css" rel="stylesheet">

    ${self.head_tags()}

    ${self.jquery_tags()}

</head>

<body style="padding:0;margin:0;">
    <div id="header_section_wrapper">

        <header id="header_container">
            <div id="header_content" class="container">
                <a href="/">
                    <img src="../static/image/headerLogo.png">
                </a>
            </div>
        </header>

        <div id="menuWrapper">

            <div id="menu">

                <ul>
                    <li><a title="Home Page" href="/">Home</a></li>
                    <li><a title="Register" href="Register">Register</a></li>
                </ul>

            </div>

        </div>




        <section id="section_container">
            <div class="container" id="section_content">
                ${self.section_content()}
            </div>
        </section>





##        <div class="navbar navbar-inverse navbar-fixed-top">
##            <div class="navbar-inner">
##
##                <div class="container">
##                    <button class="btn btn-navbar collapsed" data-target=".nav-collapse" data-toggle="collapse" type="button">
##                        <span class="icon-bar"></span>
##                        <span class="icon-bar"></span>
##                        <span class="icon-bar"></span>
##                    </button>
##
##
##                    <div class="nav-collapse collapse" style="height: 0px;">
##                        <ul class="nav">
##                            <li class="">
##                                <a href="#">Home</a>
##                            </li>
##                            <li class="">
##                                <a href="#">Register</a>
##                            </li>
##                        </ul>
##                    </div>
##                </div>
##            </div>
##        </div>

        </div>

    <div id="footer_wrapper">
        <footer id="footer_container">
            <div class="container" id="footer_content">
                <ul class="footer_links">
                    <li class="first">Copyright &copy; <a href="/">Alpha Football Academy, Mumbai</a></li>
                </ul>
            </div>
        </footer>
    </div>

</body>
</html>