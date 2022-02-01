$('#user_dropdown_menu_arrow').on('click', function(){
    if ($('#user_dropdown_menu').is(':visible')){
        $('#user_dropdown_menu').hide();
    }
    else{
        $('#user_dropdown_menu').show();
    }
});
