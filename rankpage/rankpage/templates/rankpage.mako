<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<script src="../static/js/jquery-3.4.1.min.js" type="text/javascript"></script>

<title>MedNLP-Experiment</title>

<script>
function rankinfo() {	
    var rank_name = document.getElementById("name").value;
    var rank_tfidf = document.getElementById("tfidf").value;
    var rank_size = document.getElementById("size").value;
    var rank_epoch = document.getElementById("epoch").value;
    var rank_batchsize = document.getElementById("batchsize").value;
    var rank_learningrate = document.getElementById("learningrate").value;
    var rank_macrof1 = document.getElementById("macrof1").value;
    var rankinfo_tbody=window.document.getElementById("tbody-rankinfo");

    
    $.ajax({
        method: "POST", 
        url: "/test/rankinfo",
        data: JSON.stringify({name:rank_name, tfidf:rank_tfidf, size:rank_size, epoch:rank_epoch, batchsize:rank_batchsize, learningrate:rank_learningrate, macrof1:rank_macrof1}),
        success: function(rankinfo){
            console.log(rankinfo);
          
            var inclusion_sentences = rankinfo;
            var in_str = "";
            for (i in inclusion_sentences) {
                in_str += "<tr>" + 
                          "<td>" + inclusion_sentences[i][0] + "</td>" +
                          "<td>" + inclusion_sentences[i][1] + "</td>" +
                          "<td>" + inclusion_sentences[i][7] + "</td>" +
                          "<td>" + inclusion_sentences[i][2] + "</td>" +
                          "<td>" + inclusion_sentences[i][3] + "</td>" +
                          "<td>" + inclusion_sentences[i][4] + "</td>" +
                          "<td>" + inclusion_sentences[i][5] + "</td>" +
                          "<td>" + inclusion_sentences[i][6] + "</td>" +
                          "</tr>"
                }
            rankinfo_tbody.innerHTML = in_str;
            
        },
        error: function(){
            console.log("error...");
            alert("查询失败");
        }
    });
    
}
</script>


</head>

<body>
 
<!-- <div id="container" style="width:100%"> -->
 
<div id="header" style="background-color:#4CB4E7;">
<h1 style="margin-bottom:0;">Experiment of Medical Natural Language Processing: Clinical Trials Eligibility Criteria Classification</h1></div>
 
<div id="menu" style="background-color:#FFEE97;width:100%;float:left;">
<form>
<h2>填入信息：</h2>
姓名：<br>
<input id="name" type="text" name="name" required="required"><br>
TFIDF词向量长度：<br>
<input id="tfidf" type="text" name="tfidf" required="required"><br>
神经网络size<br>
<input id="size" type="text" name="size" required="required"><br>
迭代期(Epoch)<br>
<input id="epoch" type="text" name="epoch" required="required"><br>
批大小(batch size)<br>
<input id="batchsize" type="text" name="batchsize" required="required"><br>
学习率(learning rate)<br>
<input id="learningrate" type="text" name="learningrate" required="required"><br>
Macro-F1score<br>
<input id="macrof1" type="text" name="macrof1" required="required"><br>

</form>

<!-- <form id="upform" enctype='multipart/form-data' action="http://130.147.222.117:6543/rank/uploadfiles" method = "post">
    <div class="form-group">
    	<br>
        <label for="upteainput">上传测试数据预测结果文件</label>
        <input id="upteainput" name="upfile" type="file" class="form-control-file">
    </div>
</form> -->


</div>
 
<div id="content" style="background-color:#E2DBBE;width:100%;float:left;">
	<h2>排名信息：</h2>
	<button type="button" onclick="rankinfo()">更新排名</button>
    <table id = "rankinfo" width="100%" cellspacing="0" cellpadding="0" border="0" align="left">
    <thead> 
    <tr>
    <th align="left">Rank</th>
    <th align="left">姓名</th>
    <th align="left">Macro-F1score</th>
    <th align="left">TFIDF词向量长度</th>
    <th align="left">神经网络size</th>
    <th align="left">迭代期(Epoch)</th>
    <th align="left">批大小(batch size)</th>
    <th align="left">学习率(learning rate)</th>
    </tr>
    </thead>
    <tbody id="tbody-rankinfo">
    </tbody>
    </table>


</div>
 
<div id="rankinfos" style="background-color:#FFC09F;clear:both;text-align:center;">
</div>
 
</div>
 
</body>
</html>