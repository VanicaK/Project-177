$document.ready(function(){
    getTemplates()
})

function getTemplates(){
    $.ajax({
        url:"/get-template",
        type:"get",
        success:function(result){
            fillBlanks(result.word)
        },
        error:function(result){
            alert(result.responseJSON.message)
        }
    })
}