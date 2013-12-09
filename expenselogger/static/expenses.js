// confirm form submissions
$( '#expenseform' ).submit(function( event ) {

    var currentForm = this;
    bootbox.confirm("Are you sure you want to submit the expense?", function( result ) {
        if( result ) {
            currentForm.submit();
        }
        
    });
    return false;
});

// add expenses when clicked
$( '.expense').click(function( event ){
    // get the data for the clicked expense
    // expense data is embedded in tr tag
    var expense = $(this).data('expense')[0]['fields'];


    // set the value of each form attribute to the matching expense
    $( "#id_name" ).attr('value', expense['name']);
    $( "#id_expense_type" ).val(expense['expense_type']);
    $( "#id_amount" ).val(expense['amount']);
    $( "#id_date" ).val(expense['date']);

});