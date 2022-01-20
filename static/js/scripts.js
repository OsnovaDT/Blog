$('#user_dropdown_menu_arrow').on('click', function(){
    if ($('#user_dropdown_menu').is(':visible')){
        console.log(1);
        $('#user_dropdown_menu').hide();
    }
    else{
        console.log(2);
        $('#user_dropdown_menu').show();
    }
});
