$(document).ready(function() {
    $("#add").click(function() {
        var fieldSet = $("#yourform")
        var length = $("#yourform input").length;
        var id = "input" + length;
        var fieldWrapper = $("<div class=\"fieldwrapper\" id=\"field" + id + "\"/>");
        var label = $("<label for=\"" + id + "\">" + 'timestamp'     + "</label>");
        var input = $("<input type=\"text\" class=\"input\" id=\"" + id + "\" name=\"" + id + "\" />");
        var removeButton = $("<input type=\"button\" class=\"remove\" value=\"-\" />");
        removeButton.click(function() {
            $(this).parent().remove();
        });
        fieldWrapper.append(label);
        fieldWrapper.append(input);
        fieldWrapper.append(removeButton);
        $("#yourform").append(fieldWrapper);
    });
    $("#launch").click(function() {
        var fieldSet = $("#yourform .input")
        timestamps = []
        fieldSet.each(function()  {
            timestamps.push($(  this ).val());
        })
        filepath = $('video source').attr('src')
        $.ajax({
          type: "POST",
          contentType: "application/json; charset=utf-8",
          url: '/shredder',
          data: JSON.stringify({                
                filepath: filepath,
                timestamp: timestamps}),
          success: function (data) {
            console.log(data);
          },
          dataType: "json"
        });

    });

    $("#add").trigger('click');
});