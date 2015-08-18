$(document).ready(function(){

    $('#select_category').on('change', function(){
        var category_id = $(this).val(),
            url='http://localhost:8000/category/'+category_id+'/products/';

        $.get(url, function(result, data){
            console.log(result);
            console.log(data);
            $('#features_items').html(result)
        });
    });


});
