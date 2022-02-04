$('.post_status').on('click', function(){
    const this_button_status = $(this).attr('status');

    let active_button = $('.post_status_active');

    if (this_button_status === 'post'){
        $('#user_posts').show();
        $('#user_drafts').hide();
    }
    else if (this_button_status === 'draft'){
        $('#user_drafts').show();
        $('#user_posts').hide();
    }

    active_button.addClass('post_status_disabled');
    active_button.removeClass('post_status_active');

    $(this).addClass('post_status_active');
    $(this).removeClass('post_status_disabled');
});
