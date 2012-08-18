import sys
try:
    if sys.argv[1] == "" or sys.argv[2] == "":
	pass
    with open(sys.argv[2], 'w') as file:
	file.write("")
except:     
    sys.exit("Useage: python MMLC.py file.mm output.html")

if ".mm" not in sys.argv[1]:
    sys.exit("Not a valid MML file")

tags = {
":nl:":"\n",
":form:":"<form ",
":!form:":"</form>",
":post:":"method='POST'",
":get:":"method='GET'",
":mml:":"<html>\n",
":!mml:":"\n</html>",
":cq:":'"',
":ct:":">\n",
":link:":'\n<a href="',
":!link:":"</a>\n",
":div:":"\n<div ",
":!div:":"\n</div>",
":id:":'id="',
":class:": 'class="',
":span:":"\n<span ",
":!span:":"</span>\n",
":textbox:":"<input ",
":textarea:":"\n<textarea ",
":!textarea:":"\n</textarea>\n",
":type:":'type="',
":name:": 'name="',
":value:":'value="',
":style:":'style="',
":anchor:":'<a ',
":!anchor":"</a>\n",
":main:":"\n<body>\n",
":!main:":"\n</body>",
":br:":"<br/>\n",
":bold:":"\n<strong>\n",
":button":"\n<button ",
":!button":"\n</button>\n",
":center:":"\n<center>\n",
":!center:":"\n</center>\n",
":code:":"\n<code>\n",
":!code:":"\n</code>\n",
":h1:":"\n<h1>\n",
":!h1:":"\n</h1>\n",
":h2:":"\n<h2>\n",
":!h2:":"\n</h2>\n",
":h3:":"\n<h3>\n",
":!h3:":"\n</h3>\n",
":h4:":"\n<h4>\n",
":!h4:":"\n</h4>\n",
":h5:":"\n<h5>\n",
":!h5:":"\n</h5>\n",
":h6:":"\n<h6>\n",
":!h6:":"\n</h6>\n",
":top:":"<head>",
":!top":"\n</head>\n",
":title:":"\n<title>\n,",
":!title:":"\n</title>\n",
":hr:":"\n<hr/>\n",
":bullet:":"\n<li>\n",
":!bullet:":"\n</li>\n",
":italic:":"\n<i>\n",
"!italic:":"\b</i>\n",
":src:": 'src="',
":img:": '\n<img ',
":list:":"\n<li>\n",
":!list:":"\n</li>\n",
":href:":'href="',
":include:":"\n<link ",
":rel:":'rel="',
":content:":'content="',
":meta": "\n<meta ",
":paragraph:":"\n<p>\n",
":!paragraph:":"\n</p>\n",
":javascript":"\n<script type='text/javascript'>\n",
":!javascript:":"\n</script>\n",
":css:":"\n<script type='text/css'>\n",
":!css:":"\n</script>\n",
":script:": "\n<script ",
":!script:":"\n</script>\n",
":table:":"\n<table ",
"!table:":"\n</table>\n",
":tr:":"\n<tr ",
":!tr:":"\n</tr>\n",
":td:":"\n<td ",
":!td:":"\n</td>\n",
":!top:":"\n</head>\n",
}

with open(sys.argv[1], 'r') as input:
    with open(sys.argv[2], 'a') as output:
	for lines in input:
            lines = lines.rstrip("\n")
	    try:
                lines_ = lines.replace(" ", '')
	        output.write(tags[lines_])
	    except:
		if lines.startswith(":") and lines.endswith(":"):
		    sys.exit("SyntaxError: "+lines+" is not a valid tag")
		else:
		    output.write(lines)
