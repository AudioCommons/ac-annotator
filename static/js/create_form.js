function create_choice_form(content_type, propriety_name, choices) {
    var form = document.createElement("form");
    form.setAttribute('id', propriety_name);
    var label = document.createElement("label");
    label.innerHTML = propriety_name;
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

function create_form(schema) {
    var global_form = document.createElement("form");
    global_form.setAttribute('method',"post");
    global_form.setAttribute('action',"");

    var content_types = Object.keys(schema.content_types);

    var content_type = content_types[1];
    var proprieties = schema.content_types[content_type];
    var propriety = "";
    var choices = [];
    var form = document.createElement("form");

    for (var i = 0, length = proprieties.length; i < length; i++) {
        propriety = proprieties[i];
        choices = schema.proprieties[schema.content_types[content_type][i]];
        form = create_choice_form(content_type, propriety, choices);
        global_form.appendChild(form)
    }

    return global_form;
}

function collectAll(){
    var result = $('form').serializeArray();
    // ADD AJAX POST HERE TO SEND RESULTS TO SERVER
    console.log(result);
}

$(document).ready(function() {
    form = create_form(schema);
    $("#form_container").append(form);
});