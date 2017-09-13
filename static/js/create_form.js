function create_choice_form(label_name, propriety_name, choices) {
    var form = document.createElement("form");
    form.setAttribute('id', propriety_name);
    var label = document.createElement("label");
    label.innerHTML = label_name;
    form.append(label);
    var break_line = document.createElement("br");
    form.append(break_line);
    for (var i = 0, length = choices.length; i < length; i++) {
        var input = document.createElement("input");
        input.type = "radio";
        input.name = propriety_name;
        input.id = choices[i];
        input.value = choices[i];
        form.appendChild(input);
        var label = document.createElement("label");
        label.innerHTML = choices[i];
        form.append(label);
        var break_line = document.createElement("br");
        form.append(break_line);
    }
    return form;
}

function create_final_form(schema, content_type) {
    var global_form = document.createElement("form");
    var content_types = Object.keys(schema.content_types);

    var proprieties = schema.content_types[content_type];
    var propriety = "";
    var choices = [];
    var form = document.createElement("form");

    for (var i = 0, length = proprieties.length; i < length; i++) {
        propriety = proprieties[i];
        choices = schema.proprieties[schema.content_types[content_type][i]];
        form = create_choice_form(propriety, propriety, choices);
        global_form.appendChild(form)
    }
    return global_form;
}

function collect_all(){
    var result = $('form').serializeArray();
    // ADD AJAX POST HERE TO SEND RESULTS TO SERVER
    console.log(result);
}

function select_content_type(){
    content_type = $('input[name="content_type"]:checked').val();
    form = create_final_form(schema, content_type);
    $("#content_type").hide();
    $("#content_type_button").hide();
    $("#form_container").append(form);
    $("#submit_button").show();
}

$(document).ready(function() {
    var content_types = Object.keys(schema.content_types);
    form = create_choice_form('Content type', 'content_type', content_types);
    $("#form_container").append(form);
});
