$(document).ready(function() {
    $("#add").click(function() {
        var fieldSet = $("#yourform")
        var length = $("#yourform input").length;
        var id = "input" + length;
        var fieldWrapper = $("<div class=\"fieldwrapper\" id=\"field" + id + "\"/>");
        var label = $("<label for=\"" + id + "\">" + 'timestamp'     + "</label>");
        var input = $("<input type=\"text\" id=\"" + id + "\" name=\"" + id + "\" />");
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
        console.log('hey dof    ')
    });
});