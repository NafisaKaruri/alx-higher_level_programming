$(document).ready(function(){
    $("#btn_translate").click(function(event) {
        let url = "https://www.fourtonfish.com/hellosalut/hello/" + $("#language_code").val();

        $.get(url, function(data) {
            $("#hello").text(data.hello);
        });
    });
});
