// confirm form submissions
$( '#expenseform' ).submit(function( event ) {

    var currentForm = this;
    bootbox.confirm("Are you sure you want to submit the expense?", function( result ) {
        if( result ) {
            currentForm.submit();
        }
        
    });
    event.preventDefault();
});

// add expenses when clicked
$( '.expense').click(function( event ){
    // get the ordered id the expense clicked - NOT primary key
    var currentId = $(this).attr('id').match(/\d+$/);

    // retrieve all expenses and find the current clicked
    // (all expenses is defined in the footer of index.html)
    var expense = all_expenses[currentId - 1]['fields'];


    // set the value of each form attribute to the matching expense
    $( "#id_name" ).attr('value', expense['name']);
    $( "#id_expense_type" ).val(expense['expense_type']);
    $( "#id_amount" ).val(expense['amount']);
    $( "#id_date" ).val(expense['date']);

});