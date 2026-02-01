function bindUploadPicture(){
    $("#image-upload").on("change", function(event){
        const file = event.target.files[0];
        if(!file) return;

        const formData = new FormData();
        formData.append("picture", file);

        $.post({
            url: "/upload/picture",
            data: formData,
            // 普通的表单数据,默认会进行json预处理,图片不需要处理
            processData: false,
            contentType: false,
            success: function (result){
                const category = result['category'];
                const filename = result['filename'];

                console.log(category);
                console.log(filename);

                let imagePreview = $("#image-preview");
                //  添加图片的url
                imagePreview.attr("src", "/media/" + filename);
                // 让图片显示突来
                imagePreview.removeClass("hidden");
                // 让svg隐藏起来
                $("#image-placeholder").addClass("hidden");

                // 让下来菜单选择某个option
                $("#category").val(category.id);
                $("#picture").val("/media/" + filename);
            }
        })
    });
}

$(function (){
    bindUploadPicture();
});