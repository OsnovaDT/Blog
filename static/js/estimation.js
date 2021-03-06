$(function(){
    $('.image_link').each(function(){
        const postId = $(this).attr('post_id');
        const userId = $(this).attr('user_id');

        let formData = new FormData();

        formData.append('post_id', postId);
        formData.append('user_id', userId);

        $.ajax({
            url: "/post/check_estimation/",
            type: 'POST',
            dataType: "json",
            cache: false,
            contentType: false,
            processData: false,
            data: formData,
            success: function (data) {
                if (data.is_user_liked_this_post){
                    $(`.post_like_amount[post_id="${postId}"]`).addClass('post_liked');
                }

                if (data.is_user_disliked_this_post){
                    $(`.post_dislike_amount[post_id="${postId}"]`).addClass('post_disliked');
                }
            }
        })
    })
});

$('.post_like').on('click', function(){
    const postId = $(this).attr('post_id');
    const userId = $(this).attr('user_id');

    let formData = new FormData();

    formData.append('post_id', postId);
    formData.append('user_id', userId);

    $.ajax({
        url: "/post/like/",
        type: 'POST',
        dataType: "json",
        cache: false,
        contentType: false,
        processData: false,
        data: formData,
        success: function (data) {
            $(`.post_like_amount[post_id=${postId}]`).text(data.likes);
            $(`.post_dislike_amount[post_id=${postId}]`).text(data.dislikes);

            if (data.is_user_liked_this_post){
                $(`.post_like_amount[post_id="${postId}"]`).addClass('post_liked');
                $(`.post_dislike_amount[post_id="${postId}"]`).removeClass('post_disliked');
            }
            else{
                $(`.post_like_amount[post_id="${postId}"]`).removeClass('post_liked');
            }
        }
    })
})

$('.post_dislike').on('click', function(){
    const postId = $(this).attr('post_id');
    const userId = $(this).attr('user_id');

    let formData = new FormData();

    formData.append('post_id', postId);
    formData.append('user_id', userId);

    $.ajax({
        url: "/post/dislike/",
        type: 'POST',
        dataType: "json",
        cache: false,
        contentType: false,
        processData: false,
        data: formData,
        success: function (data) {
            $(`.post_dislike_amount[post_id=${postId}]`).text(data.dislikes);
            $(`.post_like_amount[post_id=${postId}]`).text(data.likes);

            if (data.is_user_disliked_this_post){
                $(`.post_like_amount[post_id="${postId}"]`).removeClass('post_liked');
                $(`.post_dislike_amount[post_id="${postId}"]`).addClass('post_disliked');
            }
            else{
                $(`.post_dislike_amount[post_id="${postId}"]`).removeClass('post_disliked');
            }
        }
    })
})