# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1375812004.661174
_template_filename='/home/trupti/commit/webapp/gnukhata/templates/start_up.mako'
_template_uri='/start_up.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<?xml version="1.0" encoding="UTF-8"?> \n\n<!DOCTYPE HTML>\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">\n<head>\n\t<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n\t<title>Welcome to GNUKhata</title>\n\t<script type="text/javascript" src="/jquery/jquery-1.5.min.js"> </script>\n\t<script type="text/javascript" src="/jquery/jquery.form.min.js"> </script>\n\t<script type="text/javascript" src="/jquery/jquery.autocomplete-min.js"> </script>\n\t<script type="text/javascript" src="/jquery/validation.js"> </script>\n\t <script src="/jquery/jquery-latest.js"></script>\n\t<link rel="stylesheet" type="text/css" href="/jquery/tab.css">\n\t<script type="text/javascript" src="/jquery/jquery-ui.min.js"> </script>\n\t<script type="text/javascript" src="/jquery/jquery-latest.js"> </script>\n\t<script type="text/javascript" src="/jquery/jquery.titlecase2.js"> </script>\n<style>\n.button{\nwidth: 1000px;\n}\n</style>\n<script type="text/javascript">\n//<![CDATA[\nvar from_date = [];\nvar to_date = [];\n$(document).ready(function() \n{\t\n\t\n\tdocument.getElementById("NextLogin").disabled = true;\n\t$(\'#todatey\').keyup(function(){\n\t\tif(this.value.length>=4)\n\t\t{\n\t\t\t$("#newsubmitbutton").focus();\n\t\t\tvar fromdate = document.getElementById(\'fromdate\');\n\t\t\tvar fromdated = document.getElementById(\'fromdated\');\n\t\t\tvar fromdatem = document.getElementById(\'fromdatem\');\n\t\t\tvar fromdatey = document.getElementById(\'fromdatey\');\n\t\t\tvar todated = document.getElementById(\'todated\');\n\t\t\tvar todatem = document.getElementById(\'todatem\');\n\t\t        var todatey = document.getElementById(\'todatey\');\n\t\t//to check if the financial year already exists for the given organisation\n\t\t\t\tvar orgname = $(\'input#orgname\').val();\n\t\t\t\t\n\t\t\t\t$.ajax({\n           \t\t\t\ttype: "POST",\n            \t\t\t\turl: location.protocol+"//"+location.host+"/startup/getFinancialYear",\n            \t\t\t\tdata: {"organisation":orgname},\n           \t\t\t\tdataType: "json",\n\t\t\t\t\tsuccess: function(result) {\n\t\t\t\t\t\tvar res = result["financialyear"];\n\t\t\t\t\t\tvar start_date = fromdated.value + "-" + fromdatem.value + "-" + fromdatey.value;\n\t\t\t\t\t\tvar end_date = todated.value + "-" + todatem.value + "-" + todatey.value;\n\t\t\t\t\t\tvar check_date = start_date + "," + end_date;\n\t\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\tfor(var i=0;i<res.length;i++)\n\t\t\t\t   \t\t{\n\t\t\t\t\t\t\tif(res[i] == check_date)\n\t\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\talert("Organisation with Financial Year already exists");\n\t\t\t\t\t\t\t\t$(\'#orgname\').focus();\n\t\t\t\t\t\t\t\tdocument.getElementById(\'orgname\').value = "";\n\t\t\t\t\t\t\t\tfromdated.value="";fromdatem.value = ""; fromdatey.value="";\n\t\t\t\t\t\t\t\ttodated.value= "";todatem.value =""; todatey.value ="";\n\t\t\t\t\t\t\t\treturn false;\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\telse \n\t\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\t$("#newsubmitbutton").focus();\t\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t});\n\t\t\t}\n\t\t\t\n\t\t});\n\t\n\t\t$("#newsubmitbutton").click(function()\n\t\t{\n\t\t\tvar orgname = document.getElementById(\'orgname\');\n\t\t        var fromdate = document.getElementById(\'fromdate\');\n\t\t\tvar fromdated = document.getElementById(\'fromdated\');\n\t\t\tvar fromdatem = document.getElementById(\'fromdatem\');\n\t\t\tvar fromdatey = document.getElementById(\'fromdatey\');\n\t\t\tvar todated = document.getElementById(\'todated\');\n\t\t\tvar todatem = document.getElementById(\'todatem\');\n\t\t        var todatey = document.getElementById(\'todatey\');\n\t\t\t\n\t\t\tif (notEmpty(orgname,"Please Enter Organization Name") || notEmpty(fromdated,"Please Enter From Day") || notEmpty(fromdatem,"Please Enter From Month") || notEmpty(fromdatey,"Please Enter From Year") || notEmpty(todated,"Please Enter To Day") || notEmpty(todatem,"Please Enter To Month") || notEmpty(todatey,"Please Enter To Year") || !isNumeric(fromdated,"Please Enter Valid From Day") || !isNumeric(fromdatem,"Please Enter Valid From Month") || !isNumeric(fromdatey,"Please Enter Valid From Year") || !isNumeric(todated,"Please Enter Valid To Day") || !isNumeric(todatem,"Please Enter Valid To Month") || !isNumeric(todatey,"Please Enter Valid To Year"))\n\t\t\t{\n\t\t\t\treturn false;\n\t\t\t}\n\t\t\telse\n\t\t\t{\n\t\t\t\tif(fromdated.value == 0 || fromdatem.value == 0 || fromdatey.value == 0 || todated.value == 0 || todatem.value == 0 || todatey.value == 0)\n\t\t\t\t{\n\t\t\t\t\talert("Date Cant Have Zero");\n\t\t\t\t\tfromdated.value=\'\';\n\t\t\t\t\tfromdated.focus();\n\t\t\t\t\treturn false;  \n\t\t\t\t}\n\n\t\t\t\tif (fromdated.value >= 32 )\n\t\t\t\t{\t\n\t\t\t\t\talert("The From Day Cannot Be Greater Than 31");\n                                        fromdated.value=\'\';\n\t\t\t\t\tfromdated.focus();\n\t\t\t\t\treturn false;  \n                                \t\t\t\n\t\t\t\t}\n\n\t\t\t\tif (todated.value >= 32)\n\t\t\t\t{\t\n\t\t\t\t\talert("The To Day Cannot Be Greater Than 31");\n                                        todated.value=\'\';\n\t\t\t\t\ttodated.focus();\n\t\t\t\t\treturn false;  \n                                \t\t\t\n\t\t\t\t}\n\t\t\t\t\t \n\t\t\t\tif(fromdatem.value >=13)\n\t\t\t\t{\n\t\t\t\t\talert("From Month should not be greater than 12");\n\t\t\t\t\tfromdatem.value=\'\';\n\t\t\t\t\tfromdatem.focus();\n\t\t\t\t\treturn false; \n\t\t\t\t}\n\n\t\t\t\tif(todatem.value >=13)\n\t\t\t\t{\n\t\t\t\t\talert("Month should not be greater than 12");\n\t\t\t\t\ttodatem.value=\'\';\n\t\t\t\t\ttodatem.focus();\n\t\t\t\t\treturn false; \n\t\t\t\t}\n\n\t\t\t\tif(fromdatem.value == "02" || fromdatem.value == "04" || fromdatem.value == "06" || fromdatem.value == "09" || fromdatem.value == "11")\n\t\t\t\t{\n\t\t\t\t\tif (fromdated.value >= 31 || fromdated.value >= 31)\n\t\t\t\t\t{\n\t\t\t\t\t\talert("Day for the corressponding from date month does not exist");\n\t\t\t\t\t\tfromdated.value=\'\';\n\t\t\t\t\t\tfromdated.focus();\n\t\t\t\t\t\treturn false;\n\t\t\t\t\t}\n\t\t\t\t}\n\n\t\t\t\tif (todatem.value == "02" || todatem.value == "04" || todatem.value == "06" || todatem.value == "09" || todatem.value == "11")\n\t\t\t\t{\n\t\t\t\t\tif (todated.value >= 31 || todated.value >= 31)\n\t\t\t\t\t{\n\t\t\t\t\t\talert("Day for the corressponding from date month does not exist");\n\t\t\t\t\t\ttodated.value=\'\';\n\t\t\t\t\t\ttodated.focus();\n\t\t\t\t\t\treturn false;\n\t\t\t\t\t}\n\t\t\t\t}\n\n\t\t\t\tif (fromdatem.value == "01" || fromdatem.value == "03" || fromdatem.value == "05" || fromdatem.value == "07" || fromdatem.value == "08" || fromdatem.value == "10" || fromdatem.value == "12")\n\t\t\t\t{\n\t\t\t\t\tif (fromdated.value > 31 || fromdated.value > 31)\n\t\t\t\t\t{\n\t\t\t\t\t\talert("Day for the corressponding from date month does not exist");\n\t\t\t\t\t\tfromdated.value=\'\';\n\t\t\t\t\t\tfromdated.focus();\n\t\t\t\t\t\treturn false;\n\t\t\t\t\t}\n\t\t\t\t}\n\n\t\t\t\tif(todatem.value == "01" || todatem.value == "03" || todatem.value == "05" || todatem.value == "07" || todatem.value == "08" || todatem.value == "10" || todatem.value == "12")\n\t\t\t\t{\n\t\t\t\t\tif (todated.value > 31 || todated.value > 31)\n\t\t\t\t\t{\n\t\t\t\t\t\talert("Day for the corressponding from d-`ate month does not exist");\n\t\t\t\t\t\ttodated.value=\'\';\n\t\t\t\t\t\ttodated.focus();\n\t\t\t\t\t\treturn false;\n\t\t\t\t\t}\t\n\t\t\t\t}\n\n\t\t\t\tif (fromdatem.value == "02")\n\t\t\t\t{\n\t\t\t\t\tif (fromdated.value > 29)\n\t\t\t\t\t{\n\t\t\t\t\t\talert("Day for the corressponding from date month does not exist");\n\t\t\t\t\t\tfromdated.value=\'\';\n\t\t\t\t\t\tfromdated.focus();\n\t\t\t\t\t\treturn false;\n\t\t\t\t\t}\n\t\t\t\t}\n\t\n\t\t\t\tif (todatem.value == "02")\n\t\t\t\t{\n\t\t\t\t\tif (todated.value > 29)\n\t\t\t\t\t{\n\t\t\t\t\t\talert("Day for the corressponding from date month does not exist");\n\t\t\t\t\t\ttodated.value=\'\';\n\t\t\t\t\t\ttodated.focus();\n\t\t\t\t\t\treturn false;\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\t\n\t\t\t\tvar start = new Date(fromdatey.value,fromdatem.value - parseInt(1),fromdated.value);\n\t\t\t\tvar end = new Date(todatey.value,todatem.value  - parseInt(1),todated.value);\n\t\t\n\t\t\t\t//alert(start);\n\t\t\t\t//alert(end);\n\n\t\t\t\tif (start.getTime() > end.getTime())\n\t\t\t\t{\n\t\t\t\t\talert("From date should be less than to date");\n\t\t\t\t\tfromdated.focus();\n\t\t\t\t\treturn false;\t\t\t\n\t\t\t\t}\n\t\t\t\n\t\t\t\tif (!checkleapyear(fromdatey.value))\n\t\t\t\t{\n\t\t\t\t\tif (fromdatem.value == "02")\n\t\t\t\t\t{\n\t\t\t\t\t\tif (fromdated.value == "29")\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\talert("Enter valid from day for leap year");\n\t\t\t\t\t\t\tfromdated.value=\'\';\n\t\t\t\t\t\t\tfromdated.focus();\n\t\t\t\t\t\t\treturn false;\n\t\t\t\t\t\t}\n\t\t\t\t\t\t\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tif (!checkleapyear(todatey.value))\n\t\t\t\t{\n\t\t\t\t\tif (todatem.value == "02")\n\t\t\t\t\t{\n\t\t\t\t\t\tif (todated.value == "29")\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\talert("Enter valid to day for leap year");\n\t\t\t\t\t\t\ttodated.value=\'\';\n\t\t\t\t\t\t\ttodated.focus();\n\t\t\t\t\t\t\treturn false;\n\t\t\t\t\t\t}\n\t\t\t\t\t\t\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\t\n\t\t\t\treturn true;\t\n\t\t\t}\n\t\t\t\t\n\t\t\treturn false;\n\t\t});\n\n\t\t$(\'select#organisation\').change(function() {\t\n\n\t\tvar orgname = $(\'select#organisation\').val();\n\t\tdocument.getElementById("NextLogin").disabled = false;\n\t\t$.ajax({\n           \t\t\ttype: "POST",\n            \t\t\turl: location.protocol+"//"+location.host+"/startup/getFinancialYear",\n            \t\t\tdata: {"organisation":orgname},\n           \t\t\tdataType: "json",\n\t\t\t\t\n            \t\t\tsuccess: function(result) {\n\t\t\t\tlist_of_years = result["financialyear"];\n\t\t\t\tvar financial_year = document.getElementById("financial year");\n\t\t\t\tfinancial_year.options.length = 0\n\t\t\t\tif (list_of_years.length == 1)\n\t\t\t\t{\n\t\t\t\t\tvar option = document.createElement("option");\n\t\t\t\t\t//financial_year.options.add(option);\n\t\t\t\t\t\tfor(var i=0;i<list_of_years.length;i++)\n\t\t\t\t   \t\t{\n\t\t\t\t\t\t\tvar option = document.createElement("option");\n\t\t\t\t\t\t\toption.text = list_of_years[i][0] + " to " + list_of_years[i][1]; \n\t\t\t\t\t\t\toption.value = list_of_years[i][0] + " to " + list_of_years[i][1]; \n\t\t\t\t\t\t\tfinancial_year.options.add(option);\n\t\t\t\t\t\t\t//alert(list_of_years[i][0]);\n\t\t\t\t\t\t\tfrom_date[i] = list_of_years[i][0];\n\t\t\t\t\t\t\tto_date[i] = list_of_years[i][1];\n\t\t\t\t    \t\t}\n\t\t\t\t\t$("#NextLogin").focus();\n\t\t\t\t}\n\t\t\t\telse\n\t\t\t\t{\n\t\t\t\t\tvar option = document.createElement("option");\n\t\t\t\t\toption.text = "--Select--"; \n\t\t\t\t\toption.value = "--Select--";\n\t\t\t\t\tfinancial_year.options.add(option);\n\t\t\t\t\t\tfor(var i=0;i<list_of_years.length;i++)\n\t\t\t\t   \t\t{\n\t\t\t\t\t\t\tvar option = document.createElement("option");\n\t\t\t\t\t\t\toption.text = list_of_years[i][0] + " to " + list_of_years[i][1]; \n\t\t\t\t\t\t\toption.value = list_of_years[i][0] + " to " + list_of_years[i][1]; \n\t\t\t\t\t\t\tfinancial_year.options.add(option);\n\t\t\t\t\t\t\t//alert(list_of_years[i][0]);\n\t\t\t\t\t\t\tfrom_date[i] = list_of_years[i][0];\n\t\t\t\t\t\t\tto_date[i] = list_of_years[i][1];\n\t\t\t\t    \t\t}\n\t\t\t\t\toption.focus();\n\t\t\t\t}\t\n\t\t\t\t}\n\t\t\t});\n\t\t\treturn false;\n\t\t});\n\n\t\t$("#selectorg").click(function(){\n\t\t\t$(\'#logout\').empty();\n\t\t\tvar div1 = document.getElementById("toggle2");\n\t\t\tif (div1.style.display != "none")\n\t\t\t{\n\t\t\t\t$("#toggle2").toggle("slow");\n\t\t\t}\n\t\t\t$("#toggle1").toggle("slow");\n\t\t\t$("#organisation").focus();\n\t\t});\n\t\n\tfunction checkleapyear(datea)\n\t{\n       \t\tdatea = parseInt(datea);\n        \tif(datea%4 == 0)\n        \t{\n                \tif(datea%100 != 0)\n                \t{\n                \t        return true;\n                \t}\n                \telse\n                \t{\n                \t        if(datea%400 == 0)\n                \t                return true;\n                \t        else\n                \t                return false;\n                \t}\n        \t}\t\n\t\treturn false;\n\t}\n\n\tfunction notEmpty(elem, helperMsg)\n\t{\n\t\tif(elem.value.length == 0)\n\t\t{\n\t\t\talert(helperMsg);\n\t\t\telem.focus(); // set the focus to this input\n\t\t\treturn true;\n\t\t}\n\t\telse\n\t\t\treturn false;\n\t\t\t\n\t}\n\n\tfunction isNumeric(elem, helperMsg)\n\t{\n\t\tvar numericExpression = /^[0-9]+$/;\n\t\tif(elem.value.match(numericExpression)){\n\t\t\treturn true;\n\t\t}\n\t\telse\n\t\t{\n\t\t\talert(helperMsg);\n\t\t\telem.focus();\n\t\t\treturn false;\n\t\t}\n\t}\n\n\n\t\n\t\t$("#neworg").click(function(){\n\t\t\t$(\'#logout\').empty();\n\t\t\tvar div2 = document.getElementById("toggle1");\n\t\t\tif (div2.style.display != "none")\n\t\t\t{\n\t\t\t\t$("#toggle1").toggle("slow");\n\t\t\t}\n\t\t\t$("#toggle2").toggle("slow");\t\n\t\t\t$("#orgname").focus();\t\n\t\t});\n\t\t\n\t\n\n\t\t$("#NextLogin").click(function()\n\t\t{\n\t\t\tvar drop_financialYear = document.getElementById("financial year");\n\t\t\t\n\t\t\t\n\t\t\tvar index = drop_financialYear.selectedIndex;\n\t\t\tvar text = drop_financialYear.value;\n\t\t\tvar orgnamevalue = document.getElementById("organisation").value;\n\t\t\tif(orgnamevalue == "--Select--")\n\t\t\t{\n\t\t\t\talert("Please select organisation name ");\n\t\t\t\t$("select#organisation").focus();\n\t\t\t\treturn false;\n\t\t\t\t\n\t\t\t}else if(text == "--Select--")\n\t\t\t\t{\n\t\t\t\t\talert("Please select Financial Year");\n\t\t\t\t\t$("select#financial year").focus();\n\t\t\t\t\treturn false;\n\t\t\t\t}\n\t\t\telse\n\t\t\t{\n\t\t\t\tindex = 1;\n\t\t\t\tvar list_index = parseInt(index) - parseInt(1);\n\t\t\t\tdocument.forms[0].elements["yeartodate"].value = to_date[list_index];\n\t\t\t\tdocument.forms[0].elements["yearfromdate"].value = from_date[list_index];\n\t\t\t}\n\t\t\tvar datesplit = text.split(" to ");\n\t\t\tdocument.forms[0].elements["yearfrom"].value = datesplit[0];\n\t\t\tdocument.forms[0].elements["yearto"].value = datesplit[1];\n\t\n\t\t});\n\n\t\t\n\n\t\t/*\t*/\n\t\t\n\t\treturn false;\n});\n//]]>\n</script>\n<script type="text/javascript">\n//Validating date as DD\nfunction validate(obj) {\n       if (obj.value < 10 && obj.value.length != 2) {\n              alert(\'Date must be in DD\');\n              obj.value = "0" + obj.value;\n       }\n}\n</script>\n<script type="text/javascript">\n//Validating month as MM\nfunction validmonth(obj) {\n       if (obj.value < 10 && obj.value.length != 2) {\n              alert(\'Month must be in MM\');\n              obj.value = "0" + obj.value;\n       }\n}\n</script>\n<script type="text/javascript">\n//Validating year as YYYY\nfunction validyear(obj) {\n       var _thisYear = new Date().getFullYear();\n       if (obj.value.length < 4 ) {\n              alert(\'Year must be in YYYY\');\n              obj.focus();\n\t      obj.value = _thisYear;\n       }\n              \n}\n</script>\n\n<script>\n//<!CDATA[\nfunction fn(txt) {\n\tif (txt.value.length > 0)\n\t{\n\t\t$("#orgname").blur(function()\n\t\t{\n\t\t\t $("#orgname_warning").empty(); \n\t\t});\n\t\tdocument.getElementById(\'newsubmitbutton\').disabled = false;\n\t}\n\telse\n\t{\n\t\t$("#orgname").blur(function()\n\t\t{\n\t\t\t$("#orgname_warning").empty(); \n\t\t\t$("#orgname_warning").append("This field is required"); \n\t\t});\t\n\t\tdocument.getElementById(\'newsubmitbutton\').disabled = true;\t\n\t}\n}\n//]]>\n</script>\n\n<script>\nString.prototype.trim = function() {  return this.replace(/^[\\s]+/,\'\').replace(/[\\s]+$/,\'\').replace(/[\\s]{2,}/,\' \');  }\nfunction useTrim()\n{\n\tvar orgnam = document.getElementById(\'orgname\').value\n\tdocument.getElementById(\'orgname\').value = orgnam.trim();\n}\n</script>\n<script language="javascript" type="text/javascript">\n\nfunction limitText(limitField, limitCount, limitNum) {\n\tif (limitField.value.length > limitNum) {\n\t\tlimitField.value = limitField.value.substring(0, limitNum);\n\t} else {\n\t\tlimitCount.value = limitNum - limitField.value.length;\n\t}\n}\n</script>\n<script>\n//<!CDATA[\n//this is for titlecase\nString.prototype.capitalize = function(){\n   return this.replace( /(^|\\s)([a-z])/g , function(m,p1,p2){ return p1+p2.toUpperCase(); } );\n  };\nfunction change_case()\n{\n\tvar orgnam = document.getElementById(\'orgname\').value\n\tdocument.getElementById(\'orgname\').value = orgnam.capitalize();\n}\n//]]>\n</script>\n\n<script>\n/* Function to go to next field when we press Enter Key*/\nfunction keydown(e,s)\n{\n\tif (!e) var e = window.event;\n\tif (e.keyCode) code = e.keyCode;\n\telse if (e.which) code = e.which;\n\tif (code==13)\n\t{\n\t\tdocument.getElementById(s).focus();\n\t}\n}\n</script>\n\n<script>\n/* Function to go previous field when we press Up Arrow*/\nfunction keyup(e,s)\n{\n\tif (!e) var e = window.event;\n\tif (e.keyCode) code = e.keyCode;\n\telse if (e.which) code = e.which;\n\tif (code==38)\n\t{\n\t\tdocument.getElementById(s).focus();\n\t}\n}\n</script>\n<script>\n/*Function to move from organisation type to organisation name by Up arrow*/\nfunction typetoname()\n{\n\n\tvar x=document.getElementById("organisationType").selectedIndex;\n\tvar y=document.getElementById("organisationType").options;\n\tif(y[x].index==0){\n\t\tif (code==38){\n\t\t\tdocument.getElementById(\'orgname\').focus();\n\n\t         }\n        }\n\n}\n</script>\n<script>\n/*Function for Right arrow to have focus on selectorg when page is loaded*/\nfunction keyright(e,s){\n\tif (!e) var e = window.event;\n\tif (e.keyCode) code = e.keyCode;\n\telse if (e.which) code = e.which;\n\tif (code==39){\n\t\tdocument.getElementById(s).focus();\n\t}\n}\n</script>\n<script>\n/*Function to go from organisation to selectorg by Up arrow*/\nfunction orgtoselect()\n{\n\tvar x=document.getElementById("organisation").selectedIndex;\n\tvar y=document.getElementById("organisation").options;\n\tif(y[x].index==0){\n\t\tif (code==38){\n\t\t\tdocument.getElementById(\'selectorg\').focus();\n\n\t\t}\n        }\n\n}\n</script>\n<script>\n/* Function for down arrow to move to next field*/\nfunction keydowns(e,s)\n{\n\tif (!e) var e = window.event;\n\tif (e.keyCode) code = e.keyCode;\n\telse if (e.which) code = e.which;\n\tif (code==40)\n\t{\n\t\tdocument.getElementById(s).focus();\n\t}\n}\n</script>\n<script>\n//create a function that accepts an input variable (which key was key pressed)\nfunction disableEnterKey(e)\n{\n \n//create a variable to hold the number of the key that was pressed     \n\tvar key;\n\n\t//if the users browser is internet explorer\n\tif(window.event)\n\t{\n\t\t//store the key code (Key number) of the pressed key\n\t\tkey = window.event.keyCode;\n\n\t//otherwise, it is firefox\n\t} \n\telse \n\t{\n\t\t//store the key code (Key number) of the pressed key\n\t\tkey = e.which;     \n\t}\n\n\t//if key 13 is pressed (the enter key)\n\tif(key == 13)\n\t{\n\t\t//do nothing\n\t\treturn false;\n\t      \n    //otherwise\n    \t} \n\telse \n\t{\n      \n\t    //continue as normal (allow the key press for keys other than "enter")\n\t    return true;\n    \t}\n      \n\t//and don\'t forget to close the function    \n\t\n\tkeydown(e,s);\n}\n</script>\n\n\n<script>\n//function to calculate month of \'To Date\' \nfunction toMonth(e,s)\n{\n\tif (!e) var e = window.event;\n\tif (e.keyCode) code = e.keyCode;\n\telse if (e.which) code = e.which;\n\tif (code==13)\n\t{\n\t\tvar fromdated = Number(document.getElementById("fromdated").value);\n\t\tvar fromdatem = Number(document.getElementById("fromdatem").value);\n\t\tvar todatem = document.getElementById("todatem");\n\t\ttodatem.value =  fromdatem;\n\t\tvar todated = document.getElementById("todated");\n\t\tdocument.getElementById(\'fromdatey\').focus(); \n\t\tvar _thisMonth = new Date().getMonth();\n\t\t\t\t\n                if (fromdatem!=""&&!isNaN(fromdatem)){\n\n                }\n                else{\n                \n                        todatem.value=_thisMonth;\n                        alert(\'Month Cannot be Null\');\n                        document.getElementById(\'fromdatem\').focus();                             \n                }\n                   \n     \n\t\t\n\t\t \n\t\tif (fromdated == "01")\n\t\t{         \n                        todatem.value =  fromdatem - 01;\n                        todated.value=new Date().getDate();\n                        \n                        if(fromdated=="01" && fromdatem==""){\n                                  todatem.value = new Date().getMonth();\n                        }\n                      \n                        \n\t\t\tif (fromdatem == "01")\n\t\t\t{\n\t\t\t\ttodatem.value = 12;\n\t\t\t}\n\t\t          \n\n\t\t\tif (fromdatem  == "05" || fromdatem  == "07"  || fromdatem  == "10" || fromdatem  == "12")\n\t\t\t{\n\t\t\t\ttodated.value=30;\n\t\t\t}\n\t\n\t\t\t\t\n\t\t\tif (fromdatem  == "04" || fromdatem  == "06" || fromdatem  == "02"|| fromdatem == "09" || fromdatem  == "11" || fromdatem == "01" || fromdatem  == "08")\n\t\t\t{\n\t\t\t\ttodated.value=31;\n\t\t\t}\n\t\n\t\t\n\t\t\tif (fromdatem  == "03")\n\t\t\t{\n\t\t\t\ttodated.value=28;\n\t\t\t}\n\t\t\t\n\t\t}\n\t\t\t\n\t\t\telse\n\t\t\ttodated.value=fromdated-01;\n                        var _thisDate = new Date().getDate();\n\t\t\n                        if (fromdated!=""&&!isNaN(fromdated)){\n\n                         }\n                        else{\n                \n                                todated.value=_thisDate;\n                                alert(\'Date Cannot be Null\');\n                                document.getElementById(\'fromdated\').focus();      \n                        }\n                   \n     \n\t\t\tif (todatem.value < 10)\n\t\t\t{\n\t\t\t\ttodatem.value = "0" + todatem.value\n\t\t\t}\n\t\t\tif (todated.value < 10)\n\t\t\t{\n\t\t\t\ttodated.value = "0" + todated.value\n\t\t\t}\n\t\t\n\t\t\t\n\t\t          \n\t}\n\telse if (code==9) //9 code stands for tab key \n\t{\n\t\tvar fromdated = Number(document.getElementById("fromdated").value);\n\t\tvar fromdatem = Number(document.getElementById("fromdatem").value);\n\t\tvar todatem = document.getElementById("todatem");\n\t\ttodatem.value =  fromdatem;\n\t\tvar todated = document.getElementById("todated");\n\t\t\n\t\tvar _thisMonth = new Date().getMonth();\n\t\t\n                if (fromdatem!=""&&!isNaN(fromdatem)){\n\n                }\n                else{\n                        todatem.value=_thisMonth;\n                        alert(\'Month Cannot be Null\');\n                        document.getElementById(\'fromdated\').focus();      \n                }\n\t\n\t\t\n\t\tif (fromdated == "01")\n\t\t{         \n                        todatem.value =  fromdatem - 01;\n                        todated.value=new Date().getDate();\n                        \n                        if(fromdated=="01" && fromdatem==""){\n                                  todatem.value = new Date().getMonth();\n                        }\n\t\t\tif (fromdatem == "01")\n\t\t\t{\n\t\t\t\ttodatem.value = 12;\n\t\t\t}\n\t\t          \n\n\t\t\tif (fromdatem  == "05" || fromdatem  == "07"  || fromdatem  == "10" || fromdatem  == "12")\n\t\t\t{\n\t\t\t\ttodated.value=30;\n\t\t\t}\n\t\n\t\t\t\t\n\t\t\tif (fromdatem  == "04" || fromdatem  == "06" || fromdatem  == "02"|| fromdatem == "09" || fromdatem  == "11" || fromdatem == "01" || fromdatem  == "08")\n\t\t\t{\n\t\t\t\ttodated.value=31;\n\t\t\t}\n\t\n\t\t\n\t\t\tif (fromdatem  == "03")\n\t\t\t{\n\t\t\t\ttodated.value=28;\n\t\t\t}\n\t\t}\n\t\t\t\n\t\t\telse\n\t\t\ttodated.value=fromdated-01;\n\t\t\tvar _thisDate = new Date().getDate();\n\t\t\n                        if (fromdated!=""&&!isNaN(fromdated)){\n\n                         }\n                        else{\n                \n                                todated.value=_thisDate;\n                                alert(\'Date Cannot be Null\');\n                                document.getElementById(\'organisationType\').focus();      \n                        }\n\t\t\tif (todatem.value < 10)\n\t\t\t{\n\t\t\t\ttodatem.value = "0" + todatem.value\n\t\t\t}\n\t\t\tif (todated.value < 10)\n\t\t\t{\n\t\t\t\ttodated.value = "0" + todated.value\n\t\t\t}\n\t\t\t\n\t}\n}\n\n</script>\n<script>\n//function to calculate month of \'To Date\'  by click event\nfunction onClickMonth(e,s)\n{\n\tif (!e) var e = window.event;\n\tif (e.keyCode) code = e.keyCode;\n\telse if (e.which) code = e.which;\n\t\n\t\tvar fromdated = Number(document.getElementById("fromdated").value);\n\t\tvar fromdatem = Number(document.getElementById("fromdatem").value);\n\t\tvar todatem = document.getElementById("todatem");\n\t\ttodatem.value =  fromdatem;\n\t\tvar todated = document.getElementById("todated");\n\t\tdocument.getElementById(\'fromdatey\').focus(); \n\t\t var _thisMonth = new Date().getMonth();\n\t\t\n                if (fromdatem!=""&&!isNaN(fromdatem)){\n\n                }\n                else{\n                        todatem.value=_thisMonth;\n                        alert(\'Month Cannot be Null\');\n                        document.getElementById(\'fromdatem\').focus();      \n                }\n\t\n\t\tif (fromdated == "01")\n\t\t{         \n                        todatem.value =  fromdatem - 01;\n                        todated.value=new Date().getDate();\n                        \n                        if(fromdated=="01" && fromdatem==""){\n                                  todatem.value = new Date().getMonth();\n                        }\n\t\t\tif (fromdatem == "01")\n\t\t\t{\n\t\t\t\ttodatem.value = 12;\n\t\t\t}\n\t\t          \n\n\t\t\tif (fromdatem  == "05" || fromdatem  == "07"  || fromdatem  == "10" || fromdatem  == "12")\n\t\t\t{\n\t\t\t\ttodated.value=30;\n\t\t\t}\n\t\n\t\t\t\t\n\t\t\tif (fromdatem  == "04" || fromdatem  == "06" || fromdatem  == "02"|| fromdatem == "09" || fromdatem  == "11" || fromdatem == "01" || fromdatem  == "08")\n\t\t\t{\n\t\t\t\ttodated.value=31;\n\t\t\t}\n\t\n\t\t\n\t\t\tif (fromdatem  == "03")\n\t\t\t{\n\t\t\t\ttodated.value=28;\n\t\t\t}\n\t\t\t\n\t\t}\n\t\t\t\n\t\t\telse\n\t\t\ttodated.value=fromdated-01;\n\t\t\t var _thisDate = new Date().getDate();\n\t\t         if (fromdated!=""&&!isNaN(fromdated)){\n\n                         }\n                         else{\n                \n                                todated.value=_thisDate;\n                                alert(\'Date Cannot be Null\');\n                                document.getElementById(\'fromdated\').focus();      \n                        }\n\t\t\tif (todatem.value < 10)\n\t\t\t{\n\t\t\t\ttodatem.value = "0" + todatem.value\n\t\t\t}\n\t\t\tif (todated.value < 10)\n\t\t\t{\n\t\t\t\ttodated.value = "0" + todated.value\n\t\t\t}\n\t\t\t\n\t\t          \n\t}\n\n\n</script>\n<script>\n//function to calculate year of \'To Date\' \nfunction toYear(e,s)\n{\n\tif (!e) var e = window.event;\n\tif (e.keyCode) code = e.keyCode;\n\telse if (e.which) code = e.which;\n\tif (code==13)\n\t{\n\t\tvar fromdatey = parseInt(document.getElementById("fromdatey").value);\n                var todatey = document.getElementById("todatey");\n                todatey.value = fromdatey + 1;\n                document.getElementById(\'todated\').focus();\n\t\tvar fromdatem = parseInt(document.getElementById("fromdatem").value);\n\t\tvar todated = document.getElementById("todated");\n\t\tdocument.getElementById(\'todated\').focus();\n                var _thisYear = new Date().getFullYear();\n\t\t\n                if (fromdatey!=""&&!isNaN(fromdatey)){\n\n                }\n                else{\n                        todatey.value=_thisYear;\n                        alert(\'Year Cannot be Null\');\n                        document.getElementById(\'fromdatey\').focus();      \n                }\n\n\t\tif (fromdatem == "03" && fromdatey % 4 == 0 && (!(fromdatey % 100 == 0) || fromdatey % 400 == 0 && fromdatem == "02"))\n\t\t{\n\t\t \ttodated.value=28;\n\t\t}\n\t\tif(fromdatem=="03" && fromdatey % 4 != 0 && (!(fromdatey % 100 == 0) || fromdatey % 400 != 0 && fromdatem == "02"))\n\t\t{\n\t\t\ttodated.value=28;\n\t\t}\n\t\tif (fromdatem == "03" && (fromdatey + 1) % 4 == 0 && (!((fromdatey + 1)  % 100 == 0) || (fromdatey + 1) % 400 == 0 && fromdatem == "02"))\n\t\t{\n\t\t\ttodated.value=29;\n\t\t}\n\t}\n\telse if (code==9) //9 code stands for tab key \n\t{\n\t\tvar fromdatey = parseInt(document.getElementById("fromdatey").value);\n                var todatey = document.getElementById("todatey");\n                todatey.value = fromdatey + 1;\n                \n\t\tvar fromdatem = parseInt(document.getElementById("fromdatem").value);\n\t\tvar todated = document.getElementById("todated");\n                var _thisYear = new Date().getFullYear();\n\t\t\n                if (fromdatey!=""&&!isNaN(fromdatey)){\n\n                }\n                else{\n                        todatey.value=_thisYear;\n                        alert(\'Year Cannot be Null\');\n                        document.getElementById(\'fromdatem\').focus();      \n                }\n\n\t\tif (fromdatem == "03" && fromdatey % 4 == 0 && (!(fromdatey % 100 == 0) || fromdatey % 400 == 0 && fromdatem == "02"))\n\t\t{\n\t\t \ttodated.value=28;\n\t\t}\n\t\tif(fromdatem=="03" && fromdatey % 4 != 0 && (!(fromdatey % 100 == 0) || fromdatey % 400 != 0 && fromdatem == "02"))\n\t\t{\n\t\t\ttodated.value=28;\n\t\t}\n\t\tif (fromdatem == "03" && (fromdatey + 1) % 4 == 0 && (!((fromdatey + 1)  % 100 == 0) || (fromdatey + 1) % 400 == 0 && fromdatem == "02"))\n\t\t{\n\t\t\ttodated.value=29;\n\t\t}\n\t}\n}\n</script>\n<script>\n//function to calculate year of \'To Date\'  by click event\nfunction onClickYear(e,s)\n{\n\tif (!e) var e = window.event;\n\tif (e.keyCode) code = e.keyCode;\n\telse if (e.which) code = e.which;\n\t\n\t\tvar fromdatey = parseInt(document.getElementById("fromdatey").value);\n                var todatey = document.getElementById("todatey");\n                todatey.value = fromdatey + 1;\n              \n\t\tvar fromdatem = parseInt(document.getElementById("fromdatem").value);\n\t\tvar todated = document.getElementById("todated");\n                var _thisYear = new Date().getFullYear();\n\t\t\n                if (fromdatey!=""&&!isNaN(fromdatey)){\n\n                }\n                else{\n                        todatey.value=_thisYear;\n                        alert(\'Year Cannot be Null\');\n                        document.getElementById(\'fromdatey\').focus();      \n                }\n\n\t\tif (fromdatem == "03" && fromdatey % 4 == 0 && (!(fromdatey % 100 == 0) || fromdatey % 400 == 0 && fromdatem == "02"))\n\t\t{\n\t\t \ttodated.value=28;\n\t\t}\n\t\tif(fromdatem=="03" && fromdatey % 4 != 0 && (!(fromdatey % 100 == 0) || fromdatey % 400 != 0 && fromdatem == "02"))\n\t\t{\n\t\t\ttodated.value=28;\n\t\t}\n\t\tif (fromdatem == "03" && (fromdatey + 1) % 4 == 0 && (!((fromdatey + 1)  % 100 == 0) || (fromdatey + 1) % 400 == 0 && fromdatem == "02"))\n\t\t{\n\t\t\ttodated.value=29;\n\t\t}\n\t}\n\n</script>\n\n\n<img src="/jquery/images/start.png" alt="background" id="bg" /> \n</head>\n<body onload="document.getElementById(\'selectorg\').focus()" onkeypress="keyright(event,\'selectorg\')"> \n\n<div  align="top" id="content" name="content">\n<div align="center" class="start1">\n<br>\n<fieldset id="fieldset_start"><legend ><strong><h3>Welcome</h3></strong></legend>  \n<p id="firstpara"><br>\n<font size=5><b>GNUKhata A Free And Open Source Accounting Software</font>\n<h3 align= "center"><font size=4>http://gnukhata.org</h3>\n\n<hr style="color:#0044FF" width=90% height =80% id="separator"><br>\n<table id="tbl" align="center">\n<tr>\n\t<td align="center"><font color="#0022FF">Features Of GNUKhata:<br></td>\n</tr>\n<tr>\n\t<td align="left"><font color="#0022FF">\n\t<ul>\n\t\t<li> &nbsp; It is lightweight</li>\n\t\t<li> &nbsp; It is scalable</li>\n\t\t<li> &nbsp; It is fast and robust</li>\n\t\t<li> &nbsp; It can be deployed for profit and non-profit organisations</li>\n\t</ul>\n\t</td>\n</tr>\n</table>\n</fieldset>\n<fieldset id="fieldset_start"><legend ><strong></strong></legend>  \n\n<h3 align= "center"><font size=4>previous = \u21e7, nextbutton = \u21e9, next = enter, checkbox = space</h3></fieldset>\n</p>\n</div>\n<br><img class="start_logo" alt="logo"  src="/images/finallogo.png"><br><br>\n<div align="center" class="start2">\n<br><br><br>\n<form id="frm_login" method = "post" action=')
        # SOURCE LINE 1039
        __M_writer(escape(h.url_for(controller='startup',action='login')))
        __M_writer(u'>\n<input type="button" name="selectorg" id="selectorg" onkeydown="keydowns(event,\'organisation\')" onkeypress="keydowns(event,\'neworg\')" onkeyup="keydown(event,\'organisation\')" value="Select Existing Organisation">\n<input type="hidden" name="countdown" size="3" value="15">\n<input type="hidden" name="yearfromdate" id="yearfromdate">\n<input type="hidden" name="yeartodate" id="yeartodate">\n<input type="hidden" name="yearfrom" id="yearfrom">\n<input type="hidden" name="yearto" id="yearto">\n<div id="toggle1" style="display:none;"><br><br>\t\t\t\n\t<table border="0" cellpadding="1" cellspacing="1" width="60%">\n\t<tr>\n\t\t<td><label for="organisation"><font size="3">Organisation Name</label></td>\n\t\t<td><select id="organisation" name="organisation" style = "Height:30px;Width: 200px;font-size:18px;" onkeyup="orgtoselect()">\n\t\t\t<option >--Select--</option>\n')
        # SOURCE LINE 1052
        for org in c.organisations:
            # SOURCE LINE 1053
            __M_writer(u'\t\t\t<option>')
            __M_writer(escape(org))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 1055
        __M_writer(u'\t\t\t</select>\n\t\t</td>\n\t\t<td></td>\n\t</tr>\n\t<tr></tr>\n\t<tr>\n\t\t<td ><label for="financial year" id="financial year_lbl"><font size="3">For Financial Year </label></td>\n\t\t<td><select id="financial year" onkeypress="keyup(event,\'organisation\')" style = "Height:30px;Width: 200px;font-size:18px;" onkeyup="keydown(event,\'NextLogin\')" name="financial year" ><option></option></select></td>\n\t\t\n\t</tr>\t\t\n\t<tr>\n\t\t<td colspan="1"></td>\n\t\t<td><input type="submit" id="NextLogin" onkeypress="keyup(event,\'financial year\')" value="Proceed" src="/images/button.png"></td>\n\t</tr>\n\t</table>\n</div>\n</form>\n<form id="frm_new" method = "post" action=')
        # SOURCE LINE 1072
        __M_writer(escape(h.url_for(controller='startup',action='render_initialsetup')))
        __M_writer(u'><br>\n<input type="button" 8name="neworg" id="neworg" onkeyup="keydown(event,\'orgname\')" onkeypress="keyup(event,\'selectorg\')" onkeydown="keydowns(event,\'orgname\')" value="Create  New  Organisation">\n<div id="toggle2" style="display:none;">\n\t<table border ="0" width="60%" cellpadding="1" cellspacing="1">\n\t<tr>\n\t\t<td width="15%"><font size="3">Organisation Name</td>\n\t\t<td width="60%">\n\t\t<input type="text" id="orgname" onchange = "change_case();" style = "Height:30px;Width: 200px;font-size:18px;" onkeypress="keydown(event,\'organisationType\')" onKeydown="return disableEnterKey(event)" onKeyup="keyup(event,\'neworg\')" name="orgname"  class="Required" maxlength="50"><br><font size="3">(Maximum Characters: 50)</td>\n\t</tr>\t\n\t<tr>\n\t\t<td><font size="3">Organisation Type<br></td>\n\t\t<td>\n\t\t\t<select id="organisationType" style = "Height:40px;Width: 200px;font-size:19px;"  name="organisationType" onkeyup="typetoname()" onkeypress="keydown(event,\'fromdated\')" onKeydown="return disableEnterKey(event)">\n\t\t\t<option>Profit Making</option>\n\t\t\t<option>NGO</option>\n\t\t\t</select>\n\t\t\t\n\t\t</td>\n\t</tr>\n\t</tr>\n\t<tr>\n\t\t<td><font size="3">Financial Year</td>\n\t\t<td>\n\t\t\t<table>\n\t\t\t<tr><td><font size="3">From Date:<input type="text" size="1" style = "Height:30px;Width: 30px;font-size:18px;" maxlength="2" id="fromdated" onchange="validate(this);" onKeydown="return disableEnterKey(event)" onkeypress="keydown(event,\'fromdatem\')" onkeyup="keyup(event,\'organisationType\')"  name="fromdated" class="dated" onblur="CheckTextboxBlank();">-<input type="text" maxlength="2" style = "Height:30px;Width: 30px;font-size:18px;" id="fromdatem" onchange="validmonth(this);" onKeydown="return disableEnterKey(event)" onkeypress="toMonth(event,\'fromdatey\')" onkeyup="keyup(event,\'fromdated\')"   size="1" name="fromdatem" class="datem" onfocus="kk2()">-<input type="text" style = "Height:30px;Width: 80px;font-size:18px;" onchange="validyear(this);" size="2" id="fromdatey" onkeypress="toYear(event,\'todated\')" maxlength="4" onclick="onClickMonth(event,\'fromdatey\');"  onkeyup="keyup(event,\'fromdatem\')" onKeydown="return disableEnterKey(event)" name="fromdatey" class="datey">\n\t\t<br>\n\t\tTo Date :&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" size="1" maxlength="2" id="todated" onkeypress="keydown(event,\'todatem\')" onkeyup="keyup(event,\'fromdatey\')" onchange="validate(this);" style = "Height:30px;Width: 30px;font-size:18px;" onKeydown="return disableEnterKey(event)" name="todated" class="dated">-<input type="text" maxlength="2" id="todatem" onkeypress="keydown(event,\'todatey\')" onchange="validmonth(this);" onchange="validmonth(this);" style = "Height:30px;Width: 30px;font-size:18px;" onkeyup="keyup(event,\'todated\')" onKeydown="return disableEnterKey(event)" size="1" name="todatem" class="datem" >-<input type="text" size="2" maxlength="4" onclick="onClickYear(event,\'todated\');" onchange="validyear(this);" id="todatey" onkeyup="keydown(event,\'newsubmitbutton\')" maxlength="4" style = "Height:30px;Width: 80px;font-size:18px;" onkeypress="keyup(event,\'todatem\')" onKeydown="return disableEnterKey(event)" name="todatey" class="datey" ></td></tr>\t\n\t\t\t</table>\n\t\t</td>\n\t</tr><br>\n\t<tr>\n\t\t<td width ="30%"></td>\n\t\t<td width ="50%" align = "center"><input id="newsubmitbutton"  onkeyup="keyup(event,\'todatey\')" type="submit" value="Next" src="/images/button.png" enabled="false"></td></tr>\n\t</table>\n</div>\n</form>\t\n</div>\n</div> \t\t\t\t\t\n</body>\n</html>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()

