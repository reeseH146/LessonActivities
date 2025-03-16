function FormValidation(FormObj) {
    // Form data stored as variables
    let FName = FormObj.elements.item(1).value;
    let LName = FormObj.elements.item(2).value; 
    let Email = FormObj.elements.item(3).value;
    let DateOfSub = new Date(FormObj.elements.item(4).value);
    let Description = FormObj.elements.item(5).value;

    // Error variables
    let Errors = ``;
    let NoErrors = false;

    // Error Checking and logs it
    // alert(typeof DateOfSub); // Used to debug the types of variables so can properly be compared
    if (FName == "") {
        Errors.concat(` - You must have a first name!`);
        NoErrors = false;
    };
/*
    if (LName == "") {
        Errors += ` - You must have a last name!`;
        NoErrors = False;	
    };*/

    // Sends data off if valid
    if (NoErrors) {
        FormOutput();
    }
    else {
        alert(Errors);
    }
}

function FormOutput() {
    alert("FormOutput() works");
}

document.addEventListener("DOMContentLoaded", function(event) { // On loading of full page, runs code
    const Form = document.getElementById("FormName");      // Identifies form
    const Output = document.getElementById("Output");      // Identifies output

    Form.addEventListener("submit", function() {
	alert("please work");        
        event.preventDefault(); // Prevents submit when loaded and only when called?

        FormValidation(Form);                              // Validation
    });
});

/*
 # Requirements : 
 
 + Input validation
 - All inputs must be given apart from date and textarea
 - Email must have at lease 1 "." and only 1 "@"
 - Date must be in DD/MM/YYYY form and a suitable date (01/01/1900 - 01/01/currentYear++)

 + Output
 - Alert `Thank you for completing the form.\n${FirstName[0:3] + SecondName[0:3]}`
 - Probably store or send off data somehow

 + Easter egg
 - If name is Ralfs Varpins, alert : sod off Mr 10K SRQ
 - Reset textarea if length >,000 char
*/


/*
let TextArea = document.getElementById("TextBox");
TextArea.addEventListener("input", function() {
    if (this.value.length >= 10) {
        this.value = "Too full! BURPP";
    }
});
*/