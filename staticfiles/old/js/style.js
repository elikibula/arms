$(document).ready(function() {
    $('#arm-table').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": "{% url 'arm_list_json' %}",
        "columns": [
            {"data": "regimental_number"},
            {"data": "name"},
            {"data": "rank"},
            {"data": "unit"},
            {"data": "arm_type"},
            {"data": "arm_status"},
            {"data": "location"}
        ]
    });
});