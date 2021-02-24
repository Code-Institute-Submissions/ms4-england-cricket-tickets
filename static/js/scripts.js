
     $(document).ready(function(){
    //The following functions are used to initialise Materialize CSS
    $('.sidenav').sidenav({edge: "right"});
    $(".dropdown-trigger").dropdown({alighment: "bottom"}); 
    $('select').formSelect();
    $('.collapsible').collapsible();
    $(".hide-messages").click(function(e){
        $(".messages").addClass("hidden");
    });
     

});
