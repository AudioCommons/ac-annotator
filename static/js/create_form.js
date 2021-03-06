function create_choice_form(label_name, property_name, choices) {
    var form = document.createElement("form");
    form.setAttribute('id', property_name);
    var label = document.createElement("label");
    label.innerHTML = label_name;
    label.style.fontWeight= '600';
    form.append(label);
    var break_line = document.createElement("br");
    form.append(break_line);
    for (var i = 0, length = choices.length; i < length; i++) {
        var input = document.createElement("input");
        input.type = "radio";
        input.name = property_name;
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

function create_data_list_form(label_name, property_name, choices) {
    var form = document.createElement("form");
    form.setAttribute('id', property_name);
    form.setAttribute('onsubmit', "return false");
    var label = document.createElement("label");
    label.innerHTML = label_name;
    label.setAttribute('for', 'choice_' + property_name)
    form.append(label);
    var select = document.createElement("select");
    select.setAttribute('id', 'choice_' + property_name);
    select.setAttribute('name', 'choice_' + property_name);
    for (var i = 0, length = choices.length; i < length; i++) {
        var option = document.createElement("option");
        option.value = choices[i];
        option.innerHTML = choices[i];
        select.appendChild(option);
    }
    form.append(select);
    return form
}

function create_final_form(schema, content_type) {
    var global_form = document.createElement("form");
    var content_types = Object.keys(schema.content_types);

    var properties = schema.content_types[content_type];
    var property = "";
    var choices = [];
    var form = document.createElement("form");

    for (var i = 0, length = properties.length; i < length; i++) {
        property = properties[i];
        choices = schema.properties[schema.content_types[content_type][i]];
        //form = create_choice_form(property, property, choices);
        form = create_data_list_form(property, property, choices);
        global_form.appendChild(form)
    }
    return global_form;
}

function collect_all(schema){
    var content_type_result = $('#content_type').serializeArray()[0]["value"];
    var result = {'content_type': content_type_result};
    var properties = schema.content_types[content_type_result];
    for (var i = 0, length = properties.length; i < length; i++) {
        result[properties[i]] = $('#choice_'+properties[i]).val();
    }
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
