$(document).ready(function() {
    refresh();
});

function refresh() {
    $.get("/refresh", function(a) {
        $.get("/get_data", function(data) {
            $("#table").html(`<tr>
                                        <th>ID</th>
                                        <th>Date</th>
                                        <th>Temperature (C°)</th>
                                        <th>Pression (HPa)</th>
                                        <th>Altitude (m)</th>
				                    </tr>`)

            for(let i=0; i<data.length; i++) {
                let date = new Date(data[i].timestamp * 1000);
                let hours = date.getHours();
                let minutes = "0" + date.getMinutes();
                let seconds = "0" + date.getSeconds();
                var formattedTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);

                console.log(formattedTime);
                $("#table").append(`
                    <tr>
                        <td>${data[i].id}</td>
                        <td>${formattedTime}</td>
                        <td>${data[i].temperature}</td>
                        <td>${data[i].pression}</td>
                        <td>${data[i].altitude}</td>
                    </tr>`);
            }
        })
    })
}


function new_mesure() {
    $.get("/new_mesure", function() {
        alert("La mesure a été faite !")
    })
}
