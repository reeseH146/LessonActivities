function FormValidation(FormObj) {
    // Form data stored as variables
    let FName = FormObj.elements.item(1).value;
    let LName = FormObj.elements.item(2).value; 
    let Email = FormObj.elements.item(3).value;
    let DateOfSub = new Date(FormObj.elements.item(4).value);
    let Description = FormObj.elements.item(5).value;

    // Error variables
    let Errors = "";
    let NoErrors = true;

    // Error Checking and logs it
    // alert(typeof DateOfSub); // Used to debug the types of variables so can properly be compared
    if (FName == "") {
        Errors += " - You must have a first name!";
        NoErrors = false;
    };
    if (LName == "") {
        Errors += "\n - You must have a last name!";
        NoErrors = false;	
    };

    // Sends data off if valid
    if (NoErrors) {
	return [NoErrors, FName, LName, Email, DateOfSub, Description];
    }
    else {
        alert(Errors);
    }
}

document.addEventListener("DOMContentLoaded", function(event) { // On loading of full page, runs code
    const Form = document.getElementById("FormName");           // Identifies form
    const Output = document.getElementById("Output");           // Identifies output

    Form.addEventListener("submit", function(event) {                // Executes code when the Form is submitted
    alert("please work");                                       // Encourages the code to work
    event.preventDefault();                                     // When submitted, prevents page from refreshing/updating?
    let FormData = FormValidation(Form);                        // Validation
    if (FormData) {                                             // Changes the output box
        document.getElementById("OutBox").innerHTML = FormData[1];
    }
    alert("This code has ran");
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