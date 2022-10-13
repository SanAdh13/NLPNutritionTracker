function makeTable(returnedVal){
    var tableData = ' ';
    $.each(returnedVal, function(index,v){
        // each v is set like [0: n , 1: food name , 2: amount , 3: date]

        tableData += "<tr>";
        tableData += "<td>"+v[1]+'</td>';
        tableData += "<td>"+v[2]+'</td>';
        tableData += "<td>"+v[3]+'</td>';
        tableData += "</tr>";   
    })
    // clear the table before adding the new data 
    $("#userData > tr").remove();
    $('#userData').append(tableData)
}

function makeChart(returnedVal) {
    //TODO: implement this 
    //this one will update the chart 
    $.each(returnedVal,function(i,val){

    });
}

$(function(){
    $('input[name="dateRange"]').daterangepicker({
    }, function(start, end, label) {
        $.ajax({
            type:"POST",
            url:"/getDates",
            data: {from:start.format('YYYY-MM-DD'),
                    to:end.format('YYYY-MM-DD')}
        }).done(function(values){
            
            alert(values)
            //TODO: it should be something like this

            // makeTable(values.tables);
            // makeChart(values.nutrition);


        });
    });
});

$(function(){
    $("#dateSelection").change(function(){
        var data = $(this).val();
        // alert(data)
        $.ajax({
            type:"POST",
            url:"/getGrouped",
            data: {data: data }
        })
        .done(function(returnedVal){
            
            // TODO: do the nutrition retrieval before this cause the JSON format will change again


            console.log(returnedVal);

            // this one is the first array which is the
            returnedVal.forEach(timeframe => {
                // in each timeframe theres 2 index 0: which is the date it corresponds to
                // index 1: which is the array of arrays with the food and their quantities

                console.log(timeframe);
                // var n = (timeframe[0])
                
                // timeframe[1].forEach(food =>{
                //     console.log( food[0] +" | "+food[1] +" | "+ n )
                // });
                

                // e.forEach(Element => {
                //     console.log(e)
                    
                // });
                // console.log(e)
            });

            

            // makeTable(returnedVal)
            // makeChart(returnedVal)
        }); 
    }) 
});

